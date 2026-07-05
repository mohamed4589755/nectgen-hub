import os
import re

html_dir = r"C:\NextGen Hub Website"
files = ["index.html", "internships.html", "bootcamps.html", "diplomas.html", "about.html", "contact.html"]

for filename in files:
    filepath = os.path.join(html_dir, filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    # We replace the social-links container block. 
    # To handle potential differences in spacing/style tags:
    # Target footer:
    footer_target = r'<div class="social-links" style="margin-top: 16px;">\s*<a href="https://www\.linkedin\.com/company/nextgen-datahub/" class="social-icon" aria-label="LinkedIn" target="_blank">in</a>\s*<a href="[^"]*" class="social-icon" aria-label="GitHub">git</a>\s*</div>'
    footer_replacement = '''<div class="social-links" style="margin-top: 16px;">
                    <a href="https://www.linkedin.com/company/nextgen-datahub/" class="social-icon" aria-label="LinkedIn" target="_blank">in</a>
                    <a href="#" class="social-icon" aria-label="Facebook" target="_blank">fb</a>
                    <a href="#" class="social-icon" aria-label="Instagram" target="_blank">ig</a>
                    <a href="#" class="social-icon" aria-label="GitHub">git</a>
                </div>'''
                
    content = re.sub(footer_target, footer_replacement, content)
    
    # Target sidebar (for contact.html):
    sidebar_target = r'<div class="social-links">\s*<a href="https://www\.linkedin\.com/company/nextgen-datahub/" class="social-icon" aria-label="LinkedIn" target="_blank">in</a>\s*<a href="[^"]*" class="social-icon" aria-label="GitHub">git</a>\s*</div>'
    sidebar_replacement = '''<div class="social-links">
                        <a href="https://www.linkedin.com/company/nextgen-datahub/" class="social-icon" aria-label="LinkedIn" target="_blank">in</a>
                        <a href="#" class="social-icon" aria-label="Facebook" target="_blank">fb</a>
                        <a href="#" class="social-icon" aria-label="Instagram" target="_blank">ig</a>
                        <a href="#" class="social-icon" aria-label="GitHub">git</a>
                    </div>'''
                    
    content = re.sub(sidebar_target, sidebar_replacement, content)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Added Facebook and Instagram placeholders to {filename}")

# Also update the templates inside scratch/translate_html.py
translate_script = os.path.join(html_dir, "scratch", "translate_html.py")
if os.path.exists(translate_script):
    with open(translate_script, "r", encoding="utf-8") as f:
        ts_content = f.read()
        
    ts_content = re.sub(footer_target, footer_replacement, ts_content)
    ts_content = re.sub(sidebar_target, sidebar_replacement, ts_content)
    
    with open(translate_script, "w", encoding="utf-8") as f:
        f.write(ts_content)
    print("Updated templates in translate_html.py")
