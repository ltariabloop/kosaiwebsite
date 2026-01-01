#!/usr/bin/env python3
import re

file_path = "kosai-official-website/index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove chatbot script (wcSettings and wechat injection)
chatbot_script_pattern = r'<script type="text/javascript">\s*window\.wcSettings = \{.*?\}\(document,"script", "wc-dom-id"\);</script>'
content = re.sub(chatbot_script_pattern, '', content, flags=re.DOTALL)

# Remove wechat CSS link
content = re.sub(r'<link rel="stylesheet"[^>]*btg_block_wechat[^>]*>', '', content)

# Remove wechat block section (entire section including modal)
wechat_section_pattern = r'<section id="block-wechatblock"[^>]*>.*?</section>'
content = re.sub(wechat_section_pattern, '', content, flags=re.DOTALL)

# Remove wechat JS
content = re.sub(r'<script[^>]*btg_wechat[^>]*></script>', '', content)

# Remove "Join Us" section
joinus_pattern = r'<nav role="navigation" aria-labelledby="block-joinus-menu" id="block-joinus"[^>]*>.*?</nav>'
content = re.sub(joinus_pattern, '', content, flags=re.DOTALL)

# Update footer navigation to match header structure
# Footer Column 1: About Us
footer_col1_new = '''      <ul class="menu menu--footer-col-1 nav">
                      <li class="first">
                                        <a href="about-us.html" data-drupal-link-system-path="node/51">About Us</a>
              </li>
        </ul>'''

# Footer Column 2: Asset & Facility Management, Corporate Advisory & Services
footer_col2_new = '''      <ul class="menu menu--footer-col-2 nav">
                      <li class="first">
                                        <a href="asset-facility-management.html" data-drupal-link-system-path="node/asset-facility">Asset &amp; Facility Management</a>
              </li>
                      <li>
                                        <a href="corporate-advisory-services.html" data-drupal-link-system-path="node/corporate-advisory">Corporate Advisory &amp; Services</a>
              </li>
        </ul>'''

# Footer Column 3: Past Projects, Careers, Contact
footer_col3_new = '''      <ul class="menu menu--footer-col-3 nav">
                      <li class="first">
                                        <a href="past-projects.html" data-drupal-link-system-path="node/past-projects">Past Projects &amp; Experience</a>
              </li>
                      <li>
                                        <a href="careers.html" data-drupal-link-system-path="node/101">Careers</a>
              </li>
                      <li class="last">
                                        <a href="contact.html" data-drupal-link-system-path="node/91">Contact Us</a>
              </li>
        </ul>'''

# Replace footer columns
footer_col1_pattern = r'<ul class="menu menu--footer-col-1 nav">.*?</ul>'
content = re.sub(footer_col1_pattern, footer_col1_new, content, flags=re.DOTALL)

footer_col2_pattern = r'<ul class="menu menu--footer-col-2 nav">.*?</ul>'
content = re.sub(footer_col2_pattern, footer_col2_new, content, flags=re.DOTALL)

footer_col3_pattern = r'<ul class="menu menu--footer-col-3 nav">.*?</ul>'
content = re.sub(footer_col3_pattern, footer_col3_new, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Removed chatbot")
print("✓ Removed Join Us and With Banyan sections")
print("✓ Updated footer navigation to match header structure")

