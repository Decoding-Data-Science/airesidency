from fastapi import FastAPI
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from pydantic import BaseModel

from dotenv import load_dotenv
import os
import openai
# Load environment variables
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/query_program")

def query_program(query: Query):
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents=documents)
    query_engine = index.as_query_engine()
    response = query_engine.query(query.question)
    return {"response": response}
