#!/usr/bin/env python3
"""
Fix Contact Us CTA buttons in carousel slides to ensure they are visible
"""

import re
from pathlib import Path

base_dir = Path("kosai-official-website")

def fix_cta_buttons(file_path):
    """Fix Contact Us buttons in carousel slides"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Pattern to find the Contact Us button that might be hidden
        # We need to ensure it's not inside field--label-hidden or make it visible
        # Replace the hidden field wrapper with a visible one
        
        # Pattern 1: Button inside field--label-hidden - remove the hidden class or make it visible
        pattern1 = r'(<div class="field field--name-field-link field--type-link field--label-hidden field--item" style="margin-top: 15px;">\s*<a href="contact\.html" class="contact-cta-button"[^>]*>Contact Us</a>\s*</div>)'
        replacement1 = r'<div class="field field--name-field-link field--type-link field--item" style="margin-top: 15px; display: block !important;"><a href="contact.html" class="contact-cta-button" style="display: inline-block !important; padding: 12px 30px; background-color: #6F6A37; color: #F7F5EC; text-decoration: none; border-radius: 4px; font-weight: 600; transition: background-color 0.3s ease; margin-top: 10px;">Contact Us</a></div>'
        content = re.sub(pattern1, replacement1, content)
        
        # Pattern 2: If button doesn't exist, add it after Learn More link
        # Look for Learn More link followed by closing divs, and add button before closing
        pattern2 = r'(<div class="field field--name-field-link field--type-link field--label-hidden field--item"><a href="[^"]*">Learn More</a></div>\s*)(</div>\s*</div>\s*<div class="slick__slide)'
        
        def add_button_if_missing(match):
            learn_more = match.group(1)
            closing = match.group(2)
            # Check if Contact Us button already exists in this slide
            # If not, add it
            if 'contact-cta-button' not in learn_more:
                button = '<div class="field field--name-field-link field--type-link field--item" style="margin-top: 15px; display: block !important;"><a href="contact.html" class="contact-cta-button" style="display: inline-block !important; padding: 12px 30px; background-color: #6F6A37; color: #F7F5EC; text-decoration: none; border-radius: 4px; font-weight: 600; transition: background-color 0.3s ease; margin-top: 10px;">Contact Us</a></div>\n      '
                return learn_more + button + closing
            return match.group(0)
        
        content = re.sub(pattern2, add_button_if_missing, content)
        
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
    print("Fixing Contact Us CTA buttons in carousel slides...\n")
    
    # Update Asset & Facility Management page
    asset_file = base_dir / "asset-facility-management.html"
    if asset_file.exists():
        updated = fix_cta_buttons(asset_file)
        if updated:
            print("✅ Updated asset-facility-management.html")
        else:
            print("⚠️  No changes made to asset-facility-management.html")
    
    # Update Corporate Advisory Services page
    corporate_file = base_dir / "corporate-advisory-services.html"
    if corporate_file.exists():
        updated = fix_cta_buttons(corporate_file)
        if updated:
            print("✅ Updated corporate-advisory-services.html")
        else:
            print("⚠️  No changes made to corporate-advisory-services.html")
    
    print(f"\n{'='*60}")
    print("✅ CTA button fixes complete!")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()

