#!/usr/bin/env python3
import re
import os
from pathlib import Path

# Read the index.html to get the header and footer structure
index_path = "kosai-official-website/index.html"
with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract header navigation (from <nav id="block-banyantree-main-menu" to </nav>)
header_match = re.search(
    r'(<nav role="navigation" aria-labelledby="block-banyantree-main-menu-menu"[^>]*>.*?</nav>)',
    index_content,
    re.DOTALL
)
header_nav = header_match.group(1) if header_match else None

# Extract footer (from <footer to </footer>)
footer_match = re.search(
    r'(<footer[^>]*>.*?</footer>)',
    index_content,
    re.DOTALL
)
footer_content = footer_match.group(1) if footer_match else None

if not header_nav or not footer_content:
    print("Error: Could not extract header or footer from index.html")
    exit(1)

print(f"✓ Extracted header navigation ({len(header_nav)} chars)")
print(f"✓ Extracted footer ({len(footer_content)} chars)")

# Get all HTML files except index.html
html_files = []
for root, dirs, files in os.walk("kosai-official-website"):
    for file in files:
        if file.endswith('.html') and file != 'index.html':
            full_path = Path(root) / file
            html_files.append(str(full_path))

print(f"\nFound {len(html_files)} HTML files to update")

# Update each HTML file
for html_file in html_files:
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Calculate relative path from this file to index.html for asset paths
        file_path = Path(html_file)
        depth = len(file_path.relative_to("kosai-official-website").parts) - 1
        path_prefix = "../" * depth if depth > 0 else ""
        
        # Replace header navigation
        old_header_match = re.search(
            r'(<nav role="navigation" aria-labelledby="block-banyantree-main-menu-menu"[^>]*>.*?</nav>)',
            content,
            re.DOTALL
        )
        if old_header_match:
            # Update paths in header_nav for this file's location
            updated_header = header_nav
            # Fix asset paths (images, etc.)
            updated_header = re.sub(
                r'src="(sites/|themes/)',
                f'src="{path_prefix}\\1',
                updated_header
            )
            updated_header = re.sub(
                r'href="(themes/|sites/)',
                f'href="{path_prefix}\\1',
                updated_header
            )
            # Fix navigation links
            updated_header = re.sub(
                r'href="([^"]+\.html)"',
                lambda m: f'href="{path_prefix}{m.group(1)}"' if not m.group(1).startswith(('http', '../', 'about-us/', 'our-solutions/', 'past-projects/')) else f'href="{m.group(1)}"',
                updated_header
            )
            
            content = content.replace(old_header_match.group(1), updated_header)
        
        # Replace footer
        old_footer_match = re.search(
            r'(<footer[^>]*>.*?</footer>)',
            content,
            re.DOTALL
        )
        if old_footer_match:
            # Update paths in footer for this file's location
            updated_footer = footer_content
            # Fix asset paths
            updated_footer = re.sub(
                r'src="(sites/|themes/)',
                f'src="{path_prefix}\\1',
                updated_footer
            )
            updated_footer = re.sub(
                r'href="(themes/|sites/)',
                f'href="{path_prefix}\\1',
                updated_footer
            )
            # Fix navigation links
            updated_footer = re.sub(
                r'href="([^"]+\.html)"',
                lambda m: f'href="{path_prefix}{m.group(1)}"' if not m.group(1).startswith(('http', '../', 'about-us/', 'our-solutions/', 'past-projects/')) else f'href="{m.group(1)}"',
                updated_footer
            )
            
            content = content.replace(old_footer_match.group(1), updated_footer)
        
        # Also update logo link
        content = re.sub(
            r'href="home\.html"',
            f'href="{path_prefix}index.html"',
            content
        )
        content = re.sub(
            r'href="([^"]*home\.html)"',
            f'href="{path_prefix}index.html"',
            content
        )
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Updated {html_file}")
        
    except Exception as e:
        print(f"✗ Error updating {html_file}: {e}")

print("\n✓ All navigation links updated!")

