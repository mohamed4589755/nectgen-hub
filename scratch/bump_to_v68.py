import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=67 to v=68
    html = html.replace("styles.css?v=67", "styles.css?v=68")
    html = html.replace("lang.js?v=67", "lang.js?v=68")
    html = html.replace("main.js?v=67", "main.js?v=68")
    html = html.replace("assets/hero_bg.jpg?v=67", "assets/hero_bg.jpg?v=68")
    html = html.replace("bootcamp_data_analytics.png?v=67", "bootcamp_data_analytics.png?v=68")
    html = html.replace("bootcamp_ai_ml.png?v=67", "bootcamp_ai_ml.png?v=68")
    html = html.replace("bootcamp_flutter.png?v=67", "bootcamp_flutter.png?v=68")
    html = html.replace("bootcamp_frontend.png?v=67", "bootcamp_frontend.png?v=68")
    html = html.replace("diploma_frontend.png?v=67", "diploma_frontend.png?v=68")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=68 in all HTML files successfully!")
