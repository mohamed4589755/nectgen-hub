import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=51 to v=52
    html = html.replace("styles.css?v=51", "styles.css?v=52")
    html = html.replace("lang.js?v=51", "lang.js?v=52")
    html = html.replace("main.js?v=51", "main.js?v=52")
    html = html.replace("assets/hero_bg.jpg?v=51", "assets/hero_bg.jpg?v=52")
    html = html.replace("bootcamp_data_analytics.png?v=51", "bootcamp_data_analytics.png?v=52")
    html = html.replace("bootcamp_ai_ml.png?v=51", "bootcamp_ai_ml.png?v=52")
    html = html.replace("bootcamp_flutter.png?v=51", "bootcamp_flutter.png?v=52")
    html = html.replace("bootcamp_frontend.png?v=51", "bootcamp_frontend.png?v=52")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=52 in all HTML files successfully!")
