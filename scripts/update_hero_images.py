#!/usr/bin/env python3
"""
Update hero images to match navbar images for each page
"""

import os
import re
from pathlib import Path

base_dir = Path("kosai-official-website")

# Mapping of page files to their corresponding hero images
page_hero_mapping = {
    "about-us.html": "images/photos/aboutus_nav.jpg",
    "asset-facility-management.html": "images/photos/asset_nav.jpg",
    "corporate-advisory-services.html": "images/photos/corporate_nav.jpg",
    "past-projects.html": "images/photos/pastproject_nav.jpg",
    "contact.html": "images/contact_nav.jpg",
    "careers.html": "images/contact_nav.jpg",  # Careers uses contact image
}

def get_path_prefix(file_path):
    """Determine the relative path prefix based on file depth"""
    parts = file_path.parts
    depth = len([p for p in parts if p != 'kosai-official-website']) - 1
    if depth == 0:
        return ""
    elif depth == 1:
        return "../"
    elif depth == 2:
        return "../../"
    else:
        return "../" * depth

def update_hero_image(file_path):
    """Update hero image in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        file_name = file_path.name
        
        # Determine which hero image to use
        hero_image = None
        
        # Check if this is one of our main pages
        if file_name in page_hero_mapping:
            hero_image = page_hero_mapping[file_name]
        # Check if it's in a subdirectory that corresponds to a main page
        elif "about-us" in str(file_path) and "our-team" not in str(file_path):
            hero_image = "images/photos/aboutus_nav.jpg"
        elif "asset-facility" in str(file_path) or "our-solutions" in str(file_path):
            hero_image = "images/photos/asset_nav.jpg"
        elif "corporate-advisory" in str(file_path):
            hero_image = "images/photos/corporate_nav.jpg"
        elif "past-projects" in str(file_path):
            hero_image = "images/photos/pastproject_nav.jpg"
        elif "contact" in str(file_path) or "careers" in str(file_path):
            hero_image = "images/contact_nav.jpg"
        
        if not hero_image:
            return False, []
        
        path_prefix = get_path_prefix(file_path)
        full_hero_path = path_prefix + hero_image if path_prefix else hero_image
        
        changes_made = []
        
        # Pattern 1: Hero banner image in wrapper-image
        # Match: <div class="wrapper-image"> ... <img ... src="..." ... />
        pattern1 = r'(<div class="wrapper-image[^"]*">\s*<div class="field[^>]*field--name-field-image[^>]*">\s*<img[^>]*src=")[^"]*("[^>]*class="img-responsive"[^>]*/>)'
        new_content = re.sub(pattern1, rf'\1{full_hero_path}\2', content, flags=re.IGNORECASE | re.DOTALL)
        if new_content != content:
            content = new_content
            changes_made.append("hero banner image")
        
        # Pattern 2: Hero banner image with opacity-part
        pattern2 = r'(<div class="wrapper-image opacity-part">\s*<div class="field[^>]*field--name-field-image[^>]*">\s*<img[^>]*src=")[^"]*("[^>]*class="img-responsive"[^>]*/>)'
        new_content = re.sub(pattern2, rf'\1{full_hero_path}\2', content, flags=re.IGNORECASE | re.DOTALL)
        if new_content != content:
            content = new_content
            if "hero banner image" not in changes_made:
                changes_made.append("hero banner image")
        
        # Pattern 3: More flexible pattern for hero images
        # Look for hero-banner-a section and update image within it
        hero_section_pattern = r'(<div class="hero-banner-a[^"]*">[^<]*<div[^>]*hero-banner-a-wrapper[^>]*>.*?<div class="wrapper-image[^"]*">.*?<div class="field[^>]*field--name-field-image[^>]*">\s*<img[^>]*src=")[^"]*("[^>]*class="img-responsive"[^>]*/>)'
        new_content = re.sub(hero_section_pattern, rf'\1{full_hero_path}\2', content, flags=re.IGNORECASE | re.DOTALL)
        if new_content != content:
            content = new_content
            if "hero banner image" not in changes_made:
                changes_made.append("hero banner image")
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, changes_made
        return False, []
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False, []

def main():
    """Main function to update all hero images"""
    html_files = list(base_dir.rglob("*.html"))
    updated_count = 0
    total_files = len(html_files)
    
    print(f"Updating hero images to match navbar images...\n")
    
    for html_file in html_files:
        updated, changes = update_hero_image(html_file)
        if updated:
            print(f"✅ Updated: {html_file}")
            if changes:
                print(f"   Changes: {', '.join(changes)}")
            updated_count += 1
    
    print(f"\n{'='*60}")
    print(f"✅ Updated {updated_count} out of {total_files} files")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()

