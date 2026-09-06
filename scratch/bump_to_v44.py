import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=43 to v=44
    html = html.replace("styles.css?v=43", "styles.css?v=44")
    html = html.replace("lang.js?v=43", "lang.js?v=44")
    html = html.replace("main.js?v=43", "main.js?v=44")
    html = html.replace("assets/hero_bg.jpg?v=43", "assets/hero_bg.jpg?v=44")
    
    with open(filepath, "w", encoding="utf-8") as f:
        html = f.write(html)

print("Cache version bumped to v=44 in all HTML files successfully!")
