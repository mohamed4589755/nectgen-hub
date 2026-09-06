import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=15 to v=16
    html = html.replace("styles.css?v=15", "styles.css?v=16")
    html = html.replace("lang.js?v=15", "lang.js?v=16")
    html = html.replace("main.js?v=15", "main.js?v=16")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=16 in all HTML files successfully!")
