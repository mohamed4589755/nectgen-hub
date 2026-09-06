import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=42 to v=43
    html = html.replace("styles.css?v=42", "styles.css?v=43")
    html = html.replace("lang.js?v=42", "lang.js?v=43")
    html = html.replace("main.js?v=42", "main.js?v=43")
    html = html.replace("assets/hero_bg.jpg?v=42", "assets/hero_bg.jpg?v=43")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=43 in all HTML files successfully!")
