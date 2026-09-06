import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=40 to v=41
    html = html.replace("styles.css?v=40", "styles.css?v=41")
    html = html.replace("lang.js?v=40", "lang.js?v=41")
    html = html.replace("main.js?v=40", "main.js?v=41")
    html = html.replace("assets/hero_bg.jpg?v=40", "assets/hero_bg.jpg?v=41")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=41 in all HTML files successfully!")
