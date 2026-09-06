import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=68 to v=69
    html = html.replace("styles.css?v=68", "styles.css?v=69")
    html = html.replace("lang.js?v=68", "lang.js?v=69")
    html = html.replace("main.js?v=68", "main.js?v=69")
    html = html.replace("assets/hero_bg.jpg?v=68", "assets/hero_bg.jpg?v=69")
    html = html.replace("bootcamp_data_analytics.png?v=68", "bootcamp_data_analytics.png?v=69")
    html = html.replace("bootcamp_ai_ml.png?v=68", "bootcamp_ai_ml.png?v=69")
    html = html.replace("bootcamp_flutter.png?v=68", "bootcamp_flutter.png?v=69")
    html = html.replace("bootcamp_frontend.png?v=68", "bootcamp_frontend.png?v=69")
    html = html.replace("diploma_frontend.png?v=68", "diploma_frontend.png?v=69")
    html = html.replace("diploma_flutter.png?v=68", "diploma_flutter.png?v=69")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=69 in all HTML files successfully!")
