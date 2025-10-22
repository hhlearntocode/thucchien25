# AI Thực Chiến API Automation

## Setup
```bash
pip install -r requirements.txt
```

Chỉnh sửa `config.py` và thêm API key của bạn.

## Sử dụng

### CLI (Command Line)

```bash
python main.py text "viết bài thơ về mùa thu"

python main.py chat-img "a breathtaking waterfall scene" gemini-2.5-flash-image-preview

python main.py img "a beautiful sunset" imagen-4 aspect_ratio=16:9

python main.py video "a bird flying" veo-3

python main.py tts "Xin chào" tts-1 voice=alloy
```

**Lưu ý:** 
- Ảnh sẽ tự động lưu vào thư mục `images/` với tên `img_YYYYMMDD_HHMMSS.png`
- Audio sẽ tự động lưu vào thư mục `audio/` với tên `tts_YYYYMMDD_HHMMSS.mp3`

### Python Code

```python
from main import gen, save_image

result = gen("text", "viết bài thơ về mùa thu")

result = gen("chat-img", "a breathtaking waterfall scene", model="gemini-2.5-flash-image-preview")
if "choices" in result:
    images = result["choices"][0]["message"].get("images", [])
    for img in images:
        url = img.get("image_url", {}).get("url")
        filename = save_image(url)
        print(f"Image saved: {filename}")

result = gen("img", "a beautiful sunset", aspect_ratio="16:9")
if "data" in result and "b64_json" in result["data"][0]:
    filename = save_image(result["data"][0]["b64_json"])
    print(f"Image saved: {filename}")

result = gen("video", "a bird flying in the sky")

audio = gen("tts", "Xin chào, đây là test text to speech")
```

### Tham số job:
- `"text"` - Text generation
- `"chat-img"` - Image generation via chat completions (Gemini models)
- `"img"` - Image generation via images endpoint (Imagen models)
- `"video"` - Video generation
- `"tts"` - Text-to-speech

### Tham số tùy chọn:
- `model` - Tên model cụ thể
- `**kwargs` - Các tham số bổ sung (size, voice, temperature, etc.)

## Check Models

```bash
# List tất cả models
python models.py

# Check model cụ thể
python models.py gpt-4o-mini
```

## API GET Requests

```bash
# List models
python get_api.py v1/models

# Get model info
python get_api.py v1/models/gpt-4

# Get usage
python get_api.py v1/usage

# Get balance
python get_api.py v1/balance

# Get key info
python get_api.py key/info

# Custom endpoint với params
python get_api.py v1/custom_endpoint key=value
```
