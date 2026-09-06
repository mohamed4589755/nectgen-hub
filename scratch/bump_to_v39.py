import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=38 to v=39
    html = html.replace("styles.css?v=38", "styles.css?v=39")
    html = html.replace("lang.js?v=38", "lang.js?v=39")
    html = html.replace("main.js?v=38", "main.js?v=39")
    html = html.replace("assets/hero_bg.jpg?v=38", "assets/hero_bg.jpg?v=39")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=39 in all HTML files successfully!")
