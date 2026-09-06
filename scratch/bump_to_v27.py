import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=26 to v=27
    html = html.replace("styles.css?v=26", "styles.css?v=27")
    html = html.replace("lang.js?v=26", "lang.js?v=27")
    html = html.replace("main.js?v=26", "main.js?v=27")
    html = html.replace("assets/hero_bg.jpg?v=26", "assets/hero_bg.jpg?v=27")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=27 in all HTML files successfully!")
