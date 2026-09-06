import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=29 to v=30
    html = html.replace("styles.css?v=29", "styles.css?v=30")
    html = html.replace("lang.js?v=29", "lang.js?v=30")
    html = html.replace("main.js?v=29", "main.js?v=30")
    html = html.replace("assets/hero_bg.jpg?v=29", "assets/hero_bg.jpg?v=30")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=30 in all HTML files successfully!")
