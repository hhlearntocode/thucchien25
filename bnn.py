from openai import OpenAI
import base64
import os
import json
from datetime import datetime
from config import API_KEY
from prompts import IMG_NANOBANANA_PROMPT

client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.thucchien.ai"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash-image-preview",
    messages=[{"role": "user", "content": IMG_NANOBANANA_PROMPT.strip()}],
    modalities=["image"]
)

base64_string = response.choices[0].message.images[0].get("image_url").get("url")
if ',' in base64_string:
    header, encoded = base64_string.split(',', 1)
else:
    encoded = base64_string
image_data = base64.b64decode(encoded)

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
    "type": "image_generation_gemini",
    "request": {
        "model": "gemini-2.5-flash-image-preview",
        "prompt": IMG_NANOBANANA_PROMPT.strip(),
        "modalities": ["image"]
    },
    "response": {
        "choices": len(response.choices),
        "has_images": len(response.choices[0].message.images) > 0
    },
    "saved_file": filename
}
with open("logs/log.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(log_data, indent=4, ensure_ascii=False))

