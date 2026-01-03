#!/usr/bin/env python3
"""
Verify and fix navbar images across all HTML files to ensure consistency
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

def fix_navbar_images(file_path):
    """Fix navbar images in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        path_prefix = get_path_prefix(file_path)
        changes_made = []
        
        # About Us - should be aboutus_nav.jpg
        about_us_patterns = [
            (r'(<a href="[^"]*about-us[^"]*"[^>]*>About Us</a>\s*<a href="[^"]*about-us[^"]*" class="link-without-arrow">\s*<img[^>]*src=")[^"]*("[^>]*alt="About Us")', 
             rf'\1{path_prefix}images/photos/aboutus_nav.jpg\2'),
            (r'(<img[^>]*alt="About Us"[^>]*src=")[^"]*("[^>]*>)', 
             rf'\1{path_prefix}images/photos/aboutus_nav.jpg\2'),
        ]
        
        for pattern, replacement in about_us_patterns:
            new_content = re.sub(pattern, replacement, content, flags=re.IGNORECASE | re.DOTALL)
            if new_content != content:
                content = new_content
                changes_made.append("About Us")
                break
        
        # Asset & Facility Management - should be asset_nav.jpg
        asset_patterns = [
            (r'(<a href="[^"]*asset-facility[^"]*"[^>]*>Asset &amp; Facility Management</a>\s*<a href="[^"]*asset-facility[^"]*" class="link-without-arrow">\s*<img[^>]*src=")[^"]*("[^>]*alt="Asset &amp; Facility Management")', 
             rf'\1{path_prefix}images/photos/asset_nav.jpg\2'),
            (r'(<img[^>]*alt="Asset &amp; Facility Management"[^>]*src=")[^"]*("[^>]*>)', 
             rf'\1{path_prefix}images/photos/asset_nav.jpg\2'),
        ]
        
        for pattern, replacement in asset_patterns:
            new_content = re.sub(pattern, replacement, content, flags=re.IGNORECASE | re.DOTALL)
            if new_content != content:
                content = new_content
                changes_made.append("Asset & Facility Management")
                break
        
        # Corporate Advisory & Services - should be corporate_nav.jpg
        corporate_patterns = [
            (r'(<a href="[^"]*corporate-advisory[^"]*"[^>]*>Corporate Advisory[^<]*</a>\s*<a href="[^"]*corporate-advisory[^"]*" class="link-without-arrow">\s*<img[^>]*src=")[^"]*("[^>]*alt="Corporate Advisory[^"]*")', 
             rf'\1{path_prefix}images/photos/corporate_nav.jpg\2'),
            (r'(<img[^>]*alt="Corporate Advisory[^"]*"[^>]*src=")[^"]*("[^>]*>)', 
             rf'\1{path_prefix}images/photos/corporate_nav.jpg\2'),
        ]
        
        for pattern, replacement in corporate_patterns:
            new_content = re.sub(pattern, replacement, content, flags=re.IGNORECASE | re.DOTALL)
            if new_content != content:
                content = new_content
                changes_made.append("Corporate Advisory & Services")
                break
        
        # Past Projects & Experience - should be pastproject_nav.jpg
        past_projects_patterns = [
            (r'(<a href="[^"]*past-projects[^"]*"[^>]*>Past Projects[^<]*</a>\s*<a href="[^"]*past-projects[^"]*" class="link-without-arrow">\s*<img[^>]*src=")[^"]*("[^>]*alt="Past Projects[^"]*")', 
             rf'\1{path_prefix}images/photos/pastproject_nav.jpg\2'),
            (r'(<img[^>]*alt="Past Projects[^"]*"[^>]*src=")[^"]*("[^>]*>)', 
             rf'\1{path_prefix}images/photos/pastproject_nav.jpg\2'),
        ]
        
        for pattern, replacement in past_projects_patterns:
            new_content = re.sub(pattern, replacement, content, flags=re.IGNORECASE | re.DOTALL)
            if new_content != content:
                content = new_content
                changes_made.append("Past Projects & Experience")
                break
        
        # Contact Us & Careers - should be contact_nav.jpg (note: in images/ not images/photos/)
        contact_patterns = [
            (r'(<a href="[^"]*contact[^"]*"[^>]*>Contact Us[^<]*Careers</a>\s*<a href="[^"]*contact[^"]*" class="link-without-arrow">\s*<img[^>]*src=")[^"]*("[^>]*alt="Contact Us[^"]*Careers")', 
             rf'\1{path_prefix}images/contact_nav.jpg\2'),
            (r'(<img[^>]*alt="Contact Us[^"]*Careers"[^>]*src=")[^"]*("[^>]*>)', 
             rf'\1{path_prefix}images/contact_nav.jpg\2'),
        ]
        
        for pattern, replacement in contact_patterns:
            new_content = re.sub(pattern, replacement, content, flags=re.IGNORECASE | re.DOTALL)
            if new_content != content:
                content = new_content
                changes_made.append("Contact Us & Careers")
                break
        
        # Also fix any old paths that might still exist
        old_paths = [
            (r'src="([^"]*sites/btg/files/styles/hero_banner/public/2023-12/New%20About%20Us%20Banner[^"]*)"', 
             rf'src="{path_prefix}images/photos/aboutus_nav.jpg"'),
            (r'src="([^"]*sites/btg/files/2023-12/Hotels%20menu%20card[^"]*)"', 
             rf'src="{path_prefix}images/photos/asset_nav.jpg"'),
            (r'src="([^"]*sites/btg/files/2022-08/mission\.png)"', 
             rf'src="{path_prefix}images/contact_nav.jpg"'),
        ]
        
        for pattern, replacement in old_paths:
            # Only replace if it's in a menu-item-image context
            if 'menu-item-image' in content or 'link-without-arrow' in content:
                new_content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
                if new_content != content:
                    content = new_content
                    if "old path" not in changes_made:
                        changes_made.append("old path")
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, changes_made
        return False, []
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False, []

def main():
    """Main function to verify and fix all HTML files"""
    html_files = list(base_dir.rglob("*.html"))
    updated_count = 0
    total_files = len(html_files)
    
    print(f"Checking {total_files} HTML files...\n")
    
    for html_file in html_files:
        updated, changes = fix_navbar_images(html_file)
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

