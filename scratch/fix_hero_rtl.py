import os

html_dir = r"C:\NextGen Hub Website"
files = ["index.html", "internships.html", "bootcamps.html", "diplomas.html", "about.html", "contact.html"]

for filename in files:
    filepath = os.path.join(html_dir, filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Remove the inline "text-align: left;" from the section tag
    content = content.replace('text-align: left; background:', 'background:')
    content = content.replace('text-align: left; background-image:', 'background-image:')
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Fixed RTL inline overrides in {filename}")
