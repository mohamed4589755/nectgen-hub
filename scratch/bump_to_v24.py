import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=23 to v=24
    html = html.replace("styles.css?v=23", "styles.css?v=24")
    html = html.replace("lang.js?v=23", "lang.js?v=24")
    html = html.replace("main.js?v=23", "main.js?v=24")
    html = html.replace("assets/hero_bg.jpg?v=23", "assets/hero_bg.jpg?v=24")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=24 in all HTML files successfully!")
