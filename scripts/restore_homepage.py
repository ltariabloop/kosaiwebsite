#!/usr/bin/env python3
"""
Restore homepage to original state before content updates
"""

from pathlib import Path

BASE_DIR = Path('kosai-official-website')
INDEX_FILE = BASE_DIR / 'index.html'
TEMPLATE_FILE = Path('www.groupbanyan.com/home.html')

def restore_homepage():
    """Restore homepage from original template"""
    # Read the original template
    with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Update page title
    template = template.replace(
        '<title>Homepage | KOSAI Wellness and Consulting</title>',
        '<title>Homepage | KOSAI Wellness and Consulting</title>'
    )
    
    # Write to index.html
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write(template)
    
    print("✅ Homepage restored to original state!")

if __name__ == "__main__":
    restore_homepage()

