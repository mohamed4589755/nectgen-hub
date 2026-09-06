import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=20 to v=21
    html = html.replace("styles.css?v=20", "styles.css?v=21")
    html = html.replace("lang.js?v=20", "lang.js?v=21")
    html = html.replace("main.js?v=20", "main.js?v=21")
    html = html.replace("assets/hero_bg.jpg?v=20", "assets/hero_bg.jpg?v=21")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=21 in all HTML files successfully!")
