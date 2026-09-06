# Update styles.css
with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

css = css.replace("\r\n", "\n")

# 1. Update .gradient-text block
old_gradient_text = """.gradient-text {
    color: var(--accent-blue); /* Solid blue color instead of a low-contrast gradient */
    background: none;
    -webkit-background-clip: initial;
    -webkit-text-fill-color: initial;
}"""

new_gradient_text = """.gradient-text {
    background: linear-gradient(135deg, var(--accent-blue) 0%, var(--accent-cyan) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    display: inline-block;
}"""

css = css.replace(old_gradient_text, new_gradient_text)

# 2. Update .section-tag color
css = css.replace(
    "color: var(--accent-blue); /* Muted tags */",
    "color: var(--accent-cyan); /* fresh leaf green tags */"
)

# 3. Update .tag-highlight colors
old_tag_highlight = """.tag-highlight {
    background: rgba(22, 99, 217, 0.1);
    color: var(--accent-blue);
}"""

new_tag_highlight = """.tag-highlight {
    background: rgba(142, 191, 84, 0.15);
    color: var(--accent-cyan);
}"""

css = css.replace(old_tag_highlight, new_tag_highlight)

# 4. Update .scroll-progress background
css = css.replace(
    "background: var(--accent-blue);",
    "background: linear-gradient(to right, var(--accent-blue), var(--accent-cyan));"
)

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("styles.css updated with visible green elements successfully!")
