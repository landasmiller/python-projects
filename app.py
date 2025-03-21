# Q&A Chatbot
from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os

## Function to load OpenAI model and get responses

def get_openai_response(question):
    llm=OpenAI(api_key=os.getenv("OPENAI_API_KEY"),model_name="text-davinci-003", temperature=0.5)
    response=llm.predict(question)
    return response

    ## initialize streamlit app

st.set_page_config(page_title="Q&A Demo Chatbot")

st.header("LangChain Application")

input=st.text_input("Input: ",key="Input")
response=get_openai_response(input)

submit=st.button("Ask the question")

    ## if ask button is clicked

if submit and user_input:
    response = get_openai_response
    st.subheader("The Response is")
    st.write(response)