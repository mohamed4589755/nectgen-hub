import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=73 to v=74
    html = html.replace("styles.css?v=73", "styles.css?v=74")
    html = html.replace("lang.js?v=73", "lang.js?v=74")
    html = html.replace("main.js?v=73", "main.js?v=74")
    html = html.replace("assets/hero_bg.jpg?v=73", "assets/hero_bg.jpg?v=74")
    html = html.replace("bootcamp_data_analytics.png?v=73", "bootcamp_data_analytics.png?v=74")
    html = html.replace("bootcamp_ai_ml.png?v=73", "bootcamp_ai_ml.png?v=74")
    html = html.replace("bootcamp_flutter.png?v=73", "bootcamp_flutter.png?v=74")
    html = html.replace("bootcamp_frontend.png?v=73", "bootcamp_frontend.png?v=74")
    html = html.replace("diploma_frontend.png?v=73", "diploma_frontend.png?v=74")
    html = html.replace("diploma_flutter.png?v=73", "diploma_flutter.png?v=74")
    html = html.replace("diploma_data_analytics.png?v=73", "diploma_data_analytics.png?v=74")
    html = html.replace("diploma_ai_ml.png?v=73", "diploma_ai_ml.png?v=74")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=74 in all HTML files successfully!")
