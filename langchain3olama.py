
import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser

import streamlit as st




prompt=ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. please answer the question as best as you can."),
        ("user", "Question:{question}"),
    ]
)


#stremlit app
st.title("Langchain Ollama Example")
question=st.text_input("Enter your question here:")


#ollama llm
llm=Ollama(model="gemma:2b", temperature=0.9)
output_parser=StrOutputParser()
chain=prompt | llm | output_parser

if question:
    with st.spinner("Generating response..."):
        response=chain.invoke({"question":question})
    st.write("Response:")
    st.write(response)