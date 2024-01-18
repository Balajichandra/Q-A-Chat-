#Q&A ChatBot
#from langchain.llms import OpenAI
from langchain_community.llms import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st
load_dotenv()

##function to load OpenAI model and get response
#text-embedding-ada-002

def get_openai_response(question):
    llm = OpenAI(openai_api_key=os.getenv("OPEN_API_KEY"),model_name="gpt-3.5-turbo-instruct",temperature=0.5)
    response = llm(question)
    return response

##intialize streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain APP")

input = st.text_input("Input: ", key="input")
response = get_openai_response(input)

submit = st.button("Askthe question")

#IF ask button is clicked
if submit:
    st.subheader("The response is...")
    st.write(response)