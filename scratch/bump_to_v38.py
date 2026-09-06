import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=37 to v=38
    html = html.replace("styles.css?v=37", "styles.css?v=38")
    html = html.replace("lang.js?v=37", "lang.js?v=38")
    html = html.replace("main.js?v=37", "main.js?v=38")
    html = html.replace("assets/hero_bg.jpg?v=37", "assets/hero_bg.jpg?v=38")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=38 in all HTML files successfully!")
