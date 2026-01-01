# KOSAI Wellness and Consulting Website

Official website for KOSAI Wellness and Consulting, built from the original Banyan Group website structure.

## Project Structure

```
kosai-official-website/     # Main website (production files)
├── index.html              # Homepage
├── about-us.html           # About Us page
├── asset-facility-management.html
├── corporate-advisory-services.html
├── past-projects.html
├── contact.html
├── careers.html
├── our-solutions/          # Solution pages
├── past-projects/          # Past project pages
├── about-us/               # About Us sub-pages
├── themes/                 # CSS and JavaScript
├── modules/                # Drupal modules
├── libraries/              # Third-party libraries
└── sites/                  # Site assets (images, files)

www.groupbanyan.com/        # Original scraped website (reference)

scripts/                    # Python utility scripts
docs/                       # Documentation
archive/                    # Archived/old files
```

## Color Palette

- **Coastal Linen** (#F7F5EC) - Primary background
- **Sandy Beige** (#D1C7B3) - Accent color
- **Olive Palm** (#6F6A37) - Primary text/headers
- **Cocoa Cliff** (#695647) - Secondary text/borders

## Development

### Local Server

To run the website locally:

```bash
cd kosai-official-website
python3 -m http.server 8000
```

Then open http://localhost:8000 in your browser.

### Scripts

Utility scripts are located in the `scripts/` directory:

- `create_category_pages.py` - Generate category pages from templates
- `fix_relative_paths.py` - Fix asset paths based on directory depth
- `update_all_navigation.py` - Update navigation across all pages

## Navigation Structure

- **About Us** - Single consolidated page
- **Asset & Facility Management**
  - Hotel & Resort Management
  - Residential & Lifestyle Management
  - CRE Management
  - Spa & Wellness Management
  - Sports & Fitness Management
- **Corporate Advisory & Services**
  - Business Advisory & Capital
  - Sales & Marketing Strategy
  - Executive Recruitment
  - Architecture & Construction
- **Past Projects & Experience**
  - Hotels & Resorts
  - Restaurants
  - Spa & Wellness
  - Recruitment
- **Contact Us & Careers**
  - Contact Us
  - Careers

## Notes

- All pages use consistent header and footer
- Header menu images have fixed height (250px) for consistency
- CSS paths are automatically adjusted based on directory depth
- Original website structure preserved from `www.groupbanyan.com`

