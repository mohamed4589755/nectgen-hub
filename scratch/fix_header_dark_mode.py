with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Let's add the header overrides inside the dark theme styles section in styles.css
header_dark_styles = """
/* Header overrides for dark theme */
body.dark-theme header {
    background: rgba(10, 10, 12, 0.75) !important;
}
body.dark-theme header.scrolled {
    background: rgba(10, 10, 12, 0.85) !important;
}
body.dark-theme .nav-link {
    color: #A0A0A5 !important;
}
body.dark-theme .nav-link:hover, body.dark-theme .nav-link.active {
    color: #FFFFFF !important;
}
"""

# Let's append this to the end of styles.css
if "body.dark-theme header" not in css:
    css += header_dark_styles

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("styles.css updated with header dark theme overrides!")
