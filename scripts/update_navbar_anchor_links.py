#!/usr/bin/env python3
"""
Update navbar submenu links to point to anchor links on category pages
Add IDs to "OUR SERVICES" sections on category pages
"""

import os
import re
from pathlib import Path

base_dir = Path("kosai-official-website")

# Mapping of subcategory links to their category page anchors
corporate_subcategories = {
    "our-solutions/business-advisory-capital.html": "corporate-advisory-services.html#our-services",
    "our-solutions/sales-marketing-strategy.html": "corporate-advisory-services.html#our-services",
    "our-solutions/executive-recruitment.html": "corporate-advisory-services.html#our-services",
    "our-solutions/architecture-construction.html": "corporate-advisory-services.html#our-services",
}

asset_subcategories = {
    "our-solutions/hotel-resort-management.html": "asset-facility-management.html#our-services",
    "our-solutions/residential-lifestyle-management.html": "asset-facility-management.html#our-services",
    "our-solutions/cre-management.html": "asset-facility-management.html#our-services",
    "our-solutions/spa-wellness-management.html": "asset-facility-management.html#our-services",
    "our-solutions/sports-fitness-management.html": "asset-facility-management.html#our-services",
}

def add_section_id(file_path, section_id):
    """Add ID to the OUR SERVICES section"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the section containing "OUR SERVICES" and add ID if not present
        # Look for the section block that contains wrapper-component-n with "OUR SERVICES"
        pattern = r'(<section[^>]*class="[^"]*block-block-content[^"]*experiences[^"]*"[^>]*)(id="[^"]*")?'
        
        # First, try to find the section with id="experiences" and update it
        if 'id="experiences"' in content:
            # Replace id="experiences" with id="our-services"
            content = re.sub(
                r'id="experiences"',
                'id="our-services"',
                content
            )
        elif 'id="experiences"' not in content:
            # Add id="our-services" to the section
            content = re.sub(
                r'(<section[^>]*class="[^"]*block-block-content[^"]*experiences[^"]*"[^>]*)>',
                r'\1 id="our-services">',
                content
            )
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"Error adding section ID to {file_path}: {e}")
        return False

def update_navbar_links(file_path, subcategory_mapping):
    """Update navbar submenu links in a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Update each subcategory link
        for old_link, new_link in subcategory_mapping.items():
            # Pattern to match href="old_link" in navbar context
            # Look for links in menu items
            pattern = rf'href="{re.escape(old_link)}"'
            replacement = f'href="{new_link}"'
            content = re.sub(pattern, replacement, content)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error updating navbar links in {file_path}: {e}")
        return False

def main():
    """Main function"""
    html_files = list(base_dir.rglob("*.html"))
    
    print("Updating navbar submenu links and adding section IDs...\n")
    
    # Add ID to OUR SERVICES section on category pages
    print("Adding 'our-services' ID to category pages...")
    add_section_id(base_dir / "corporate-advisory-services.html", "our-services")
    print("✅ Updated corporate-advisory-services.html")
    
    add_section_id(base_dir / "asset-facility-management.html", "our-services")
    print("✅ Updated asset-facility-management.html")
    
    # Update navbar links in all HTML files
    print("\nUpdating navbar submenu links...")
    updated_count = 0
    
    for html_file in html_files:
        updated_corporate = update_navbar_links(html_file, corporate_subcategories)
        updated_asset = update_navbar_links(html_file, asset_subcategories)
        
        if updated_corporate or updated_asset:
            print(f"✅ Updated: {html_file}")
            updated_count += 1
    
    print(f"\n{'='*60}")
    print(f"✅ Updated {updated_count} files with new anchor links")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()

