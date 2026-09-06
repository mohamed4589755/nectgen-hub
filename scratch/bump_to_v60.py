import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=52 to v=60
    html = html.replace("styles.css?v=52", "styles.css?v=60")
    html = html.replace("lang.js?v=52", "lang.js?v=60")
    html = html.replace("main.js?v=52", "main.js?v=60")
    html = html.replace("assets/hero_bg.jpg?v=52", "assets/hero_bg.jpg?v=60")
    html = html.replace("bootcamp_data_analytics.png?v=52", "bootcamp_data_analytics.png?v=60")
    html = html.replace("bootcamp_ai_ml.png?v=52", "bootcamp_ai_ml.png?v=60")
    html = html.replace("bootcamp_flutter.png?v=52", "bootcamp_flutter.png?v=60")
    html = html.replace("bootcamp_frontend.png?v=52", "bootcamp_frontend.png?v=60")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=60 in all HTML files successfully!")
