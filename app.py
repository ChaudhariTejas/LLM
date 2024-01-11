# Q&A Chatbot
#from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image


import google.generativeai as genai


os.getenv('AIzaSyD9A3PN1a6ZFp0gWm8MZFzK3IgVhIOji00')
genai.configure(api_key=os.getenv('AIzaSyD9A3PN1a6ZFp0gWm8MZFzK3IgVhIOji00'))

## Function to load OpenAI model and get respones

def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text

# ##initialize our streamlit app

st.set_page_config(page_title="Gemini Image Demo")

st.header("💁‍♂️💁कुछ भी पूछ ले भाई सब बता दूंगा🦹‍♀️🦹‍♀️")
input=st.text_input("Ask any Question Related with Image You Provided : ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("😃😃अबे जल्दी बोल कल सुबह पनवेल निकलना है😃😃")


## If ask button is clicked

if submit:
    
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)
