import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=25 to v=26
    html = html.replace("styles.css?v=25", "styles.css?v=26")
    html = html.replace("lang.js?v=25", "lang.js?v=26")
    html = html.replace("main.js?v=25", "main.js?v=26")
    html = html.replace("assets/hero_bg.jpg?v=25", "assets/hero_bg.jpg?v=26")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=26 in all HTML files successfully!")
