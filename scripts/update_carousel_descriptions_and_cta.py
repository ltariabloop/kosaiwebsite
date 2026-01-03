#!/usr/bin/env python3
"""
Expand carousel descriptions and add Contact Us CTA buttons with color palette
"""

import re
from pathlib import Path

base_dir = Path("kosai-official-website")

# Expanded descriptions for Asset & Facility Management
asset_descriptions = {
    "Hotel &amp; Resort Management": """<h6><strong>Hotel &amp; Resort Management</strong></h6><p>Comprehensive management services for hotels and resorts, ensuring optimal guest experience and operational excellence. We handle everything from pre-opening planning and staff training to daily operations, revenue optimization, and quality assurance. Our proven methodologies ensure smooth operations, higher guest satisfaction scores, and improved profitability.</p>""",
    "Residential &amp; Lifestyle Management": """<h6><strong>Residential &amp; Lifestyle Management</strong></h6><p>Elevate residential communities with comprehensive lifestyle amenities and property management services. We design and operate fitness centers, wellness programs, concierge services, and community spaces that enhance resident satisfaction and property values. From concept development to ongoing operations, we create living environments that residents love and return to.</p>""",
    "CRE Management": """<h6><strong>CRE Management</strong></h6><p>Commercial real estate management solutions that maximize property value and tenant satisfaction. We specialize in managing office buildings, retail spaces, and mixed-use developments with a focus on tenant retention, operational efficiency, and asset optimization. Our approach combines strategic planning with hands-on management to deliver measurable results.</p>""",
    "Spa &amp; Wellness Management": """<h6><strong>Spa &amp; Wellness Management</strong></h6><p>Complete spa and wellness facility management, from concept to operations, ensuring exceptional guest experiences. We develop treatment menus, train therapists, implement operational systems, and manage day-to-day operations. Our expertise ensures profitable spas that deliver authentic wellness experiences while maintaining strong financial performance.</p>""",
    "Sports &amp; Fitness Management": """<h6><strong>Sports &amp; Fitness Management</strong></h6><p>Full-service management for sports clubs, fitness centers, and athletic facilities. We handle membership programs, personal training operations, group fitness scheduling, equipment maintenance, and member retention strategies. Our data-driven approach ensures facilities operate efficiently while delivering exceptional member experiences and strong financial returns.</p>"""
}

# Expanded descriptions for Corporate Advisory Services
corporate_descriptions = {
    "Business Advisory &amp; Capital": """<h6><strong>Business Advisory &amp; Capital</strong></h6><p>Strategic business advisory and capital solutions to drive growth and optimize financial performance. We provide comprehensive consulting services including business strategy development, financial planning, investment analysis, and capital structuring. Our team works closely with clients to identify opportunities, mitigate risks, and secure the right funding solutions for sustainable expansion and profitability.</p>""",
    "Sales &amp; Marketing Strategy": """<h6><strong>Sales &amp; Marketing Strategy</strong></h6><p>Data-driven sales and marketing strategies that position brands effectively and drive revenue growth. We develop comprehensive marketing plans, brand positioning strategies, digital marketing campaigns, and sales processes that convert. Our approach combines market research, consumer insights, and performance analytics to create strategies that deliver measurable ROI and sustainable competitive advantage.</p>""",
    "Executive Recruitment": """<h6><strong>Executive Recruitment</strong></h6><p>Cross-border executive recruitment services that match top talent with strategic leadership opportunities. We specialize in placing C-suite executives, senior managers, and specialized professionals in the hospitality, wellness, and fitness industries. Our extensive network, rigorous vetting process, and deep industry knowledge ensure successful placements that align with organizational culture and strategic objectives.</p>""",
    "Architecture &amp; Construction": """<h6><strong>Architecture &amp; Construction</strong></h6><p>Sustainable, guest-led design-build services delivered on brief, on time, and on budget. We manage the entire design and construction process from initial concept through final delivery. Our integrated approach ensures designs that enhance guest experiences while meeting operational requirements, sustainability goals, and financial constraints. We coordinate architects, engineers, contractors, and vendors to deliver seamless project execution.</p>"""
}

def update_carousel_slides(file_path, descriptions_dict):
    """Update carousel descriptions and add Contact Us button"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Update each description
        for title_key, new_description in descriptions_dict.items():
            # Pattern to match the description section for each service
            # Look for the field-content that contains the title
            pattern = rf'(<div class="field field--name-field-content field--type-text-long field--label-hidden field--item">)(<h6><strong>{re.escape(title_key)}</strong></h6><p>[^<]*</p>)(</div>)'
            replacement = rf'\1{new_description}\3'
            content = re.sub(pattern, replacement, content)
        
        # Add Contact Us button after each "Learn More" link
        # Find the pattern: Learn More link followed by closing divs
        # We'll add a new button after the Learn More link
        contact_button_html = '''<div class="field field--name-field-link field--type-link field--label-hidden field--item" style="margin-top: 15px;">
            <a href="contact.html" class="contact-cta-button" style="display: inline-block; padding: 12px 30px; background-color: #6F6A37; color: #F7F5EC; text-decoration: none; border-radius: 4px; font-weight: 600; transition: background-color 0.3s ease;">Contact Us</a>
          </div>'''
        
        # Add Contact Us button after each Learn More link in carousel slides
        # Pattern: Learn More link closing tag, then closing divs for the slide
        pattern = r'(<div class="field field--name-field-link field--type-link field--label-hidden field--item"><a href="[^"]*">Learn More</a></div>\s*)(</div>\s*</div>\s*<div class="slick__slide|</div>\s*</div>\s*</div>\s*<nav)'
        replacement = rf'\1{contact_button_html}\2'
        content = re.sub(pattern, replacement, content)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error updating {file_path}: {e}")
        return False

def main():
    """Main function"""
    print("Updating carousel descriptions and adding Contact Us buttons...\n")
    
    # Update Asset & Facility Management page
    asset_file = base_dir / "asset-facility-management.html"
    if asset_file.exists():
        updated = update_carousel_slides(asset_file, asset_descriptions)
        if updated:
            print("✅ Updated asset-facility-management.html")
        else:
            print("⚠️  No changes made to asset-facility-management.html")
    
    # Update Corporate Advisory Services page
    corporate_file = base_dir / "corporate-advisory-services.html"
    if corporate_file.exists():
        updated = update_carousel_slides(corporate_file, corporate_descriptions)
        if updated:
            print("✅ Updated corporate-advisory-services.html")
        else:
            print("⚠️  No changes made to corporate-advisory-services.html")
    
    print(f"\n{'='*60}")
    print("✅ Carousel updates complete!")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()

