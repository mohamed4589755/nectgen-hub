with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Locate and remove the footer specific logo overrides
old_footer_overrides = """/* Footer specific overrides for light text on dark background */
footer .logo-text-top {
    color: var(--text-dark) !important;
}
footer .logo-text-bottom {
    color: var(--text-dark) !important;
    opacity: 0.8;
}"""

css = css.replace(old_footer_overrides, "")

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Footer logo text color overrides removed from styles.css!")
