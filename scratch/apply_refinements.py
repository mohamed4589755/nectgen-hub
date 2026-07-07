import glob

def apply_refinements():
    # Update CSS
    with open("styles.css", "r", encoding="utf-8") as f:
        css = f.read()
        
    css = css.replace('--accent-blue: #0071E3;', '--accent-blue: #1E6BFF;')
    css = css.replace('--accent-cyan: #0071E3;', '--accent-cyan: #1E6BFF;')
    css = css.replace('--text-main: #1D1D1F;', '--text-main: #1F1F1F;')
    
    with open("styles.css", "w", encoding="utf-8") as f:
        f.write(css)

    # Update HTML files
    for filepath in glob.glob("*.html"):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        content = content.replace('src="assets/icon.png"', 'src="assets/icon.svg"')
        # Update inline styles for logo text color just in case it had hardcoded #1D1D1F
        content = content.replace('color: #1D1D1F;', 'color: var(--text-main);')
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
            
    print("Refinements applied successfully!")

apply_refinements()
