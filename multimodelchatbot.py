from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
import streamlit as st

st.set_page_config(
    page_icon="🤖",
    page_title="Chatbot",
    layout="centered"
)

st.title("💬 Multi model Generative AI Chatbot")

model={
    "Groq":["llama-3.3-70b-versatile","qwen/qwen3-32b"],
    "Gemini": ["gemini-2.5-flash","gemini-2.5-pro"],
    
    
}

provider=st.selectbox("Choose Provider",list(model.keys()))
model_name=st.selectbox("Choose model",model[provider])


if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def load_llm(provider, model_name):
    if provider=="Gemini":
        return ChatGoogleGenerativeAI(model=model_name,temperature=0)
    else:
        return ChatGroq(model=model_name,temperature=0)
        
llm=load_llm(provider,model_name)

user_prompt=st.chat_input("Ask chatbot ...")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role":"user","content":user_prompt})
    response=llm.invoke(
        input=[{"role":"system","content":"You are an helpful assistant. Be concise and accurate"},*st.session_state.chat_history]
    )
    assistantresponse=response.content
    st.session_state.chat_history.append({"role":"assistant","content":assistantresponse})
    with st.chat_message("assistant"):
        st.markdown(assistantresponse)