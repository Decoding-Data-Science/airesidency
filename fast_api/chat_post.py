from fastapi import FastAPI
from pydantic import BaseModel
from huggingface_hub import InferenceClient

app = FastAPI()

# Hugging Face API Token and Model
TOKEN = "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"
MODEL = "gpt2"

# Request body structure
class ChatRequest(BaseModel):
    prompt: str = "Once upon a time"
    max_tokens: int = 100

@app.post("/chat1")
async def chat(request: ChatRequest):
    # Initialize the Hugging Face client
    client = InferenceClient(model=MODEL, token=TOKEN)

    # Generate text
    response = client.text_generation(
        request.prompt, max_new_tokens=request.max_tokens
    )

    # Return the response
    return {"message": response}
