import glob

# 1. Update styles.css
with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Remove the old .logo-img block and override .logo
css = css.replace(
    ".logo {\n    font-size: 1.25rem;\n    font-weight: 600;\n    letter-spacing: -0.02em;\n    display: flex;\n    flex-direction: row;\n    flex-wrap: nowrap;\n    align-items: center;\n    gap: 12px;\n    gap: 6px;\n    color: var(--text-main);\n}",
    ""
).replace(
    ".logo-img {\n    height: 100px; /* Scaled to 100px per user request */\n    width: auto;\n    display: block;\n}",
    ""
)

new_logo_css = """
/* Refined Stacked Logo Layout */
.logo {
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 10px;
    text-decoration: none !important;
}
.logo-img {
    height: 48px !important; /* Perfect height to align with stacked text */
    width: auto;
    display: block;
    flex-shrink: 0;
}
.logo-text-wrap {
    display: flex;
    flex-direction: column;
    line-height: 1.1;
    justify-content: center;
}
.logo-text-top {
    font-size: 1.35rem;
    font-weight: 800;
    color: var(--text-main);
    letter-spacing: -0.02em;
}
.logo-text-bottom {
    font-size: 1.25rem;
    font-weight: 500;
    color: var(--text-main);
    opacity: 0.85;
    letter-spacing: -0.02em;
}

/* Footer specific overrides for light text on dark background */
footer .logo-text-top {
    color: var(--text-dark) !important;
}
footer .logo-text-bottom {
    color: var(--text-dark) !important;
    opacity: 0.8;
}
"""

if ".logo-text-wrap" not in css:
    css += new_logo_css

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("styles.css updated with new logo layout CSS!")


# 2. Update HTML files
header_pattern = """            <a href="index.html" class="logo" id="logoLink">
                <img src="assets/icon.png" alt="NextGen Institute Logo" class="logo-img" height="100" style="height: 100px; width: auto;">
                <span class="logo-text" style="font-size: 1.8rem; font-weight: 800; color: var(--text-main); letter-spacing: -0.03em; text-decoration: none; white-space: nowrap;">NextGen <span style="color: var(--accent-blue);">Institute</span></span>
            </a>"""

new_header_html = """            <a href="index.html" class="logo" id="logoLink">
                <img src="assets/icon.png" alt="NextGen Institute Logo" class="logo-img">
                <div class="logo-text-wrap">
                    <span class="logo-text-top">NextGen</span>
                    <span class="logo-text-bottom">Institute</span>
                </div>
            </a>"""

footer_pattern = """                <a href="index.html" class="logo" style="margin-bottom: 16px;">
                    <img src="assets/icon.png" alt="NextGen Institute Logo" class="logo-img" height="100" style="height: 100px; width: auto;">
                    <span class="logo-text" style="font-size: 1.8rem; font-weight: 800; color: var(--text-dark); letter-spacing: -0.03em; text-decoration: none; white-space: nowrap;">NextGen <span style="color: var(--accent-blue);">Institute</span></span>
                </a>"""

new_footer_html = """                <a href="index.html" class="logo" style="margin-bottom: 16px;">
                    <img src="assets/icon.png" alt="NextGen Institute Logo" class="logo-img">
                    <div class="logo-text-wrap">
                        <span class="logo-text-top">NextGen</span>
                        <span class="logo-text-bottom">Institute</span>
                    </div>
                </a>"""

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    content = content.replace(header_pattern, new_header_html)
    content = content.replace(footer_pattern, new_footer_html)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("All HTML files updated with new logo layout successfully!")
