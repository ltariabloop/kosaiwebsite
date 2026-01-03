#!/usr/bin/env python3
"""
Fix all Contact Us buttons - remove inline styles and rely on CSS
"""

import re
from pathlib import Path

base_dir = Path("kosai-official-website")

def fix_contact_buttons(file_path):
    """Remove inline styles from Contact Us buttons"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Pattern to find Contact Us buttons with inline styles
        # Replace with clean button without inline styles
        pattern = r'<a href="contact\.html" class="contact-cta-button"[^>]*style="[^"]*"[^>]*>Contact Us</a>'
        replacement = '<a href="contact.html" class="contact-cta-button">Contact Us</a>'
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
    print("Fixing all Contact Us buttons...\n")
    
    # Update Asset & Facility Management page
    asset_file = base_dir / "asset-facility-management.html"
    if asset_file.exists():
        updated = fix_contact_buttons(asset_file)
        if updated:
            print("✅ Updated asset-facility-management.html")
        else:
            print("⚠️  No changes made to asset-facility-management.html")
    
    # Update Corporate Advisory Services page
    corporate_file = base_dir / "corporate-advisory-services.html"
    if corporate_file.exists():
        updated = fix_contact_buttons(corporate_file)
        if updated:
            print("✅ Updated corporate-advisory-services.html")
        else:
            print("⚠️  No changes made to corporate-advisory-services.html")
    
    print(f"\n{'='*60}")
    print("✅ Contact Us button fixes complete!")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()

