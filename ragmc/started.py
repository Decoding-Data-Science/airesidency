from dotenv import load_dotenv
import os
import openai
# Load environment variables
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# Load data
documents = SimpleDirectoryReader("data").load_data()

# Create an Index
# Chunk data and convert it into vector embeddings

index = VectorStoreIndex.from_documents (documents)

# Create a QueryEngine for Retrieval & Augmentation
query_engine = index.as_query_engine()

# Generate response by asking a query to the QueryEngine
response = query_engine.query("What is the first program author tried?")

print(response)


