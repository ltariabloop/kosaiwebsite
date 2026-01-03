#!/usr/bin/env python3
"""
Check and fix navbar image alignment and sizing across all pages
"""

import re
from pathlib import Path

base_dir = Path("kosai-official-website")

def check_navbar_css(file_path):
    """Check if navbar image CSS is present and correct"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for the CSS rule
        has_css = 'height: 150px !important' in content and 'object-fit: cover !important' in content
        has_alignment = 'display: flex' in content and 'flex-direction: column' in content
        
        return has_css, has_alignment
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False, False

def add_navbar_css(file_path):
    """Add navbar image CSS if missing"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Check if CSS is already present
        if 'height: 150px !important' in content and 'object-fit: cover !important' in content:
            return False
        
        # Find the style tag or create one
        css_rules = """      .menu.menu-level-0 > .menu-item--expanded > .link-without-arrow .menu-item-image {
        width: 100% !important;
        height: 150px !important;
        object-fit: cover !important;
        display: block !important;
      }
      /* Fix menu image positioning for titles that wrap to two lines */
      .menu.menu-level-0 > .menu-item--expanded {
        display: flex !important;
        flex-direction: column !important;
        align-items: flex-start !important;
      }
      .menu.menu-level-0 > .menu-item--expanded > a:first-child {
        min-height: 48px !important;
        display: flex !important;
        align-items: center !important;
        line-height: 1.2 !important;
      }
      .menu.menu-level-0 > .menu-item--expanded > .link-without-arrow {
        margin-top: 10px !important;
        width: 100% !important;
      }"""
        
        # Try to find existing style tag
        if '</style>' in content:
            # Insert before closing style tag
            content = content.replace('</style>', css_rules + '\n    </style>', 1)
        elif '<style>' in content:
            # Add after opening style tag
            content = content.replace('<style>', '<style>\n' + css_rules, 1)
        else:
            # Add style tag in head
            if '</head>' in content:
                style_tag = f'    <style>\n{css_rules}\n    </style>\n'
                content = content.replace('</head>', style_tag + '</head>', 1)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error updating {file_path}: {e}")
        return False

def verify_image_tags(file_path):
    """Verify image tags have correct structure"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for menu-item-image class
        images = re.findall(r'<img[^>]*class="[^"]*menu-item-image[^"]*"[^>]*>', content)
        
        issues = []
        for img in images:
            if 'img-responsive' not in img:
                issues.append("Missing 'img-responsive' class")
            if 'alt=' not in img:
                issues.append("Missing alt attribute")
            if 'src=' not in img:
                issues.append("Missing src attribute")
        
        return issues
    except Exception as e:
        print(f"Error verifying images in {file_path}: {e}")
        return []

def main():
    """Main function"""
    html_files = list(base_dir.rglob("*.html"))
    
    print("Checking navbar image alignment and sizing across all pages...\n")
    
    css_fixed = 0
    css_already_present = 0
    image_issues = 0
    
    for html_file in html_files:
        has_css, has_alignment = check_navbar_css(html_file)
        
        if not has_css:
            if add_navbar_css(html_file):
                print(f"✅ Added CSS to: {html_file}")
                css_fixed += 1
            else:
                print(f"⚠️  Could not add CSS to: {html_file}")
        else:
            css_already_present += 1
        
        # Verify image tags
        issues = verify_image_tags(html_file)
        if issues:
            print(f"⚠️  Image issues in {html_file}: {', '.join(issues)}")
            image_issues += len(issues)
    
    print(f"\n{'='*60}")
    print(f"✅ CSS already present: {css_already_present} files")
    print(f"✅ CSS added: {css_fixed} files")
    if image_issues > 0:
        print(f"⚠️  Image issues found: {image_issues}")
    else:
        print(f"✅ All image tags verified")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()

