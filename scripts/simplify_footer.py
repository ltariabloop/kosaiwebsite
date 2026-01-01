#!/usr/bin/env python3
import re

file_path = "kosai-official-website/index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the Brands section (from <nav id="block-brands" to </nav>)
brands_pattern = r'<nav role="navigation" aria-labelledby="block-brands-menu" id="block-brands"[^>]*>.*?</nav>'
content = re.sub(brands_pattern, '', content, flags=re.DOTALL)

# Remove "In Partnership with" sections (already done, but check if any remain)
partnership_pattern = r'<section[^>]*id="block-partnershiplogo[^"]*"[^>]*>.*?</section>'
content = re.sub(partnership_pattern, '', content, flags=re.DOTALL)

# Also remove any wrapper-partnership divs
partnership_div_pattern = r'<div class="wrapper-partnership">.*?</div>'
content = re.sub(partnership_div_pattern, '', content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Footer simplified: Removed Brands section and Partnership sections")

