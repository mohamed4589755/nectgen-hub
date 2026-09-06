import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=45 to v=46
    html = html.replace("styles.css?v=45", "styles.css?v=46")
    html = html.replace("lang.js?v=45", "lang.js?v=46")
    html = html.replace("main.js?v=45", "main.js?v=46")
    html = html.replace("assets/hero_bg.jpg?v=45", "assets/hero_bg.jpg?v=46")
    html = html.replace("bootcamp_data_analytics.png?v=45", "bootcamp_data_analytics.png?v=46")
    html = html.replace("bootcamp_ai_ml.png?v=1", "bootcamp_ai_ml.png?v=46")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=46 in all HTML files successfully!")
