import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=64 to v=65
    html = html.replace("styles.css?v=64", "styles.css?v=65")
    html = html.replace("lang.js?v=64", "lang.js?v=65")
    html = html.replace("main.js?v=64", "main.js?v=65")
    html = html.replace("assets/hero_bg.jpg?v=64", "assets/hero_bg.jpg?v=65")
    html = html.replace("bootcamp_data_analytics.png?v=64", "bootcamp_data_analytics.png?v=65")
    html = html.replace("bootcamp_ai_ml.png?v=64", "bootcamp_ai_ml.png?v=65")
    html = html.replace("bootcamp_flutter.png?v=64", "bootcamp_flutter.png?v=65")
    html = html.replace("bootcamp_frontend.png?v=64", "bootcamp_frontend.png?v=65")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=65 in all HTML files successfully!")
