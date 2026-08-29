import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()

api_key = os.environ.get("OPENAI_API_KEY", "").replace('"', '')
base_url = os.environ.get("OPENAI_BASE_URL", "").replace('"', '')
model = os.environ.get("MODEL_CLASSIFIER", "qwen/qwen3-32b").replace('"', '')

print(f"Base URL: {repr(base_url)}")
print(f"API Key: {repr(api_key)}")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

payload = {
    "model": model,
    "messages": [{"role": "user", "content": "Hello"}],
    "max_tokens": 10
}

url = f"{base_url}/chat/completions"

print(f"Sending request to: {url}")
response = requests.post(url, headers=headers, json=payload)
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.text}")

