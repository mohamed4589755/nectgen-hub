import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=65 to v=66
    html = html.replace("styles.css?v=65", "styles.css?v=66")
    html = html.replace("lang.js?v=65", "lang.js?v=66")
    html = html.replace("main.js?v=65", "main.js?v=66")
    html = html.replace("assets/hero_bg.jpg?v=65", "assets/hero_bg.jpg?v=66")
    html = html.replace("bootcamp_data_analytics.png?v=65", "bootcamp_data_analytics.png?v=66")
    html = html.replace("bootcamp_ai_ml.png?v=65", "bootcamp_ai_ml.png?v=66")
    html = html.replace("bootcamp_flutter.png?v=65", "bootcamp_flutter.png?v=66")
    html = html.replace("bootcamp_frontend.png?v=65", "bootcamp_frontend.png?v=66")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=66 in all HTML files successfully!")
