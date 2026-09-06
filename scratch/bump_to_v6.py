import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=5 to v=6
    html = html.replace("styles.css?v=5", "styles.css?v=6")
    html = html.replace("lang.js?v=5", "lang.js?v=6")
    html = html.replace("main.js?v=5", "main.js?v=6")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=6 in all HTML files successfully!")
