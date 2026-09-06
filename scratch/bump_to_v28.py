import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=27 to v=28
    html = html.replace("styles.css?v=27", "styles.css?v=28")
    html = html.replace("lang.js?v=27", "lang.js?v=28")
    html = html.replace("main.js?v=27", "main.js?v=28")
    html = html.replace("assets/hero_bg.jpg?v=27", "assets/hero_bg.jpg?v=28")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=28 in all HTML files successfully!")
