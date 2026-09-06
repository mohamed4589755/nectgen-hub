import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=36 to v=37
    html = html.replace("styles.css?v=36", "styles.css?v=37")
    html = html.replace("lang.js?v=36", "lang.js?v=37")
    html = html.replace("main.js?v=36", "main.js?v=37")
    html = html.replace("assets/hero_bg.jpg?v=36", "assets/hero_bg.jpg?v=37")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=37 in all HTML files successfully!")
