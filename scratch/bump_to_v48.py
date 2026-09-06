import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=47 to v=48
    html = html.replace("styles.css?v=47", "styles.css?v=48")
    html = html.replace("lang.js?v=47", "lang.js?v=48")
    html = html.replace("main.js?v=47", "main.js?v=48")
    html = html.replace("assets/hero_bg.jpg?v=47", "assets/hero_bg.jpg?v=48")
    html = html.replace("bootcamp_data_analytics.png?v=47", "bootcamp_data_analytics.png?v=48")
    html = html.replace("bootcamp_ai_ml.png?v=47", "bootcamp_ai_ml.png?v=48")
    html = html.replace("bootcamp_flutter.png?v=47", "bootcamp_flutter.png?v=48")
    html = html.replace("bootcamp_frontend.png?v=1", "bootcamp_frontend.png?v=48")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=48 in all HTML files successfully!")
