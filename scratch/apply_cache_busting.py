import glob

head_script = """    <link rel="stylesheet" href="styles.css?v=4">
    <script>
        if (localStorage.getItem('selectedTheme') === 'dark') {
            document.documentElement.classList.add('dark-theme');
        }
    </script>"""

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # 1. Replace styles.css link with cache-busting and instant theme check
    # Check both styles.css and styles.css?v=...
    html = html.replace('<link rel="stylesheet" href="styles.css">', head_script)
    
    # 2. Replace lang.js and main.js script tags
    html = html.replace('<script src="lang.js"></script>', '<script src="lang.js?v=4"></script>')
    html = html.replace('<script src="main.js"></script>', '<script src="main.js?v=4"></script>')
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("Cache busting and head script injected into all HTML files successfully!")
