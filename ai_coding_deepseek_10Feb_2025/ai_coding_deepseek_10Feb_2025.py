#install streamlit langchain_core langchain_community langchain_ollama
import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate

# App Title
st.title("🔍 Decoding Data Science AI Coding Companion")
st.caption("🚀 Your AI-Powered Coding Assistant")


# AI Engine
llm_engine = ChatOllama(model="deepseek-r1:1.5b", base_url="http://localhost:11434", temperature=0.3)

# System Prompt
system_prompt = SystemMessagePromptTemplate.from_template(
    "You are an expert AI coding assistant. Provide concise, correct solutions with strategic print statements for debugging."
)

# Generate AI Response
def generate_ai_response(user_input):
    prompt_chain = ChatPromptTemplate.from_messages([
        system_prompt,
        HumanMessagePromptTemplate.from_template(user_input)
    ])
    return (prompt_chain | llm_engine | StrOutputParser()).invoke({})

# Chat Input
user_query = st.chat_input("Type your coding question here...")

if user_query:
    st.write("🧠 AI Response:")
    st.markdown(generate_ai_response(user_query))
