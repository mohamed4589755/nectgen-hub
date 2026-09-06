import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=12 to v=13
    html = html.replace("styles.css?v=12", "styles.css?v=13")
    html = html.replace("lang.js?v=12", "lang.js?v=13")
    html = html.replace("main.js?v=12", "main.js?v=13")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=13 in all HTML files successfully!")
