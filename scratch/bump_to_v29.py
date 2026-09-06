import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=28 to v=29
    html = html.replace("styles.css?v=28", "styles.css?v=29")
    html = html.replace("lang.js?v=28", "lang.js?v=29")
    html = html.replace("main.js?v=28", "main.js?v=29")
    html = html.replace("assets/hero_bg.jpg?v=28", "assets/hero_bg.jpg?v=29")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=29 in all HTML files successfully!")
