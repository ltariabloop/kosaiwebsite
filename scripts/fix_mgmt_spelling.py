#!/usr/bin/env python3
"""
Replace "Mgmt" with "Management" for Residential & Lifestyle throughout all HTML files
"""

import os
import re
from pathlib import Path

base_dir = Path("kosai-official-website")

def fix_mgmt_spelling(file_path):
    """Fix Mgmt spelling in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes_made = []
        
        # Replace "Residential & Lifestyle Mgmt" with "Residential & Lifestyle Management"
        if "Residential" in content and "Lifestyle" in content and "Mgmt" in content:
            # Pattern 1: "Residential & Lifestyle Mgmt" or "Residential &amp; Lifestyle Mgmt"
            content = re.sub(
                r'Residential\s*&amp;?\s*Lifestyle\s+Mgmt',
                'Residential &amp; Lifestyle Management',
                content,
                flags=re.IGNORECASE
            )
            
            # Pattern 2: "Lifestyle Mgmt" when in context of Residential
            content = re.sub(
                r'Lifestyle\s+Mgmt',
                'Lifestyle Management',
                content,
                flags=re.IGNORECASE
            )
            
            if content != original_content:
                changes_made.append("Residential & Lifestyle Mgmt")
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, changes_made
        return False, []
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False, []

def main():
    """Main function to fix all HTML files"""
    html_files = list(base_dir.rglob("*.html"))
    updated_count = 0
    total_files = len(html_files)
    
    print(f"Fixing 'Mgmt' spelling to 'Management'...\n")
    
    for html_file in html_files:
        updated, changes = fix_mgmt_spelling(html_file)
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

