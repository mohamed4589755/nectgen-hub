import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=18 to v=19
    html = html.replace("styles.css?v=18", "styles.css?v=19")
    html = html.replace("lang.js?v=18", "lang.js?v=19")
    html = html.replace("main.js?v=18", "main.js?v=19")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=19 in all HTML files successfully!")
