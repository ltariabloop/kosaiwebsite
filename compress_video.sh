#!/bin/bash

# Video Compression Script for GitHub Pages
# This will compress balivideo.mp4 to under 100MB

echo "🎬 Compressing video for GitHub Pages..."
echo ""

cd "$(dirname "$0")/kosai-official-website"

# Check if ffmpeg is installed
if ! command -v ffmpeg &> /dev/null; then
    echo "❌ ffmpeg is not installed."
    echo ""
    echo "📦 Install ffmpeg:"
    echo "   brew install ffmpeg"
    echo ""
    echo "Then run this script again."
    exit 1
fi

# Check if source video exists
if [ ! -f "balivideo.mp4" ]; then
    echo "❌ balivideo.mp4 not found!"
    exit 1
fi

echo "📹 Source video: $(du -h balivideo.mp4 | cut -f1)"
echo ""

# Compress video with aggressive settings to get under 100MB
# Target: ~80MB to be safe
echo "⚙️  Compressing (this may take a few minutes)..."
ffmpeg -i balivideo.mp4 \
  -vcodec libx264 \
  -crf 30 \
  -preset slow \
  -vf "scale=1920:-2" \
  -r 30 \
  -acodec aac \
  -b:a 96k \
  -movflags +faststart \
  -y \
  balivideo-compressed.mp4 2>&1 | grep -E "Duration|frame|size|error" || echo "Compression in progress..."

# Check file size
if [ -f "balivideo-compressed.mp4" ]; then
    SIZE=$(du -m balivideo-compressed.mp4 | cut -f1)
    echo ""
    echo "✅ Compression complete!"
    echo "📊 Compressed size: ${SIZE}MB"
    
    if [ "$SIZE" -lt 100 ]; then
        echo "✅ File is under 100MB - safe for GitHub!"
        echo ""
        echo "🔄 Replacing original with compressed version..."
        mv balivideo-compressed.mp4 balivideo.mp4
        echo "✅ Done! Video is ready to push to GitHub."
    else
        echo "⚠️  File is still over 100MB (${SIZE}MB)"
        echo "   Trying more aggressive compression..."
        # Try even more aggressive compression
        ffmpeg -i balivideo.mp4 \
          -vcodec libx264 \
          -crf 32 \
          -preset slow \
          -vf "scale=1280:-2" \
          -r 24 \
          -acodec aac \
          -b:a 64k \
          -movflags +faststart \
          -y \
          balivideo-compressed.mp4
        
        NEW_SIZE=$(du -m balivideo-compressed.mp4 | cut -f1)
        if [ "$NEW_SIZE" -lt 100 ]; then
            mv balivideo-compressed.mp4 balivideo.mp4
            echo "✅ Successfully compressed to ${NEW_SIZE}MB!"
        else
            echo "❌ Still too large (${NEW_SIZE}MB). Consider:"
            echo "   - Using external hosting (YouTube/Vimeo)"
            echo "   - Using Git LFS"
            echo "   - Further reducing resolution/quality"
        fi
    fi
else
    echo "❌ Compression failed!"
    exit 1
fi

