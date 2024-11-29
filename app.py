
from dotenv import load_dotenv 
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
genai.configure(api_key=os.getenv("google_api_key"))
# model genai.Generativewodel("gemini-flash-1.5")
model=genai.GenerativeModel("gemini-pro")
def my_output(query) -> str:
 response =model.generate_content(query)
 return response.text
st.set_page_config(page_title="AJAY_GURU")
st.header("AJAY_GURU")
input=st.text_input("Input",key="input")
submit=st.button("ask your query")
if submit:
 response=my_output(input)
 st.subheader("The Response is=")
 st.write(response)