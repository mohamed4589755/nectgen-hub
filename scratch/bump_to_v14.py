import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=13 to v=14
    html = html.replace("styles.css?v=13", "styles.css?v=14")
    html = html.replace("lang.js?v=13", "lang.js?v=14")
    html = html.replace("main.js?v=13", "main.js?v=14")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=14 in all HTML files successfully!")
