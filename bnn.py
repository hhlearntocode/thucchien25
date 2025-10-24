from openai import OpenAI
import base64
import os
import json
from datetime import datetime
from config import API_KEY
from utils import append_log
from prompts import IMG_NANOBANANA_PROMPT, REF_IMG_URL

client = OpenAI(api_key=API_KEY, base_url="https://api.thucchien.ai")

if REF_IMG_URL:
    with open(REF_IMG_URL, "rb") as img_file:
        img_data = img_file.read()
    encoded_img = base64.b64encode(img_data).decode("utf-8")
    IMG_NANOBANANA_PROMPT = (
        f"Reference image: data:image/jpeg;base64,{encoded_img}\n"
        + IMG_NANOBANANA_PROMPT
    )
else:
    print("No reference image found, proceeding without it.")

response = client.chat.completions.create(
    model="gemini-2.5-flash-image-preview",
    messages=[{"role": "user", "content": IMG_NANOBANANA_PROMPT.strip()}],
    modalities=["image"],
)

base64_string = response.choices[0].message.images[0].get("image_url").get("url")
if "," in base64_string:
    header, encoded = base64_string.split(",", 1)
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
log_data = {
    "timestamp": timestamp,
    "type": "image_generation_gemini",
    "request": {
        "model": "gemini-2.5-flash-image-preview",
        "prompt": IMG_NANOBANANA_PROMPT.strip(),
        "modalities": ["image"],
    },
    "response": {
        "choices": len(response.choices),
        "has_images": len(response.choices[0].message.images) > 0,
    },
    "saved_file": filename,
}
append_log(log_data)
