from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

chat_groq = ChatGroq(model="llama-3.1-8b-instant", groq_api_key=groq_api_key)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Translate the following English text to French:"),
    ("user", "{text}")
])

parser=StrOutputParser()

#create chain
chain = prompt | chat_groq | parser

#create app
app = FastAPI()
#add routes
add_routes(app, chain,path="/chain")
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)