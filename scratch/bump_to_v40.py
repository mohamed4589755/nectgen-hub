import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=39 to v=40
    html = html.replace("styles.css?v=39", "styles.css?v=40")
    html = html.replace("lang.js?v=39", "lang.js?v=40")
    html = html.replace("main.js?v=39", "main.js?v=40")
    html = html.replace("assets/hero_bg.jpg?v=39", "assets/hero_bg.jpg?v=40")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=40 in all HTML files successfully!")
