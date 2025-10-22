#!/bin/bash

# Veo 3 Video Generation Script
# Usage: ./veo3.sh
API_KEY="your-api-key-here"
PROMPT="A cinematic shot of a baby raccoon wearing a tiny cowboy hat, riding a miniature pony through a field of daisies at sunset."
IMAGE_PATH="/Users/leonard/thucchien/images/img_00:37:00.png"

echo "🎬 Starting Veo 3 Video Generation..."
echo "Prompt: $PROMPT"
echo ""

# Bước 1: Tạo video
echo "📝 Step 1: Creating video..."

# Create JSON file with proper image format
if [ -f "$IMAGE_PATH" ]; then
    echo "🖼️ Using image: $IMAGE_PATH"
    IMAGE_BASE64=$(base64 -i "$IMAGE_PATH" | tr -d '\n')
    # Google AI API expects data:image/jpeg;base64, prefix
    IMAGE_DATA="data:image/png;base64,$IMAGE_BASE64"
    
    cat > /tmp/veo3_request.json << EOF
{
  "instances": [{
    "prompt": "$PROMPT",
    "image": {
      "bytesBase64Encoded": "$IMAGE_BASE64",
      "mimeType": "image/png"
    }
  }],
  "parameters": {
    "negativePrompt": "blurry, low quality",
    "aspectRatio": "16:9",
    "resolution": "1080p",
    "personGeneration": "allow_adult"
  }
}
EOF
else
    echo "⚠️ Image not found, trying without image"
    cat > /tmp/veo3_request.json << EOF
{
  "instances": [{
    "prompt": "$PROMPT"
  }],
  "parameters": {
    "negativePrompt": "blurry, low quality",
    "aspectRatio": "16:9",
    "resolution": "1080p",
    "personGeneration": "allow_adult"
  }
}
EOF
fi

RESPONSE=$(curl -s -X POST "https://api.thucchien.ai/gemini/v1beta/models/veo-3.0-generate-001:predictLongRunning" \
-H "Content-Type: application/json" \
-H "x-goog-api-key: $API_KEY" \
-d @/tmp/veo3_request.json)

echo "Response: $RESPONSE"

# Extract operation ID
OPERATION_ID=$(echo $RESPONSE | grep -o 'operations/[^"]*' | cut -d'/' -f2)
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

# Clean up
rm -f /tmp/veo3_request.json
