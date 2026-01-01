# Deployment Guide

## Option 1: GitHub Pages (Free & Easy)

1. **Create a GitHub repository:**
   ```bash
   # On GitHub, create a new repository called "kosai-website" (or any name)
   ```

2. **Push your code to GitHub:**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/kosai-website.git
   git branch -M main
   git push -u origin main
   ```

3. **Enable GitHub Pages:**
   - Go to your repository on GitHub
   - Click "Settings" → "Pages"
   - Under "Source", select "main" branch and "/ (root)" folder
   - Click "Save"
   - Your site will be available at: `https://YOUR_USERNAME.github.io/kosai-website/`

4. **Update for GitHub Pages:**
   - The website files are in `kosai-official-website/`
   - You may need to move them to root or configure GitHub Pages to use that folder
   - Or create a `gh-pages` branch with the website files

## Option 2: Netlify (Recommended - Free & Fast)

1. **Install Netlify CLI (optional):**
   ```bash
   npm install -g netlify-cli
   ```

2. **Deploy via Netlify:**
   - Go to [netlify.com](https://www.netlify.com)
   - Sign up/login
   - Click "Add new site" → "Import an existing project"
   - Connect your GitHub repository
   - Set "Publish directory" to `kosai-official-website`
   - Click "Deploy site"
   - Your site will get a URL like: `https://random-name-123.netlify.app`

3. **Or drag & drop:**
   - Go to [app.netlify.com/drop](https://app.netlify.com/drop)
   - Drag the `kosai-official-website` folder
   - Your site will be live instantly!

## Option 3: Vercel (Free & Fast)

1. **Install Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

2. **Deploy:**
   ```bash
   cd kosai-official-website
   vercel
   ```

## Quick Setup Script

Run this to prepare for GitHub Pages:

```bash
# Create a gh-pages branch with website files
git checkout -b gh-pages
git rm -rf --cached .
git add kosai-official-website/
git mv kosai-official-website/* .
git commit -m "Setup GitHub Pages"
git push origin gh-pages
```

Then enable GitHub Pages to use the `gh-pages` branch.

