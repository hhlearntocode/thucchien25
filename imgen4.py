import requests
import json
import base64
import os
from datetime import datetime
from config import API_KEY, API_URL
from prompts import IMG_PROMPT

url = f"{API_URL}/images/generations"
headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {API_KEY}"
}
data = {
  "model": "imagen-4",
  "prompt": IMG_PROMPT.strip(),
  "n": "1",
  "aspect_ratio": "16:9",
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    result = response.json()
    b64_data = result['data'][0]['b64_json']
    image_data = base64.b64decode(b64_data)
    
    os.makedirs("images", exist_ok=True)
    now = datetime.now()
    timestamp = now.strftime("%H:%M:%S")
    filename = f"images/img_{timestamp}.png"
    
    with open(filename, "wb") as f:
        f.write(image_data)
    print(f"Image saved to {filename}")
    
    # Log to file
    os.makedirs("logs", exist_ok=True)
    log_data = {
        "timestamp": timestamp,
        "type": "image_generation",
        "request": data,
        "response": result,
        "saved_file": filename
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
        "type": "image_generation_error",
        "request": data,
        "error": {
            "status_code": response.status_code,
            "text": response.text
        }
    }
    with open("logs/log.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(log_data, indent=4, ensure_ascii=False))

