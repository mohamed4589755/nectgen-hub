import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump the cache-busting version from v=4 to v=5
    html = html.replace("styles.css?v=4", "styles.css?v=5")
    html = html.replace("lang.js?v=4", "lang.js?v=5")
    html = html.replace("main.js?v=4", "main.js?v=5")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache-busting version bumped to v=5 in all HTML files successfully!")
