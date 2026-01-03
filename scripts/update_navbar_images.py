#!/usr/bin/env python3
"""
Update navbar images across all HTML files in kosai-official-website
"""

import os
import re
from pathlib import Path

# Base directory
base_dir = Path("kosai-official-website")

# Image mappings - new paths
image_mappings = {
    # About Us
    r'sites/btg/files/styles/hero_banner/public/2023-12/New%20About%20Us%20Banner%20Image_opacity_0\.jpg\.webp%3Fitok=xpJ4LMYN': 'images/photos/aboutus_nav.jpg',
    r'\.\./sites/btg/files/styles/hero_banner/public/2023-12/New%20About%20Us%20Banner%20Image_opacity_0\.jpg\.webp%3Fitok=xpJ4LMYN': '../images/photos/aboutus_nav.jpg',
    r'\.\./\.\./sites/btg/files/styles/hero_banner/public/2023-12/New%20About%20Us%20Banner%20Image_opacity_0\.jpg\.webp%3Fitok=xpJ4LMYN': '../../images/photos/aboutus_nav.jpg',
    
    # Asset & Facility Management
    r'sites/btg/files/2023-12/Hotels%20menu%20card\.jpg': 'images/photos/asset_nav.jpg',
    r'\.\./sites/btg/files/2023-12/Hotels%20menu%20card\.jpg': '../images/photos/asset_nav.jpg',
    r'\.\./\.\./sites/btg/files/2023-12/Hotels%20menu%20card\.jpg': '../../images/photos/asset_nav.jpg',
    
    # Corporate Advisory & Services
    # (same as Asset & Facility - Hotels menu card)
    
    # Past Projects & Experience
    # (same as About Us - New About Us Banner)
    
    # Contact Us & Careers
    r'sites/btg/files/2022-08/mission\.png': 'images/contact_nav.jpg',
    r'\.\./sites/btg/files/2022-08/mission\.png': '../images/contact_nav.jpg',
    r'\.\./\.\./sites/btg/files/2022-08/mission\.png': '../../images/contact_nav.jpg',
}

def get_path_prefix(file_path):
    """Determine the relative path prefix based on file depth"""
    parts = file_path.parts
    # Count depth from kosai-official-website
    depth = len([p for p in parts if p != 'kosai-official-website']) - 1
    if depth == 0:
        return ""
    elif depth == 1:
        return "../"
    elif depth == 2:
        return "../../"
    else:
        return "../" * depth

def update_navbar_images(file_path):
    """Update navbar images in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        path_prefix = get_path_prefix(file_path)
        
        # About Us
        if 'About Us' in content or 'about-us' in content.lower():
            # Root level
            content = re.sub(
                r'src="sites/btg/files/styles/hero_banner/public/2023-12/New%20About%20Us%20Banner%20Image_opacity_0\.jpg\.webp%3Fitok=xpJ4LMYN"',
                f'src="{path_prefix}images/photos/aboutus_nav.jpg"',
                content
            )
            # With ../ prefix
            content = re.sub(
                r'src="\.\./sites/btg/files/styles/hero_banner/public/2023-12/New%20About%20Us%20Banner%20Image_opacity_0\.jpg\.webp%3Fitok=xpJ4LMYN"',
                f'src="{path_prefix}images/photos/aboutus_nav.jpg"',
                content
            )
            # With ../../ prefix
            content = re.sub(
                r'src="\.\./\.\./sites/btg/files/styles/hero_banner/public/2023-12/New%20About%20Us%20Banner%20Image_opacity_0\.jpg\.webp%3Fitok=xpJ4LMYN"',
                f'src="{path_prefix}images/photos/aboutus_nav.jpg"',
                content
            )
        
        # Asset & Facility Management
        content = re.sub(
            r'src="([^"]*sites/btg/files/2023-12/Hotels%20menu%20card\.jpg)"',
            lambda m: f'src="{path_prefix}images/photos/asset_nav.jpg"' if 'Asset' in content or 'asset-facility' in content.lower() else m.group(0),
            content
        )
        # Also handle with ../ prefix
        content = re.sub(
            r'src="\.\./sites/btg/files/2023-12/Hotels%20menu%20card\.jpg"',
            f'src="{path_prefix}images/photos/asset_nav.jpg"',
            content
        )
        content = re.sub(
            r'src="\.\./\.\./sites/btg/files/2023-12/Hotels%20menu%20card\.jpg"',
            f'src="{path_prefix}images/photos/asset_nav.jpg"',
            content
        )
        
        # Corporate Advisory & Services (same old image as Asset)
        if 'Corporate Advisory' in content or 'corporate-advisory' in content.lower():
            content = re.sub(
                r'src="([^"]*sites/btg/files/2023-12/Hotels%20menu%20card\.jpg)"',
                f'src="{path_prefix}images/photos/corporate_nav.jpg"',
                content
            )
        
        # Past Projects & Experience (same old image as About Us)
        if 'Past Projects' in content or 'past-projects' in content.lower():
            content = re.sub(
                r'src="([^"]*sites/btg/files/styles/hero_banner/public/2023-12/New%20About%20Us%20Banner%20Image_opacity_0\.jpg\.webp%3Fitok=xpJ4LMYN)"',
                f'src="{path_prefix}images/photos/pastproject_nav.jpg"',
                content
            )
        
        # Contact Us & Careers
        if 'Contact' in content or 'Careers' in content or 'contact' in content.lower():
            content = re.sub(
                r'src="([^"]*sites/btg/files/2022-08/mission\.png)"',
                f'src="{path_prefix}images/contact_nav.jpg"',
                content
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
    """Main function to update all HTML files"""
    html_files = list(base_dir.rglob("*.html"))
    updated_count = 0
    
    for html_file in html_files:
        if update_navbar_images(html_file):
            print(f"Updated: {html_file}")
            updated_count += 1
    
    print(f"\n✅ Updated {updated_count} files")

if __name__ == "__main__":
    main()

