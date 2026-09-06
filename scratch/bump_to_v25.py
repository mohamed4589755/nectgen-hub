import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=24 to v=25
    html = html.replace("styles.css?v=24", "styles.css?v=25")
    html = html.replace("lang.js?v=24", "lang.js?v=25")
    html = html.replace("main.js?v=24", "main.js?v=25")
    html = html.replace("assets/hero_bg.jpg?v=24", "assets/hero_bg.jpg?v=25")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=25 in all HTML files successfully!")
