import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=71 to v=72
    html = html.replace("styles.css?v=71", "styles.css?v=72")
    html = html.replace("lang.js?v=71", "lang.js?v=72")
    html = html.replace("main.js?v=71", "main.js?v=72")
    html = html.replace("assets/hero_bg.jpg?v=71", "assets/hero_bg.jpg?v=72")
    html = html.replace("bootcamp_data_analytics.png?v=71", "bootcamp_data_analytics.png?v=72")
    html = html.replace("bootcamp_ai_ml.png?v=71", "bootcamp_ai_ml.png?v=72")
    html = html.replace("bootcamp_flutter.png?v=71", "bootcamp_flutter.png?v=72")
    html = html.replace("bootcamp_frontend.png?v=71", "bootcamp_frontend.png?v=72")
    html = html.replace("diploma_frontend.png?v=71", "diploma_frontend.png?v=72")
    html = html.replace("diploma_flutter.png?v=71", "diploma_flutter.png?v=72")
    html = html.replace("diploma_data_analytics.png?v=71", "diploma_data_analytics.png?v=72")
    html = html.replace("diploma_ai_ml.png?v=71", "diploma_ai_ml.png?v=72")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=72 in all HTML files successfully!")
