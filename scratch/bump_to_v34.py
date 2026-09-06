import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=33 to v=34
    html = html.replace("styles.css?v=33", "styles.css?v=34")
    html = html.replace("lang.js?v=33", "lang.js?v=34")
    html = html.replace("main.js?v=33", "main.js?v=34")
    html = html.replace("assets/hero_bg.jpg?v=33", "assets/hero_bg.jpg?v=34")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=34 in all HTML files successfully!")
