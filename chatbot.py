from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

load_dotenv()

st.set_page_config(
    page_icon="🤖",
    page_title="💬 Chatbot",
    layout="centered"
)
st.title("💬 Genarative AI Chatbot")