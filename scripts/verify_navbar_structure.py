#!/usr/bin/env python3
"""
Verify navbar image structure and alignment across all pages
"""

import re
from pathlib import Path

base_dir = Path("kosai-official-website")

def verify_navbar_structure(file_path):
    """Verify navbar image structure is correct"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        issues = []
        
        # Check for menu-item-image tags
        image_pattern = r'<img[^>]*class="[^"]*menu-item-image[^"]*"[^>]*>'
        images = re.findall(image_pattern, content)
        
        for img in images:
            # Check required attributes
            if 'img-responsive' not in img:
                issues.append("Missing 'img-responsive' class")
            if 'alt=' not in img:
                issues.append("Missing alt attribute")
            if 'src=' not in img:
                issues.append("Missing src attribute")
            
            # Check if image is inside link-without-arrow
            # This is harder to check with regex, so we'll check the context
        
        # Check CSS rules
        if 'height: 150px !important' not in content:
            issues.append("Missing height CSS rule")
        if 'object-fit: cover !important' not in content:
            issues.append("Missing object-fit CSS rule")
        if 'display: flex' not in content or 'flex-direction: column' not in content:
            issues.append("Missing flex alignment CSS")
        
        return issues, len(images)
    except Exception as e:
        return [f"Error: {e}"], 0

def main():
    """Main function"""
    html_files = list(base_dir.rglob("*.html"))
    
    print("Verifying navbar image structure and alignment...\n")
    
    total_issues = 0
    files_with_issues = []
    total_images = 0
    
    for html_file in html_files:
        issues, image_count = verify_navbar_structure(html_file)
        total_images += image_count
        
        if issues:
            print(f"⚠️  {html_file}:")
            for issue in issues:
                print(f"   - {issue}")
            files_with_issues.append(html_file)
            total_issues += len(issues)
    
    print(f"\n{'='*60}")
    print(f"📊 Summary:")
    print(f"   Total files checked: {len(html_files)}")
    print(f"   Total navbar images found: {total_images}")
    print(f"   Files with issues: {len(files_with_issues)}")
    print(f"   Total issues: {total_issues}")
    
    if total_issues == 0:
        print(f"\n✅ All navbar images are properly structured!")
    else:
        print(f"\n⚠️  Issues found - review needed")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()

