# Q&A Chatbot
from langchain.llms import HuggingFaceHub
from dotenv import load_dotenv
import streamlit as st
import os

# Load environment variables from .env file
load_dotenv()  # This will load HUGGINGFACEHUB_API_TOKEN from your .env file

## Function to load Hugging Face model and get responses
def get_huggingface_response(question):
    # Make sure we're using the correct environment variable name
    api_token = os.environ.get("HUGGINGFACE_API_TOKEN")
    if not api_token:
        raise ValueError("HUGGINGFACE_API_TOKEN not found in environment variables")
        
    llm = HuggingFaceHub(
        repo_id="google/flan-t5-base",  # You can change this to any Hugging Face model
        huggingfacehub_api_token=api_token
    )
    response = llm(question)
    return response

##initialize our streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Mini Q&A Chatbot")

# Regular input
input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

## If ask button is clicked
if submit:
    try:
        response = get_huggingface_response(inpt)
        st.subheader("The Response is")
        st.write(response)
    except Exception as e:
        st.error(f"Error: {str(e)}")
        st.info("Check that your .env file contains the HUGGINGFACEHUB_API_TOKEN variable")
