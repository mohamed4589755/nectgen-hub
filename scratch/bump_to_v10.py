import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=9 to v=10
    html = html.replace("styles.css?v=9", "styles.css?v=10")
    html = html.replace("lang.js?v=9", "lang.js?v=10")
    html = html.replace("main.js?v=9", "main.js?v=10")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=10 in all HTML files successfully!")
