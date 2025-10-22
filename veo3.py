import requests
import json
import time
import os
from datetime import datetime
import base64
from config import API_KEY, API_URL
image_path = "/Users/leonard/thucchien/images/img_00:37:00.png"
if image_path and os.path.exists(image_path):
    with open(image_path, "rb") as f:
       image_data = base64.b64encode(f.read()).decode('utf-8')
       print("success encode image")
else:
    print("error encode image")
    
def create_video(prompt, aspect_ratio="16:9", resolution="1080p"):
    url = f"{API_URL}/gemini/v1beta/models/veo-3.0-generate-001:predictLongRunning"
    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": API_KEY
    }
    data = {
        "instances": [{
            "prompt": prompt,
            "image": image_data
        }],
        "parameters": {
            "negativePrompt": "blurry, low quality",
            "aspectRatio": aspect_ratio,
            "resolution": resolution,
            "personGeneration": "allow_all"
        }
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        result = response.json()
        operation_name = result.get("name", "")
        operation_id = operation_name.split("/")[-1] if operation_name else None
        print(f"Video generation started. Operation ID: {operation_id}")
        
        # Log to file
        os.makedirs("logs", exist_ok=True)
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_data = {
            "timestamp": timestamp,
            "type": "video_generation_start",
            "request": data,
            "response": result,
            "operation_id": operation_id
        }
        with open("logs/log.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(log_data, indent=4, ensure_ascii=False))
        
        return operation_id
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        
        # Log error
        os.makedirs("logs", exist_ok=True)
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_data = {
            "timestamp": timestamp,
            "type": "video_generation_error",
            "request": data,
            "error": {
                "status_code": response.status_code,
                "text": response.text
            }
        }
        with open("logs/log.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(log_data, indent=4, ensure_ascii=False))
        
        return None

def check_status(operation_id):
    url = f"{API_URL}/gemini/v1beta/models/veo-3.0-generate-001/operations/{operation_id}"
    headers = {"x-goog-api-key": API_KEY}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

def download_video(file_id, output_dir="videos"):
    os.makedirs(output_dir, exist_ok=True)
    
    url = f"{API_URL}/gemini/download/v1beta/files/{file_id}:download?alt=media"
    headers = {"x-goog-api-key": API_KEY}
    
    response = requests.get(url, headers=headers, stream=True)
    
    if response.status_code == 200:
        now = datetime.now()
        timestamp = now.strftime("%H:%M:%S")
        filename = f"{output_dir}/video_{timestamp}.mp4"
        
        with open(filename, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f"Video saved to {filename}")
        
        # Log completion
        os.makedirs("logs", exist_ok=True)
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_data = {
            "timestamp": timestamp,
            "type": "video_generation_complete",
            "saved_file": filename,
            "file_id": file_id
        }
        with open("logs/log.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(log_data, indent=4, ensure_ascii=False))
        
        return filename
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

def generate_and_wait(prompt, check_interval=10, aspect_ratio="16:9", resolution="1080p"):
    operation_id = create_video(prompt, aspect_ratio, resolution)
    
    if not operation_id:
        return None
    
    print("Waiting for video generation to complete...")
    
    while True:
        status = check_status(operation_id)
        
        if not status:
            return None
        
        if status.get("done"):
            print("Video generation completed!")
            
            if "response" in status:
                predictions = status.get("response", {}).get("predictions", [])
                if predictions and "generatedSamples" in predictions[0]:
                    samples = predictions[0]["generatedSamples"]
                    if samples:
                        video_uri = samples[0].get("video", {}).get("uri", "")
                        if video_uri:
                            file_id = video_uri.split("/")[-1]
                            return download_video(file_id)
            
            print("No video found in response")
            print(json.dumps(status, indent=2, ensure_ascii=False))
            return None
        
        print(f"Status: {status.get('metadata', {}).get('progressPercentage', 0)}% - Checking again in {check_interval}s...")
        time.sleep(check_interval)

if __name__ == "__main__":
    from prompts import VIDEO_PROMPT
    generate_and_wait(VIDEO_PROMPT.strip())

