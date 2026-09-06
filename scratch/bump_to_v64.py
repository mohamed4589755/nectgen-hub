import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=63 to v=64
    html = html.replace("styles.css?v=63", "styles.css?v=64")
    html = html.replace("lang.js?v=63", "lang.js?v=64")
    html = html.replace("main.js?v=63", "main.js?v=64")
    html = html.replace("assets/hero_bg.jpg?v=63", "assets/hero_bg.jpg?v=64")
    html = html.replace("bootcamp_data_analytics.png?v=63", "bootcamp_data_analytics.png?v=64")
    html = html.replace("bootcamp_ai_ml.png?v=63", "bootcamp_ai_ml.png?v=64")
    html = html.replace("bootcamp_flutter.png?v=63", "bootcamp_flutter.png?v=64")
    html = html.replace("bootcamp_frontend.png?v=63", "bootcamp_frontend.png?v=64")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=64 in all HTML files successfully!")
