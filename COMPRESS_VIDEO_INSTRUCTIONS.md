# Compress Video for GitHub Pages

## Quick Method (Recommended)

### Step 1: Install ffmpeg
```bash
brew install ffmpeg
```

### Step 2: Run the compression script
```bash
cd "/Users/leonaureliustaira/KOSAI WEBSITE"
./compress_video.sh
```

The script will:
- Compress `balivideo.mp4` to under 100MB
- Replace the original with the compressed version
- Make it ready for GitHub

---

## Manual Method

If the script doesn't work, compress manually:

```bash
cd "/Users/leonaureliustaira/KOSAI WEBSITE/kosai-official-website"

# Compress video (target ~80MB to be safe)
ffmpeg -i balivideo.mp4 \
  -vcodec libx264 \
  -crf 30 \
  -preset slow \
  -vf "scale=1920:-2" \
  -r 30 \
  -acodec aac \
  -b:a 96k \
  -movflags +faststart \
  balivideo-compressed.mp4

# Check size
ls -lh balivideo-compressed.mp4

# If under 100MB, replace original
mv balivideo-compressed.mp4 balivideo.mp4
```

---

## After Compression

1. **Check file size:**
   ```bash
   ls -lh kosai-official-website/balivideo.mp4
   ```
   Should be under 100MB

2. **Update .gitignore** (remove mp4 exclusion temporarily):
   ```bash
   # Edit .gitignore to allow balivideo.mp4
   ```

3. **Add and commit:**
   ```bash
   git add kosai-official-website/balivideo.mp4
   git commit -m "Add compressed video for GitHub Pages"
   git push -u origin main
   ```

---

## Compression Settings Explained

- `-crf 30`: Quality (lower = better quality, higher = smaller file)
- `-preset slow`: Better compression (slower but smaller)
- `-vf "scale=1920:-2"`: Max width 1920px (maintains aspect ratio)
- `-r 30`: Frame rate (30fps)
- `-b:a 96k`: Audio bitrate (96kbps)

If still too large, try:
- `-crf 32` (lower quality)
- `-vf "scale=1280:-2"` (smaller resolution)
- `-r 24` (lower frame rate)

---

## Alternative: Use HandBrake (GUI)

1. Download HandBrake: https://handbrake.fr
2. Open `balivideo.mp4`
3. Preset: "Fast 1080p30"
4. Adjust Quality slider to target ~80MB
5. Export as `balivideo-compressed.mp4`
6. Replace original

