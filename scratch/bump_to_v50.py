import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=49 to v=50
    html = html.replace("styles.css?v=49", "styles.css?v=50")
    html = html.replace("lang.js?v=49", "lang.js?v=50")
    html = html.replace("main.js?v=49", "main.js?v=50")
    html = html.replace("assets/hero_bg.jpg?v=49", "assets/hero_bg.jpg?v=50")
    html = html.replace("bootcamp_data_analytics.png?v=49", "bootcamp_data_analytics.png?v=50")
    html = html.replace("bootcamp_ai_ml.png?v=49", "bootcamp_ai_ml.png?v=50")
    html = html.replace("bootcamp_flutter.png?v=49", "bootcamp_flutter.png?v=50")
    html = html.replace("bootcamp_frontend.png?v=49", "bootcamp_frontend.png?v=50")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=50 in all HTML files successfully!")
