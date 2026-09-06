import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=11 to v=12
    html = html.replace("styles.css?v=11", "styles.css?v=12")
    html = html.replace("lang.js?v=11", "lang.js?v=12")
    html = html.replace("main.js?v=11", "main.js?v=12")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=12 in all HTML files successfully!")
