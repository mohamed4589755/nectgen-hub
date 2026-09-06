import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=21 to v=22
    html = html.replace("styles.css?v=21", "styles.css?v=22")
    html = html.replace("lang.js?v=21", "lang.js?v=22")
    html = html.replace("main.js?v=21", "main.js?v=22")
    html = html.replace("assets/hero_bg.jpg?v=21", "assets/hero_bg.jpg?v=22")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=22 in all HTML files successfully!")
