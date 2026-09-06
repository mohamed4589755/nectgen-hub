import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=50 to v=51
    html = html.replace("styles.css?v=50", "styles.css?v=51")
    html = html.replace("lang.js?v=50", "lang.js?v=51")
    html = html.replace("main.js?v=50", "main.js?v=51")
    html = html.replace("assets/hero_bg.jpg?v=50", "assets/hero_bg.jpg?v=51")
    html = html.replace("bootcamp_data_analytics.png?v=50", "bootcamp_data_analytics.png?v=51")
    html = html.replace("bootcamp_ai_ml.png?v=50", "bootcamp_ai_ml.png?v=51")
    html = html.replace("bootcamp_flutter.png?v=50", "bootcamp_flutter.png?v=51")
    html = html.replace("bootcamp_frontend.png?v=50", "bootcamp_frontend.png?v=51")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=51 in all HTML files successfully!")
