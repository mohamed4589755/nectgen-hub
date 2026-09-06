import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=35 to v=36
    html = html.replace("styles.css?v=35", "styles.css?v=36")
    html = html.replace("lang.js?v=35", "lang.js?v=36")
    html = html.replace("main.js?v=35", "main.js?v=36")
    html = html.replace("assets/hero_bg.jpg?v=35", "assets/hero_bg.jpg?v=36")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=36 in all HTML files successfully!")
