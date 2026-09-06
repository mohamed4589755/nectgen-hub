import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Bump from v=41 to v=42
    html = html.replace("styles.css?v=41", "styles.css?v=42")
    html = html.replace("lang.js?v=41", "lang.js?v=42")
    html = html.replace("main.js?v=41", "main.js?v=42")
    html = html.replace("assets/hero_bg.jpg?v=41", "assets/hero_bg.jpg?v=42")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache version bumped to v=42 in all HTML files successfully!")
