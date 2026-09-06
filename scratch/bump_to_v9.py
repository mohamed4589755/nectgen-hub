import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump to v=9 for all main files
    for v in ["v=7", "v=6", "v=5", "v=4", "v=8"]:
        html = html.replace(f"styles.css?{v}", "styles.css?v=9")
        html = html.replace(f"lang.js?{v}", "lang.js?v=9")
        html = html.replace(f"main.js?{v}", "main.js?v=9")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=9 in all HTML files successfully!")
