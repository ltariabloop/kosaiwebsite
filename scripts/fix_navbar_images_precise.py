#!/usr/bin/env python3
"""
Precisely update navbar images by matching menu item text
"""

import os
import re
from pathlib import Path

base_dir = Path("kosai-official-website")

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

def update_file(file_path):
    """Update navbar images in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        path_prefix = get_path_prefix(file_path)
        
        # About Us - match by "About Us" text and link
        about_us_pattern = r'(<a href="[^"]*about-us[^"]*"[^>]*>About Us</a>\s*<a href="[^"]*about-us[^"]*" class="link-without-arrow">\s*<img[^>]*src=")[^"]*("[^>]*alt="About Us")'
        content = re.sub(
            about_us_pattern,
            rf'\1{path_prefix}images/photos/aboutus_nav.jpg\2',
            content,
            flags=re.IGNORECASE
        )
        
        # Asset & Facility Management - match by "Asset & Facility Management" text
        asset_pattern = r'(<a href="[^"]*asset-facility[^"]*"[^>]*>Asset &amp; Facility Management</a>\s*<a href="[^"]*asset-facility[^"]*" class="link-without-arrow">\s*<img[^>]*src=")[^"]*("[^>]*alt="Asset &amp; Facility Management")'
        content = re.sub(
            asset_pattern,
            rf'\1{path_prefix}images/photos/asset_nav.jpg\2',
            content,
            flags=re.IGNORECASE
        )
        
        # Corporate Advisory & Services - match by "Corporate Advisory" text
        corporate_pattern = r'(<a href="[^"]*corporate-advisory[^"]*"[^>]*>Corporate Advisory[^<]*</a>\s*<a href="[^"]*corporate-advisory[^"]*" class="link-without-arrow">\s*<img[^>]*src=")[^"]*("[^>]*alt="Corporate Advisory[^"]*")'
        content = re.sub(
            corporate_pattern,
            rf'\1{path_prefix}images/photos/corporate_nav.jpg\2',
            content,
            flags=re.IGNORECASE
        )
        
        # Past Projects & Experience - match by "Past Projects" text
        past_projects_pattern = r'(<a href="[^"]*past-projects[^"]*"[^>]*>Past Projects[^<]*</a>\s*<a href="[^"]*past-projects[^"]*" class="link-without-arrow">\s*<img[^>]*src=")[^"]*("[^>]*alt="Past Projects[^"]*")'
        content = re.sub(
            past_projects_pattern,
            rf'\1{path_prefix}images/photos/pastproject_nav.jpg\2',
            content,
            flags=re.IGNORECASE
        )
        
        # Contact Us & Careers - match by "Contact Us" or "Careers" text
        contact_pattern = r'(<a href="[^"]*contact[^"]*"[^>]*>Contact Us[^<]*Careers</a>\s*<a href="[^"]*contact[^"]*" class="link-without-arrow">\s*<img[^>]*src=")[^"]*("[^>]*alt="Contact Us[^"]*Careers")'
        content = re.sub(
            contact_pattern,
            rf'\1{path_prefix}images/contact_nav.jpg\2',
            content,
            flags=re.IGNORECASE
        )
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    html_files = list(base_dir.rglob("*.html"))
    updated_count = 0
    
    for html_file in html_files:
        if update_file(html_file):
            print(f"Updated: {html_file}")
            updated_count += 1
    
    print(f"\n✅ Updated {updated_count} files")

if __name__ == "__main__":
    main()

