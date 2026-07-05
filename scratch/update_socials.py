import os
import re

html_dir = r"C:\NextGen Hub Website"
files = ["index.html", "internships.html", "bootcamps.html", "diplomas.html", "about.html", "contact.html"]

linkedin_url = "https://www.linkedin.com/company/nextgen-datahub/"

for filename in files:
    filepath = os.path.join(html_dir, filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    # 1. Update LinkedIn link (replace '#' in aria-label="LinkedIn" href)
    # Target: <a href="#" class="social-icon" aria-label="LinkedIn">in</a>
    # Or variations with spaces
    linkedin_pattern = r'<a href="[^"]*"\s+class="social-icon"\s+aria-label="LinkedIn">in</a>'
    linkedin_replacement = f'<a href="{linkedin_url}" class="social-icon" aria-label="LinkedIn" target="_blank">in</a>'
    content = re.sub(linkedin_pattern, linkedin_replacement, content)
    
    # 2. Remove Twitter/X link
    # Target: <a href="#" class="social-icon" aria-label="Twitter">𝕏</a>
    twitter_pattern = r'\s*<a href="[^"]*"\s+class="social-icon"\s+aria-label="Twitter">𝕏</a>'
    content = re.sub(twitter_pattern, '', content)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Updated social links in {filename}")

# Also update the templates inside scratch/translate_html.py so they stay synchronized in case we re-run it
translate_script = os.path.join(html_dir, "scratch", "translate_html.py")
if os.path.exists(translate_script):
    with open(translate_script, "r", encoding="utf-8") as f:
        ts_content = f.read()
        
    # Do the same regex replacements in the templates python script
    ts_content = re.sub(linkedin_pattern, linkedin_replacement, ts_content)
    ts_content = re.sub(twitter_pattern, '', ts_content)
    
    with open(translate_script, "w", encoding="utf-8") as f:
        f.write(ts_content)
    print("Updated templates in translate_html.py")
