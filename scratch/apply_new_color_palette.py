import glob

# 1. Update styles.css
with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

css = css.replace("\r\n", "\n")

# Replace variable declarations in :root
css = css.replace("--accent-blue: #1E6BFF;", "--accent-blue: #1663d9;")
css = css.replace("--accent-cyan: #1E6BFF;", "--accent-cyan: #8ebf54;")

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("styles.css updated successfully!")


# 2. Update subpage background radial-gradients in HTML files
for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    html = html.replace("\r\n", "\n")
    
    # Replace indigo/sky-blue radial gradients with royal blue from the image
    html = html.replace("rgba(99, 102, 241, 0.06)", "rgba(22, 99, 217, 0.06)")
    html = html.replace("rgba(14, 165, 233, 0.06)", "rgba(22, 99, 217, 0.06)")
    html = html.replace("rgba(99, 102, 241, 0.08)", "rgba(22, 99, 217, 0.06)")
    html = html.replace("rgba(14, 165, 233, 0.08)", "rgba(22, 99, 217, 0.06)")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

print("All HTML files' subpage gradients updated successfully!")
