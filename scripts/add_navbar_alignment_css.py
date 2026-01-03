#!/usr/bin/env python3
"""
Add missing navbar alignment CSS to pages that need it
"""

import re
from pathlib import Path

base_dir = Path("kosai-official-website")

def add_alignment_css(file_path):
    """Add flex alignment CSS if missing"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Check if alignment CSS is already present
        if 'display: flex' in content and 'flex-direction: column' in content and 'align-items: flex-start' in content:
            return False
        
        # Alignment CSS rules
        alignment_css = """      /* Fix menu image positioning for titles that wrap to two lines */
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
        
        # Find where to insert - look for existing menu-item-image CSS
        if '.menu-item-image' in content:
            # Insert after the menu-item-image CSS rule
            pattern = r'(\.menu\.menu-level-0 > \.menu-item--expanded > \.link-without-arrow \.menu-item-image[^}]+})'
            replacement = r'\1\n' + alignment_css
            content = re.sub(pattern, replacement, content)
        elif '</style>' in content:
            # Insert before closing style tag
            content = content.replace('</style>', alignment_css + '\n    </style>', 1)
        elif '<style>' in content:
            # Add after opening style tag
            content = content.replace('<style>', '<style>\n' + alignment_css, 1)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error updating {file_path}: {e}")
        return False

def main():
    """Main function"""
    files_to_fix = [
        base_dir / "past-projects.html",
        base_dir / "contact.html",
        base_dir / "corporate-advisory-services.html",
        base_dir / "about-us.html",
        base_dir / "asset-facility-management.html",
    ]
    
    print("Adding navbar alignment CSS to pages that need it...\n")
    
    fixed_count = 0
    
    for file_path in files_to_fix:
        if file_path.exists():
            if add_alignment_css(file_path):
                print(f"✅ Updated: {file_path}")
                fixed_count += 1
            else:
                print(f"⚠️  No changes needed: {file_path}")
        else:
            print(f"⚠️  File not found: {file_path}")
    
    print(f"\n{'='*60}")
    print(f"✅ Updated {fixed_count} files")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()

