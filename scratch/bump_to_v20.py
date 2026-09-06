import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=19 to v=20
    html = html.replace("styles.css?v=19", "styles.css?v=20")
    html = html.replace("lang.js?v=19", "lang.js?v=20")
    html = html.replace("main.js?v=19", "main.js?v=20")
    
    # Specific to index.html to break image cache
    if filepath == "index.html":
        html = html.replace('src="assets/hero_bg.jpg"', 'src="assets/hero_bg.jpg?v=20"')
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=20 in all HTML files successfully!")
