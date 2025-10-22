from openai import OpenAI
from pathlib import Path
import os
import json
from datetime import datetime
from config import API_KEY
from prompts import SPEECH_PROMPT

client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.thucchien.ai"
)

os.makedirs("audio", exist_ok=True)
now = datetime.now()
timestamp = now.strftime("%H:%M:%S")
speech_file_path = Path("audio") / f"speech_{timestamp}.mp3"

response = client.audio.speech.create(
    model="gemini-2.5-flash-preview-tts",
    voice="Zephyr",
    input=SPEECH_PROMPT.strip()
)

response.stream_to_file(speech_file_path)
print(f"File âm thanh đã được lưu tại: {speech_file_path}")

# Log to file
os.makedirs("logs", exist_ok=True)
log_data = {
    "timestamp": timestamp,
    "type": "speech_generation",
    "request": {
        "model": "gemini-2.5-flash-preview-tts",
        "voice": "Zephyr",
        "input": SPEECH_PROMPT.strip()
    },
    "response": {
        "content_length": len(response.content) if hasattr(response, 'content') else 'unknown'
    },
    "saved_file": str(speech_file_path)
}
with open("logs/log.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(log_data, indent=4, ensure_ascii=False))

