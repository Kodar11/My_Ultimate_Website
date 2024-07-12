import streamlit as st 
import json
import requests
from streamlit_lottie import st_lottie

st.header(":mailbox: Get In Touch With Me!!")

# def load_lottiefile(filepath: str):
#     with open(filepath,"r") as f:
#         return json.load(f)
    
# def load_lottieurl(url:str):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()

# code = load_lottiefile(r"C:\Users\Tanmay Chavan\Documents\Computer Science\Python\Pytnon Code\Practice\Streamlit\My_Ultimate_Streamlit_Website\Animation - 1720629687924.json")

# st_lottie(
#     code,
#     speed =1,
#     reverse=False,
#     loop = True,
#     quality= "low"  
# )

contact_form = """
<form action="https://formsubmit.co/tanmay.chavan@walchandsangli.ac.in" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder ="Your Name" required>
     <input type="email" name="email" placeholder = "Your Email" required>
    <textarea name="message" placeholder="Details of your problem"></textarea>
     <button type="submit">Send</button>
</form>"""

st.markdown(contact_form,unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css(r"My_Ultimate_Streamlit_Website\style\style.css")