# AI Thực Chiến API Automation

## Setup
```bash
pip install -r requirements.txt
```

Chỉnh sửa `config.py` và thêm API key của bạn.

## Sử dụng

### Individual Scripts

```bash
# Text generation
python text.py

# Image generation (Imagen-4)
python imgen4.py

# Image generation (Gemini)
python bnn.py

# Video generation (Veo 3)
python veo3.py

# Speech generation
python speech.py
```

### Check Models & API Info

```bash
# List tất cả models
python models.py

# Check model cụ thể
python models.py gpt-4o-mini

# Check API key info
python checkusage.py
```

## Prompt Management

Tất cả prompts được quản lý tập trung trong `prompts.py`:

```python
# prompts.py
TEXT_PROMPT = """
    Hãy viết một câu giới thiệu về Việt Nam.
"""

IMG_PROMPT = """
    a digital render of a massive skyscraper, modern, grand, epic with a beautiful sunset in the background
"""

VIDEO_PROMPT = """
    A cinematic shot of a baby raccoon wearing a tiny cowboy hat, riding a miniature pony through a field of daisies at sunset.
"""

SPEECH_PROMPT = """
    Xin chào, đây là một thử nghiệm chuyển văn bản thành giọng nói qua AI Thực Chiến gateway.
"""
```

**Chỉnh sửa prompts:** Mở `prompts.py` và thay đổi nội dung các biến.

## Output Files

- **Images:** `images/img_HH:MM:SS.png`
- **Videos:** `videos/video_HH:MM:SS.mp4`
- **Audio:** `audio/speech_HH:MM:SS.mp3`
- **Logs:** `logs/log.json` (lưu tất cả logs)

## Logging

Tất cả requests và responses được log vào `logs/log.json` dưới dạng mảng. Mỗi log entry sẽ được thêm vào, không ghi đè.

Format của mỗi log entry:

```json
[
    {
        "timestamp": "14:30:25",
        "type": "text_generation",
        "request": {...},
        "response": {...},
        "saved_file": "images/img_14:30:25.png"
    },
    {
        "timestamp": "14:32:10",
        "type": "image_generation",
        "request": {...},
        "response": {...},
        "saved_file": "images/img_14:32:10.png"
    }
]
```

## File Structure

```
thucchien/
├── config.py          # API key và URL
├── prompts.py         # Tất cả prompts
├── utils.py           # Helper functions (logging)
├── text.py            # Text generation
├── imgen4.py          # Image generation (Imagen)
├── bnn.py             # Image generation (Gemini)
├── veo3.py            # Video generation
├── speech.py          # Speech generation
├── models.py          # Check available models
├── checkusage.py      # Check API key info
├── images/            # Generated images
├── videos/            # Generated videos
├── audio/             # Generated audio
└── logs/              # Log files
```
