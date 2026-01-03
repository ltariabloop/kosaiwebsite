#!/usr/bin/env python3
"""
Fix carousel slide content - remove duplicate titles from content field
"""

import re
from pathlib import Path

base_dir = Path("kosai-official-website")

def fix_slide_content(file_path):
    """Remove duplicate h6 titles from content field in carousel slides"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Pattern to find content fields with duplicate h6 titles
        # The content should not have <h6><strong>Title</strong></h6> since title is already in title field
        # Pattern: <h6><strong>Title</strong></h6><p>Description</p>
        # Replace with: <p>Description</p>
        
        # Match the pattern where h6 title matches the service name
        pattern = r'(<div class="field field--name-field-content field--type-text-long field--label-hidden field--item">)<h6><strong>([^<]+)</strong></h6><p>'
        replacement = r'\1<p>'
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
    """Main function"""
    print("Fixing carousel slide content - removing duplicate titles...\n")
    
    # Update Asset & Facility Management page
    asset_file = base_dir / "asset-facility-management.html"
    if asset_file.exists():
        updated = fix_slide_content(asset_file)
        if updated:
            print("✅ Updated asset-facility-management.html")
        else:
            print("⚠️  No changes made to asset-facility-management.html")
    
    # Update Corporate Advisory Services page
    corporate_file = base_dir / "corporate-advisory-services.html"
    if corporate_file.exists():
        updated = fix_slide_content(corporate_file)
        if updated:
            print("✅ Updated corporate-advisory-services.html")
        else:
            print("⚠️  No changes made to corporate-advisory-services.html")
    
    print(f"\n{'='*60}")
    print("✅ Carousel slide content fixes complete!")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()

