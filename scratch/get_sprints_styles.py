import urllib.request
import re
import ssl

context = ssl._create_unverified_context()

def get_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
        }
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=context, timeout=10) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

# Fetch Sprints.ai homepage
html = get_page("https://sprints.ai")
if html:
    print("Successfully fetched HTML")
    # Search for fonts
    # Look for google fonts links
    font_links = re.findall(r'href="https://fonts\.googleapis\.com/[^"]+"', html)
    print("Font links found:")
    for link in font_links:
        print("  ", link)
        
    # Look for stylesheets
    stylesheets = re.findall(r'href="([^"]+\.css[^"]*)"', html)
    print("Stylesheets found:")
    for sheet in stylesheets:
        if not sheet.startswith('http'):
            sheet = "https://sprints.ai" + (sheet if sheet.startswith('/') else '/' + sheet)
        print("  ", sheet)
        # Let's fetch the stylesheet to see if it has font-family
        css_content = get_page(sheet)
        if css_content:
            font_families = re.findall(r'font-family\s*:\s*([^;\}]+)', css_content)
            if font_families:
                print("    Font families in CSS:")
                for ff in set(font_families[:10]):
                    print("      ", ff.strip())
            
            # Let's check text-align and general overrides
            alignments = re.findall(r'text-align\s*:\s*([^;\}]+)', css_content)
            if alignments:
                print("    Text alignments in CSS (first 5):")
                for al in set(alignments[:5]):
                    print("      ", al.strip())
else:
    print("Failed to fetch HTML")
