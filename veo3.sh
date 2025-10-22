#!/bin/bash
from config import API_KEY

# Veo 3 Video Generation Script
# Usage: ./veo3.sh

PROMPT="A cinematic shot of a baby raccoon wearing a tiny cowboy hat, riding a miniature pony through a field of daisies at sunset."

echo "🎬 Starting Veo 3 Video Generation..."
echo "Prompt: $PROMPT"
echo ""

# Bước 1: Tạo video
echo "📝 Step 1: Creating video..."
RESPONSE=$(curl -s -X POST "https://api.thucchien.ai/gemini/v1beta/models/veo-3.0-generate-001:predictLongRunning" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $API_KEY" \
-d "{
  \"instances\": [{
    \"prompt\": \"$PROMPT\",
    \"image\": null
  }],
  \"parameters\": {
    \"negativePrompt\": \"blurry, low quality\",
    \"aspectRatio\": \"16:9\",
    \"resolution\": \"720p\",
    \"personGeneration\": \"allow_all\"
  }
}")

echo "Response: $RESPONSE"

# Extract operation ID
OPERATION_ID=$(echo $RESPONSE | grep -o '"name":"operations/[^"]*"' | cut -d'/' -f2 | tr -d '"')
echo "Operation ID: $OPERATION_ID"

if [ -z "$OPERATION_ID" ]; then
    echo "❌ Failed to get operation ID"
    exit 1
fi

# Bước 2: Check status
echo ""
echo "⏳ Step 2: Waiting for completion..."
while true; do
    STATUS_RESPONSE=$(curl -s "https://api.thucchien.ai/gemini/v1beta/models/veo-3.0-generate-001/operations/$OPERATION_ID" \
    -H "x-goog-api-key: $API_KEY")
    
    if echo $STATUS_RESPONSE | grep -q '"done":true'; then
        echo "✅ Video generation completed!"
        break
    fi
    
    PROGRESS=$(echo $STATUS_RESPONSE | grep -o '"progressPercentage":[0-9]*' | cut -d':' -f2)
    echo "📊 Progress: $PROGRESS%"
    sleep 10
done

# Bước 3: Download video
echo ""
echo "📥 Step 3: Downloading video..."
FILE_ID=$(echo $STATUS_RESPONSE | grep -o '"uri":"[^"]*"' | cut -d'/' -f4 | tr -d '"')
echo "File ID: $FILE_ID"

if [ -z "$FILE_ID" ]; then
    echo "❌ Failed to get file ID"
    exit 1
fi

TIMESTAMP=$(date +%H:%M:%S)
curl "https://api.thucchien.ai/gemini/download/v1beta/files/$FILE_ID:download?alt=media" \
-H "x-goog-api-key: $API_KEY" \
--output "video_$TIMESTAMP.mp4"

echo "🎉 Video saved as: video_$TIMESTAMP.mp4"
