import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=32 to v=33
    html = html.replace("styles.css?v=32", "styles.css?v=33")
    html = html.replace("lang.js?v=32", "lang.js?v=33")
    html = html.replace("main.js?v=32", "main.js?v=33")
    html = html.replace("assets/hero_bg.jpg?v=32", "assets/hero_bg.jpg?v=33")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=33 in all HTML files successfully!")
