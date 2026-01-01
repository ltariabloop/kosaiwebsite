#!/usr/bin/env python3
from pathlib import Path
import re

# Read the retreats-experiences template
template_file = Path('www.groupbanyan.com/retreats-experiences.html')
with open(template_file, 'r', encoding='utf-8') as f:
    template = f.read()

# Read index.html to get the header and footer
index_file = Path('kosai-official-website/index.html')
with open(index_file, 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract header and footer
header_match = re.search(r'(<header[^>]*>.*?</header>)', index_content, re.DOTALL)
footer_match = re.search(r'(<footer[^>]*>.*?</footer>)', index_content, re.DOTALL)
header = header_match.group(1) if header_match else ''
footer = footer_match.group(1) if footer_match else ''

# Extract head section from index.html
head_match = re.search(r'(<head>.*?</head>)', index_content, re.DOTALL)
head_template = head_match.group(1) if head_match else ''

# Page configurations
pages_config = {
    'asset-facility-management.html': {
        'title': 'Asset & Facility Management | KOSAI Wellness and Consulting',
        'h1': 'ASSET & FACILITY MANAGEMENT',
        'intro': 'KOSAI provides comprehensive asset and facility management services across hospitality, residential, commercial, spa, and fitness sectors. Our expertise ensures optimal performance, operational efficiency, and long-term value creation for your properties.',
        'sections': [
            {'title': 'Hotel & Resort Management', 'link': 'our-solutions/hotel-resort-management.html'},
            {'title': 'Residential & Lifestyle Management', 'link': 'our-solutions/residential-lifestyle-management.html'},
            {'title': 'CRE Management', 'link': 'our-solutions/cre-management.html'},
            {'title': 'Spa & Wellness Management', 'link': 'our-solutions/spa-wellness-management.html'},
            {'title': 'Sports & Fitness Management', 'link': 'our-solutions/sports-fitness-management.html'},
        ]
    },
    'corporate-advisory-services.html': {
        'title': 'Corporate Advisory & Services | KOSAI Wellness and Consulting',
        'h1': 'CORPORATE ADVISORY & SERVICES',
        'intro': 'KOSAI delivers strategic advisory and operational services to help businesses achieve their goals. From business development and capital solutions to sales, marketing, recruitment, and construction, we provide end-to-end support for sustainable growth.',
        'sections': [
            {'title': 'Business Advisory & Capital', 'link': 'our-solutions/business-advisory-capital.html'},
            {'title': 'Sales & Marketing Strategy', 'link': 'our-solutions/sales-marketing-strategy.html'},
            {'title': 'Executive Recruitment', 'link': 'our-solutions/executive-recruitment.html'},
            {'title': 'Architecture & Construction', 'link': 'our-solutions/architecture-construction.html'},
        ]
    },
    'past-projects.html': {
        'title': 'Past Projects & Experience | KOSAI Wellness and Consulting',
        'h1': 'PAST PROJECTS & EXPERIENCE',
        'intro': 'KOSAI has successfully delivered projects across multiple sectors, building a portfolio of excellence in hospitality, wellness, fitness, and commercial real estate. Explore our track record of transformative projects and proven results.',
        'sections': [
            {'title': 'Hotels & Resorts', 'link': 'past-projects/hotels-resorts.html'},
            {'title': 'Restaurants', 'link': 'past-projects/restaurants.html'},
            {'title': 'Spa & Wellness', 'link': 'past-projects/spa-wellness.html'},
            {'title': 'Recruitment', 'link': 'past-projects/recruitment.html'},
        ]
    },
    'contact.html': {
        'title': 'Contact Us & Careers | KOSAI Wellness and Consulting',
        'h1': 'CONTACT US & CAREERS',
        'intro': 'Get in touch with KOSAI Wellness and Consulting. Whether you\'re seeking our services, exploring career opportunities, or have questions about our solutions, we\'re here to help you achieve your goals.',
        'sections': [
            {'title': 'Contact Us', 'link': 'contact.html'},
            {'title': 'Careers', 'link': 'careers.html'},
        ]
    }
}

def create_section_html(section, index, total):
    """Create HTML for a single section"""
    component_class = 'wrapper-component-d-a' if index % 2 == 0 else 'wrapper-component-d-b'
    section_id = section['title'].lower().replace(' ', '-').replace('&', '').replace('amp;', '')
    
    if index % 2 == 0:  # Image on left
        return f'''  <section class="block block-block-content block-block-content-{index+1} clearfix" id="{section_id}">
          <div class="wrapper-imgs-txt">
        
          
<div class="{component_class}" style="background-color: #F7F5EC">
  <div class="{component_class}-wrapper">
    <div class="row">
      <div class="col-md-6 wrapper-image" data-aos="custom-fade-in" data-aos-easing="ease-in-out" data-aos-duration="1500">
        
            <div class="field field--name-field-image field--type-image field--label-hidden field--item"><img loading="lazy" src="sites/btg/files/2023-12/Hotels%20menu%20card.jpg" alt="{section['title']}" class="img-responsive" /></div>
      
      </div>
      <div class="col-md-6 wrapper-content">
        <div class="wrapper-title" style="color: #000000" data-aos="custom-fade-in" data-aos-easing="ease-in-out" data-aos-duration="1500">
          
        </div>
        <div class="wrapper-description" style="color: #000000" data-aos="custom-fade-in" data-aos-easing="ease-in-out" data-aos-duration="1500">
          
            <div class="field field--name-body field--type-text-with-summary field--label-hidden field--item"><h3>{section['title'].upper()}</h3><p>&nbsp;</p><p>Explore our comprehensive {section['title'].lower()} services designed to optimize performance and deliver measurable results.</p></div>
      
        </div>
        <div class="wrapper-link" style="color: #000000" data-aos="custom-fade-in" data-aos-easing="ease-in-out" data-aos-duration="1500">
          
            <div class="field field--name-field-link field--type-link field--label-hidden field--item"><a href="{section['link']}">Learn More</a></div>
      
        </div>
      </div>
    </div>
  </div>
</div>
        
      </div>
      </section>
'''
    else:  # Image on right
        return f'''  <section class="block block-block-content block-block-content-{index+1} clearfix" id="{section_id}">
          <div class="wrapper-imgs-txt">
        
          
<div class="{component_class}" style="background-color: #F7F5EC">
  <div class="{component_class}-wrapper">
    <div class="row">
      <div class="col-md-6 wrapper-content">
        <div class="wrapper-title" style="color: #000000" data-aos="custom-fade-in" data-aos-easing="ease-in-out" data-aos-duration="1500">
          
        </div>
        <div class="wrapper-description" style="color: #000000" data-aos="custom-fade-in" data-aos-easing="ease-in-out" data-aos-duration="1500">
          
            <div class="field field--name-body field--type-text-with-summary field--label-hidden field--item"><h3>{section['title'].upper()}</h3><p>&nbsp;</p><p>Explore our comprehensive {section['title'].lower()} services designed to optimize performance and deliver measurable results.</p></div>
      
        </div>
        <div class="wrapper-link" style="color: #000000" data-aos="custom-fade-in" data-aos-easing="ease-in-out" data-aos-duration="1500">
          
            <div class="field field--name-field-link field--type-link field--label-hidden field--item"><a href="{section['link']}">Learn More</a></div>
      
        </div>
      </div>
      <div class="col-md-6 wrapper-image" data-aos="custom-fade-in" data-aos-easing="ease-in-out" data-aos-duration="1500">
        
            <div class="field field--name-field-image field--type-image field--label-hidden field--item"><img loading="lazy" src="sites/btg/files/2023-12/Hotels%20menu%20card.jpg" alt="{section['title']}" class="img-responsive" /></div>
      
      </div>
    </div>
  </div>
</div>
        
      </div>
      </section>
'''

def create_page_content(filename, config):
    # Start with template structure
    content = template
    
    # Update head section
    head_start = content.find('<head>')
    head_end = content.find('</head>')
    if head_start != -1 and head_end != -1:
        # Update title and canonical
        new_head = head_template
        new_head = re.sub(r'<title>.*?</title>', f'<title>{config["title"]}</title>', new_head)
        new_head = re.sub(r'<link rel="canonical" href="[^"]+"', f'<link rel="canonical" href="{filename}"', new_head)
        new_head = re.sub(r'<link rel="shortlink" href="[^"]+"', f'<link rel="shortlink" href="{filename}"', new_head)
        content = content[:head_start] + new_head + content[head_end + 7:]
    
    # Update header
    old_header_match = re.search(r'(<header[^>]*>.*?</header>)', content, re.DOTALL)
    if old_header_match:
        content = content.replace(old_header_match.group(1), header)
    
    # Update footer
    old_footer_match = re.search(r'(<footer[^>]*>.*?</footer>)', content, re.DOTALL)
    if old_footer_match:
        content = content.replace(old_footer_match.group(1), footer)
    
    # Update body class
    content = re.sub(r'<body[^>]*class="[^"]*"', '<body class="path-node page-node-type-page has-glyphicons"', content)
    
    # Update hero banner H1
    content = re.sub(
        r'<h1>RETREATS &amp; EXPERIENCES</h1>',
        f'<h1>{config["h1"]}</h1>',
        content
    )
    
    # Update intro section
    intro_section = f'<div class="field field--name-body field--type-text-with-summary field--label-hidden field--item"><p>{config["intro"]}</p></div>'
    content = re.sub(
        r'<div class="field field--name-body field--type-text-with-summary field--label-hidden field--item"><p>We welcome you to join our retreats.*?</p></div>',
        intro_section,
        content,
        flags=re.DOTALL
    )
    
    # Create sections HTML for subsections
    sections_html = ''
    for i, section in enumerate(config['sections']):
        sections_html += create_section_html(section, i, len(config['sections']))
    
    # Find where to insert sections (after intro section)
    intro_end = content.find('</section>', content.find('id="retreats-with-banyan-group"'))
    if intro_end != -1:
        # Find the next layout div
        next_layout = content.find('<div class="layout layout--onecol">', intro_end)
        if next_layout != -1:
            # Insert our sections before the existing content sections
            content = content[:next_layout] + sections_html + content[next_layout:]
    
    # Remove existing retreat-specific sections
    content = re.sub(
        r'<section[^>]*id="upcoming-events"[^>]*>.*?</section>',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Remove all existing retreat/experience sections but keep layout structure
    # Find the section starting with "BANYAN TREE CONNECTIONS" and remove everything until "EXPERIENCES"
    content = re.sub(
        r'<section[^>]*id="banyan-tree-connections"[^>]*>.*?<section[^>]*id="experiences"[^>]*>',
        '<section class="block block-block-content block-block-content-experiences clearfix" id="experiences">',
        content,
        flags=re.DOTALL
    )
    
    # Remove the "EXPERIENCES" carousel section
    content = re.sub(
        r'<section[^>]*id="experiences"[^>]*>.*?<section[^>]*id="signature-programme"[^>]*>',
        '<section class="block block-layout-builder block-inline-blocksimple-title clearfix" id="signature-programme">',
        content,
        flags=re.DOTALL
    )
    
    # Remove signature programme section
    content = re.sub(
        r'<section[^>]*id="signature-programme"[^>]*>.*?</section>',
        '',
        content,
        flags=re.DOTALL
    )
    
    return content

# Create all pages
for filename, config in pages_config.items():
    page_content = create_page_content(filename, config)
    output_file = Path(f'kosai-official-website/{filename}')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(page_content)
    print(f"✓ Created {filename}")

print("\n✓ All pages created!")

