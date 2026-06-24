import os
from dotenv import load_dotenv

import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# LangSmith Configuration (Optional)
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

# Groq API Key
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Prompt Template
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful assistant. Please respond to the user's question and give appropriate responses."
    ),
    ("user", "Question: {question}")
])

# Streamlit App
st.title("Sreenivasa sai with LangChain")

input_text = st.text_input(
    "What question do you have in your mind?"
)

# Initialize Groq Model
llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    temperature=0.2,
)

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)