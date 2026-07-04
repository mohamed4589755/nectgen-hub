import os
import re

html_dir = r"C:\NextGen Hub Website"
files = ["index.html", "internships.html", "bootcamps.html", "about.html", "contact.html"]

# 1. Clean up index.html (remove Diplomas Section)
index_path = os.path.join(html_dir, "index.html")
if os.path.exists(index_path):
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # We want to remove from <!-- Professional Diplomas Section --> to <!-- Call to Action -->
    pattern = r"<!-- Professional Diplomas Section -->.*?<!-- Call to Action -->"
    content_new = re.sub(pattern, "<!-- Call to Action -->", content, flags=re.DOTALL)
    
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content_new)
    print("Removed Diplomas section from index.html")

# 2. Clean up bootcamps.html (remove Diplomas Section)
bootcamps_path = os.path.join(html_dir, "bootcamps.html")
if os.path.exists(bootcamps_path):
    with open(bootcamps_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    pattern = r"<!-- Professional Diplomas Section -->.*?<!-- FAQ Section -->"
    content_new = re.sub(pattern, "<!-- FAQ Section -->", content, flags=re.DOTALL)
    
    with open(bootcamps_path, "w", encoding="utf-8") as f:
        f.write(content_new)
    print("Removed Diplomas section from bootcamps.html")

# 3. Update Nav Menu and Footer in all files
for filename in files:
    filepath = os.path.join(html_dir, filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    # --- Update Nav Menu ---
    # We find the <ul class="nav-menu" id="navMenu">...</ul> and replace it
    # We determine which link should be active based on current file
    active_class = {
        "index.html": ("active", "", "", "", ""),
        "internships.html": ("", "active", "", "", ""),
        "bootcamps.html": ("", "", "active", "", ""),
        "about.html": ("", "", "", "active", ""),
        "contact.html": ("", "", "", "", "active")
    }
    
    act = active_class[filename]
    
    nav_pattern = r'<ul class="nav-menu" id="navMenu">.*?</ul>'
    nav_replacement = f'''<ul class="nav-menu" id="navMenu">
                <li><a href="index.html" class="nav-link {act[0]}" id="navIndex">Home</a></li>
                <li><a href="internships.html" class="nav-link {act[1]}" id="navInternships">Internships</a></li>
                <li><a href="bootcamps.html" class="nav-link {act[2]}" id="navBootcamps">Bootcamps</a></li>
                <li><a href="diplomas.html" class="nav-link" id="navDiplomas">Diplomas</a></li>
                <li><a href="about.html" class="nav-link {act[3]}" id="navAbout">About Us</a></li>
                <li><a href="contact.html" class="nav-link {act[4]}" id="navContact">Contact</a></li>
            </ul>'''
            
    content = re.sub(nav_pattern, nav_replacement, content, flags=re.DOTALL)
    
    # --- Update Footer Quick Links ---
    footer_pattern = r'<div class="footer-nav">\s*<h4 class="footer-nav-title">Quick Links</h4>.*?</div>'
    footer_replacement = '''<div class="footer-nav">
                <h4 class="footer-nav-title">Quick Links</h4>
                <a href="index.html" id="footerNavHome">Home</a>
                <a href="internships.html" id="footerNavInternships">Internship Listings</a>
                <a href="bootcamps.html" id="footerNavBootcamps">Summer Bootcamps</a>
                <a href="diplomas.html" id="footerNavDiplomas">Professional Diplomas</a>
            </div>'''
            
    content = re.sub(footer_pattern, footer_replacement, content, flags=re.DOTALL)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Updated nav and footer in {filename}")
