import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=14 to v=15
    html = html.replace("styles.css?v=14", "styles.css?v=15")
    html = html.replace("lang.js?v=14", "lang.js?v=15")
    html = html.replace("main.js?v=14", "main.js?v=15")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=15 in all HTML files successfully!")
