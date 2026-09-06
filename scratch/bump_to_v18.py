import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=17 to v=18
    html = html.replace("styles.css?v=17", "styles.css?v=18")
    html = html.replace("lang.js?v=17", "lang.js?v=18")
    html = html.replace("main.js?v=17", "main.js?v=18")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=18 in all HTML files successfully!")
