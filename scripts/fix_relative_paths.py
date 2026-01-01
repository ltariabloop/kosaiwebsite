#!/usr/bin/env python3
import re
import os
from pathlib import Path

def get_relative_path(from_file, to_file):
    """Calculate relative path from one file to another"""
    from_path = Path(from_file).parent
    to_path = Path(to_file)
    
    # If to_file is absolute, make it relative to kosai-official-website
    if to_path.is_absolute():
        to_path = to_path.relative_to(Path("kosai-official-website"))
    
    try:
        rel_path = Path(os.path.relpath(to_path, from_path))
        return str(rel_path).replace('\\', '/')
    except:
        return str(to_path).replace('\\', '/')

# File mappings
file_mappings = {
    'about-us.html': 'about-us/who-we-are.html',
    'who-we-are.html': 'about-us/who-we-are.html',
    'our-team.html': 'about-us/our-team.html',
    'asset-facility-management.html': 'asset-facility-management.html',
    'corporate-advisory-services.html': 'corporate-advisory-services.html',
    'hotel-resort-management.html': 'our-solutions/hotel-resort-management.html',
    'residential-lifestyle-management.html': 'our-solutions/residential-lifestyle-management.html',
    'cre-management.html': 'our-solutions/cre-management.html',
    'spa-wellness-management.html': 'our-solutions/spa-wellness-management.html',
    'sports-fitness-management.html': 'our-solutions/sports-fitness-management.html',
    'business-advisory-capital.html': 'our-solutions/business-advisory-capital.html',
    'sales-marketing-strategy.html': 'our-solutions/sales-marketing-strategy.html',
    'executive-recruitment.html': 'our-solutions/executive-recruitment.html',
    'architecture-construction.html': 'our-solutions/architecture-construction.html',
    'past-projects.html': 'past-projects/hotels-resorts.html',
    'past-projects-hotels-resorts.html': 'past-projects/hotels-resorts.html',
    'past-projects-restaurants.html': 'past-projects/restaurants.html',
    'past-projects-spa-wellness.html': 'past-projects/spa-wellness.html',
    'past-projects-recruitment.html': 'past-projects/recruitment.html',
    'careers.html': 'careers.html',
    'contact.html': 'contact.html',
    'home.html': 'index.html',
    'index.html': 'index.html',
}

# Get all HTML files
html_files = []
for root, dirs, files in os.walk("kosai-official-website"):
    for file in files:
        if file.endswith('.html'):
            full_path = Path(root) / file
            html_files.append(str(full_path))

print(f"Updating {len(html_files)} HTML files...")

for html_file in html_files:
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        file_path = Path(html_file)
        file_dir = file_path.parent
        
        # Update all href links
        for old_name, new_path in file_mappings.items():
            # Calculate correct relative path from this file
            target_path = Path("kosai-official-website") / new_path
            rel_path = get_relative_path(file_dir, target_path)
            
            # Update href attributes
            # Pattern 1: href="filename.html"
            pattern1 = rf'href="{re.escape(old_name)}"'
            replacement1 = f'href="{rel_path}"'
            content = re.sub(pattern1, replacement1, content)
            
            # Pattern 2: href="../filename.html" or href="filename.html" in navigation
            pattern2 = rf'href="([^"]*/)?{re.escape(old_name)}"'
            def replace_func(m):
                prefix = m.group(1) if m.group(1) else ""
                # If it already has a relative path, calculate the correct one
                if prefix.startswith('../') or prefix.startswith('./'):
                    return f'href="{rel_path}"'
                return f'href="{rel_path}"'
            content = re.sub(pattern2, replace_func, content)
        
        # Fix logo link
        content = re.sub(
            r'href="([^"]*)?home\.html"',
            lambda m: f'href="{get_relative_path(file_dir, Path("kosai-official-website/index.html"))}"',
            content
        )
        
        if content != original_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Updated {html_file}")
        
    except Exception as e:
        print(f"✗ Error updating {html_file}: {e}")

print("\n✓ All relative paths fixed!")

