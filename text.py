import requests
import json
import os
from datetime import datetime
from config import API_KEY, API_URL
from prompts import TEXT_PROMPT

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
    os.makedirs("logs", exist_ok=True)
    timestamp = datetime.now().strftime("%H:%M:%S")
    log_data = {
        "timestamp": timestamp,
        "type": "text_generation",
        "request": data,
        "response": result
    }
    with open("logs/log.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(log_data, indent=4, ensure_ascii=False))
else:
    print(f"Error: {response.status_code}")
    print(response.text)
    
    # Log error
    os.makedirs("logs", exist_ok=True)
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
    with open("logs/log.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(log_data, indent=4, ensure_ascii=False))

