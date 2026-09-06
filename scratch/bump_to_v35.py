import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=34 to v=35
    html = html.replace("styles.css?v=34", "styles.css?v=35")
    html = html.replace("lang.js?v=34", "lang.js?v=35")
    html = html.replace("main.js?v=34", "main.js?v=35")
    html = html.replace("assets/hero_bg.jpg?v=34", "assets/hero_bg.jpg?v=35")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=35 in all HTML files successfully!")
