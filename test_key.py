import os
from dotenv import load_dotenv
import requests

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

headers = {
    "Authorization":f"Bearer {api_key}",
    "Content-Type":"application/json"
}

payload= {
    "model": "openai/gpt-oss-20b",
    "messages": [{"role":"user", "content": "Say hello in one short sentence."}]
}

response= requests.post(
    "https://api.groq.com/openai/v1/chat/completions",
    headers=headers,
    json=payload
)
print("Status Code:", response.status_code)
print(response.json())