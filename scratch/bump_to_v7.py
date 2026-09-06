import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=6 to v=7
    html = html.replace("styles.css?v=6", "styles.css?v=7")
    html = html.replace("lang.js?v=6", "lang.js?v=7")
    html = html.replace("main.js?v=6", "main.js?v=7")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=7 in all HTML files successfully!")
