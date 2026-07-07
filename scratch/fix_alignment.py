import glob

def fix_alignment():
    # Update CSS
    with open("styles.css", "r", encoding="utf-8") as f:
        css = f.read()
        
    css = css.replace('.logo {\n    font-size: 1.25rem;\n    font-weight: 600;\n    letter-spacing: -0.02em;\n    display: flex;\n    align-items: center;',
                      '.logo {\n    font-size: 1.25rem;\n    font-weight: 600;\n    letter-spacing: -0.02em;\n    display: flex;\n    flex-direction: row;\n    flex-wrap: nowrap;\n    align-items: center;')
    
    with open("styles.css", "w", encoding="utf-8") as f:
        f.write(css)

    # Update HTML files
    for filepath in glob.glob("*.html"):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        content = content.replace('text-decoration: none;">NextGen', 'text-decoration: none; white-space: nowrap;">NextGen')
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
            
    print("Alignment fixed successfully!")

fix_alignment()
