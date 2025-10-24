import requests
import json
import os
from datetime import datetime
from config import API_KEY, API_URL
from prompts import TEXT_PROMPT
from utils import append_log

url = f"{API_URL}/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}
data = {
    "model": "gemini-2.5-flash",
    "messages": [
        {
            "role": "system",
            "content": "Bạn là một trợ lý ảo"
        },
        {
            "role": "user",
            "content": TEXT_PROMPT.strip()
        }
    ]
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    result = response.json()
    print(result['choices'][0]['message']['content'])
    
    # Log to file
    timestamp = datetime.now().strftime("%H:%M:%S")
    log_data = {
        "timestamp": timestamp,
        "type": "text_generation",
        "request": data,
        "response": result
    }
    append_log(log_data)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
    
    # Log error
    timestamp = datetime.now().strftime("%H:%M:%S")
    log_data = {
        "timestamp": timestamp,
        "type": "text_generation_error",
        "request": data,
        "error": {
            "status_code": response.status_code,
            "text": response.text
        }
    }
    append_log(log_data)

