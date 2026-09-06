import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=22 to v=23
    html = html.replace("styles.css?v=22", "styles.css?v=23")
    html = html.replace("lang.js?v=22", "lang.js?v=23")
    html = html.replace("main.js?v=22", "main.js?v=23")
    html = html.replace("assets/hero_bg.jpg?v=22", "assets/hero_bg.jpg?v=23")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=23 in all HTML files successfully!")
