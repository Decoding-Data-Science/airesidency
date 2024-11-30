#pip install requests
#pip install groq
#pip install python-dotenv
#pip install gradio
# use 3.11 python

import os
import requests
import gradio as gr
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the Groq API key from environment variables
groq_api_key = os.environ.get("GROQ_API_KEY")

# Check if the Groq API key is set
if groq_api_key is None:
    raise ValueError("Groq API key is not set in environment variables.")

# Define the URL for the Groq API endpoint
url = "https://api.groq.com/openai/v1/chat/completions"

# Function to interact with the Groq API
def groq_chat(prompt):
    headers = {
        "Authorization": f"Bearer {groq_api_key}"
    }
    body = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    
    # Send a POST request to the Groq API
    response = requests.post(url, headers=headers, json=body)
    
    if response.status_code == 200:
        # Extract and return the content of the first message choice
        return response.json().get('choices', [{}])[0].get('message', {}).get('content', "No response found.")
    else:
        # Return the error details
        return f"Error {response.status_code}: {response.text}"

# Define the Gradio interface
with gr.Blocks() as interface:
    gr.Markdown("# DDS 1st Chatbot")
    with gr.Row():
        user_input = gr.Textbox(label="Enter your prompt", placeholder="Type something funny or interesting...")
    with gr.Row():
        output = gr.Textbox(label="Response from Groq API")
    with gr.Row():
        submit_button = gr.Button("Get Response")
    
    submit_button.click(fn=groq_chat, inputs=user_input, outputs=output)

# Launch the interface
if __name__ == "__main__":
    interface.launch(share=True)
