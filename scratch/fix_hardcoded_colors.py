# Update styles.css
with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

css = css.replace("\r\n", "\n")

# Replace hardcoded hover state of primary button
css = css.replace("background: #0077ED;", "background: #1256be;")

# Replace other RGB representations of old Apple blue
css = css.replace("rgba(0, 113, 227", "rgba(22, 99, 217")

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("styles.css hardcoded colors updated successfully!")
