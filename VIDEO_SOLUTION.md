# Video File Size Issue - Solutions

## Problem
The `balivideo.mp4` file is 189.50 MB, which exceeds GitHub's 100 MB file size limit.

## ✅ What I've Done
- Removed video from git tracking (file still exists locally)
- Added `*.mp4` to `.gitignore`
- Video will work locally but won't be pushed to GitHub

## Solutions

### Option 1: Git LFS (Git Large File Storage) ⭐ Recommended for GitHub

**Install Git LFS:**
```bash
# Install (if not already installed)
brew install git-lfs

# Initialize in your repo
cd "/Users/leonaureliustaira/KOSAI WEBSITE"
git lfs install

# Track video files
git lfs track "*.mp4"
git add .gitattributes
git commit -m "Add Git LFS tracking for video files"
git add kosai-official-website/balivideo.mp4
git commit -m "Add video file with Git LFS"
git push -u origin main
```

**Pros:**
- ✅ Works with GitHub
- ✅ Keeps video in repository
- ✅ Automatic handling

**Cons:**
- ⚠️ Requires Git LFS installation
- ⚠️ Uses GitHub LFS bandwidth (1GB free/month)

---

### Option 2: Host Video Externally ⭐ Best for Web Performance

**Upload to:**
- **YouTube** (unlisted) - Free, unlimited
- **Vimeo** - Free with limits
- **Cloudinary** - Free tier available
- **AWS S3** - Pay per use

**Then update HTML:**
```html
<!-- Replace balivideo.mp4 with hosted URL -->
<video autoplay loop muted playsinline>
  <source src="https://your-hosted-video-url.mp4" type="video/mp4" />
</video>
```

**Pros:**
- ✅ No size limits
- ✅ Better performance (CDN)
- ✅ No git issues
- ✅ Faster page loads

**Cons:**
- ⚠️ Requires external hosting
- ⚠️ Need to update HTML with new URL

---

### Option 3: Compress Video

**Using ffmpeg:**
```bash
# Install ffmpeg: brew install ffmpeg
ffmpeg -i kosai-official-website/balivideo.mp4 \
  -vcodec libx264 -crf 28 \
  -preset slow \
  -acodec aac -b:a 128k \
  kosai-official-website/balivideo-compressed.mp4
```

**Using HandBrake (GUI):**
1. Download HandBrake
2. Open `balivideo.mp4`
3. Use "Fast 1080p30" preset
4. Adjust quality to get under 100MB
5. Export as `balivideo-compressed.mp4`

**Pros:**
- ✅ Keeps video local
- ✅ No external dependencies
- ✅ Can push to GitHub

**Cons:**
- ⚠️ May reduce video quality
- ⚠️ Takes time to compress

---

### Option 4: Replace with Image

Replace the video hero banner with a static image.

**Pros:**
- ✅ No size issues
- ✅ Faster loading
- ✅ Simple solution

**Cons:**
- ⚠️ Loses video animation
- ⚠️ Less dynamic

---

## My Recommendation

**For GitHub Pages:** Use **Option 2 (External Hosting)** or **Option 1 (Git LFS)**

**Quick Fix:** Use **Option 3 (Compress)** to get under 100MB

Which option would you like to use? I can help implement it!

