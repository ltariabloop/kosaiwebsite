#!/usr/bin/env python3
"""
Update all navbar logos to use white logo (kosailogo_white.png) 
for better visibility on dark/transparent backgrounds
"""

import re
from pathlib import Path

base_dir = Path("kosai-official-website")

def get_path_prefix(file_path):
    """Calculate relative path prefix based on file depth"""
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

def update_logo_in_file(file_path):
    """Update logo to white version in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        path_prefix = get_path_prefix(file_path)
        
        # Pattern to match the logo image tag
        # Match both relative paths (themes/custom/banyantree/images/kosai-logo.png) 
        # and paths with ../ prefixes
        patterns = [
            # Pattern 1: themes/custom/banyantree/images/kosai-logo.png (root level)
            (r'src="themes/custom/banyantree/images/kosai-logo\.png"', 
             f'src="{path_prefix}images/photos/logos/kosailogo_white.png"'),
            # Pattern 2: ../themes/custom/banyantree/images/kosai-logo.png (subdirectory)
            (r'src="\.\./themes/custom/banyantree/images/kosai-logo\.png"', 
             f'src="{path_prefix}images/photos/logos/kosailogo_white.png"'),
            # Pattern 3: ../../themes/custom/banyantree/images/kosai-logo.png (nested subdirectory)
            (r'src="\.\./\.\./themes/custom/banyantree/images/kosai-logo\.png"', 
             f'src="{path_prefix}images/photos/logos/kosailogo_white.png"'),
        ]
        
        for pattern, replacement in patterns:
            content = re.sub(pattern, replacement, content)
        
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
    total_files = len(html_files)
    
    print(f"Updating logos to white version across all navbars...\n")
    
    for html_file in html_files:
        if update_logo_in_file(html_file):
            print(f"✅ Updated: {html_file}")
            updated_count += 1
    
    print(f"\n{'='*60}")
    print(f"✅ Updated {updated_count} out of {total_files} files")
    print(f"{'='*60}")
    
    # Verify the white logo file exists
    white_logo = base_dir / "images/photos/logos/kosailogo_white.png"
    if white_logo.exists():
        print(f"✅ White logo file found: {white_logo}")
    else:
        print(f"⚠️  Warning: White logo file not found at {white_logo}")

if __name__ == "__main__":
    main()

