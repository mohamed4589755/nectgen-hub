with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace the text colors in the stacked logo styles
old_top_style = """.logo-text-top {
    font-size: 1.35rem;
    font-weight: 800;
    color: var(--text-main);
    letter-spacing: -0.02em;
}"""

new_top_style = """.logo-text-top {
    font-size: 1.35rem;
    font-weight: 800;
    color: #151e26; /* Exact brand charcoal-navy color */
    letter-spacing: -0.02em;
}"""

old_bottom_style = """.logo-text-bottom {
    font-size: 1.25rem;
    font-weight: 500;
    color: var(--text-main);
    opacity: 0.85;
    letter-spacing: -0.02em;
}"""

new_bottom_style = """.logo-text-bottom {
    font-size: 1.25rem;
    font-weight: 600;
    color: #3b5772; /* Exact brand slate-blue color */
    letter-spacing: -0.02em;
}"""

css = css.replace(old_top_style, new_top_style).replace(old_bottom_style, new_bottom_style)

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("styles.css logo colors updated successfully!")
