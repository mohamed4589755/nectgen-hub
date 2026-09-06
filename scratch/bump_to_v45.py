import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=44 to v=45
    html = html.replace("styles.css?v=44", "styles.css?v=45")
    html = html.replace("lang.js?v=44", "lang.js?v=45")
    html = html.replace("main.js?v=44", "main.js?v=45")
    html = html.replace("assets/hero_bg.jpg?v=44", "assets/hero_bg.jpg?v=45")
    html = html.replace("bootcamp_data_analytics.png?v=1", "bootcamp_data_analytics.png?v=45")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=45 in all HTML files successfully!")
