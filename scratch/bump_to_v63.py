import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=62 to v=63
    html = html.replace("styles.css?v=62", "styles.css?v=63")
    html = html.replace("lang.js?v=62", "lang.js?v=63")
    html = html.replace("main.js?v=62", "main.js?v=63")
    html = html.replace("assets/hero_bg.jpg?v=62", "assets/hero_bg.jpg?v=63")
    html = html.replace("bootcamp_data_analytics.png?v=62", "bootcamp_data_analytics.png?v=63")
    html = html.replace("bootcamp_ai_ml.png?v=62", "bootcamp_ai_ml.png?v=63")
    html = html.replace("bootcamp_flutter.png?v=62", "bootcamp_flutter.png?v=63")
    html = html.replace("bootcamp_frontend.png?v=62", "bootcamp_frontend.png?v=63")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=63 in all HTML files successfully!")
