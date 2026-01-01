#!/usr/bin/env python3
import re
import os
from pathlib import Path

# Get all HTML files
html_files = []
for root, dirs, files in os.walk("kosai-official-website"):
    for file in files:
        if file.endswith('.html'):
            full_path = Path(root) / file
            rel_path = full_path.relative_to("kosai-official-website")
            html_files.append(str(rel_path).replace('\\', '/'))

print("Found HTML files:")
for f in sorted(html_files):
    print(f"  {f}")

# File path mappings
path_mappings = {
    # About Us
    'about-us.html': 'about-us/who-we-are.html',  # Main About Us page
    'who-we-are.html': 'about-us/who-we-are.html',
    'our-team.html': 'about-us/our-team.html',
    
    # Asset & Facility Management
    'hotel-resort-management.html': 'our-solutions/hotel-resort-management.html',
    'residential-lifestyle-management.html': 'our-solutions/residential-lifestyle-management.html',
    'cre-management.html': 'our-solutions/cre-management.html',
    'spa-wellness-management.html': 'our-solutions/spa-wellness-management.html',
    'sports-fitness-management.html': 'our-solutions/sports-fitness-management.html',
    
    # Corporate Advisory & Services
    'business-advisory-capital.html': 'our-solutions/business-advisory-capital.html',
    'sales-marketing-strategy.html': 'our-solutions/sales-marketing-strategy.html',
    'executive-recruitment.html': 'our-solutions/executive-recruitment.html',
    'architecture-construction.html': 'our-solutions/architecture-construction.html',
    
    # Past Projects
    'past-projects.html': 'past-projects/hotels-resorts.html',  # Main Past Projects page
    'past-projects-hotels-resorts.html': 'past-projects/hotels-resorts.html',
    'past-projects-restaurants.html': 'past-projects/restaurants.html',
    'past-projects-spa-wellness.html': 'past-projects/spa-wellness.html',
    'past-projects-recruitment.html': 'past-projects/recruitment.html',
}

file_path = "kosai-official-website/index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Update header navigation links
for old_path, new_path in path_mappings.items():
    # Update href attributes
    content = re.sub(
        rf'href="{re.escape(old_path)}"',
        f'href="{new_path}"',
        content
    )
    # Also update links that might have .html extension variations
    old_base = old_path.replace('.html', '')
    new_base = new_path.replace('.html', '')
    if old_base != old_path:
        content = re.sub(
            rf'href="{re.escape(old_base)}"',
            f'href="{new_base}"',
            content
        )

# Update footer links
# Footer Column 1
content = re.sub(
    r'href="about-us\.html"',
    'href="about-us/who-we-are.html"',
    content
)

# Footer Column 2 - already correct (asset-facility-management.html and corporate-advisory-services.html are in root)

# Footer Column 3
content = re.sub(
    r'href="past-projects\.html"',
    'href="past-projects/hotels-resorts.html"',
    content
)

# Update logo link to point to index
content = re.sub(
    r'href="home\.html"',
    'href="index.html"',
    content
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✓ Updated navigation links in index.html")

