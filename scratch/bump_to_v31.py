import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=30 to v=31
    html = html.replace("styles.css?v=30", "styles.css?v=31")
    html = html.replace("lang.js?v=30", "lang.js?v=31")
    html = html.replace("main.js?v=30", "main.js?v=31")
    html = html.replace("assets/hero_bg.jpg?v=30", "assets/hero_bg.jpg?v=31")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=31 in all HTML files successfully!")
