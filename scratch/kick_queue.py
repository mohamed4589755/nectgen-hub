with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Add a dummy comment to kick the build queue
css += "\n/* Dummy comment to kick GitHub Actions queue */\n"

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("styles.css kicked with a dummy comment!")
