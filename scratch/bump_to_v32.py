import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=31 to v=32
    html = html.replace("styles.css?v=31", "styles.css?v=32")
    html = html.replace("lang.js?v=31", "lang.js?v=32")
    html = html.replace("main.js?v=31", "main.js?v=32")
    html = html.replace("assets/hero_bg.jpg?v=31", "assets/hero_bg.jpg?v=32")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=32 in all HTML files successfully!")
