import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=46 to v=47
    html = html.replace("styles.css?v=46", "styles.css?v=47")
    html = html.replace("lang.js?v=46", "lang.js?v=47")
    html = html.replace("main.js?v=46", "main.js?v=47")
    html = html.replace("assets/hero_bg.jpg?v=46", "assets/hero_bg.jpg?v=47")
    html = html.replace("bootcamp_data_analytics.png?v=46", "bootcamp_data_analytics.png?v=47")
    html = html.replace("bootcamp_ai_ml.png?v=46", "bootcamp_ai_ml.png?v=47")
    html = html.replace("bootcamp_flutter.png?v=1", "bootcamp_flutter.png?v=47")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=47 in all HTML files successfully!")
