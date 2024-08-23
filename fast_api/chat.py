from typing import Union
from fastapi import FastAPI

app = FastAPI()


from huggingface_hub import InferenceClient

@app.get("/chat")
async def chat(prompt: Union[str, None] = None, max_tokens: Union[int, None] = None): 
    client = InferenceClient(model="gpt2", token="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")
   

    input_text = prompt or "Once upon a time"
  

    # Call the text generation API
    response = client.text_generation(
        input_text, max_new_tokens=int(max_tokens or 100)
    )
    
    # Print the generated text
    print(response)

    return {"message": response}
