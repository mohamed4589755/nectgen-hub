import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=10 to v=11
    html = html.replace("styles.css?v=10", "styles.css?v=11")
    html = html.replace("lang.js?v=10", "lang.js?v=11")
    html = html.replace("main.js?v=10", "main.js?v=11")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=11 in all HTML files successfully!")
