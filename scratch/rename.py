import os
import glob
import re

def update_files():
    html_files = glob.glob("*.html")
    js_files = glob.glob("*.js")
    css_file = "styles.css"
    
    # Update CSS
    with open(css_file, "r", encoding="utf-8") as f:
        css = f.read()
    if 'gap: 12px;' not in css.split('.logo {')[1][:100]:
        css = css.replace('.logo {\n    font-size: 1.25rem;\n    font-weight: 600;\n    letter-spacing: -0.02em;\n    display: flex;\n    align-items: center;',
                          '.logo {\n    font-size: 1.25rem;\n    font-weight: 600;\n    letter-spacing: -0.02em;\n    display: flex;\n    align-items: center;\n    gap: 12px;')
    # Hide underline on logo hover for the text specifically, or let it be. The user might want hover effect.
    css = css.replace('NextGen Hub', 'NextGen Institute')
    with open(css_file, "w", encoding="utf-8") as f:
        f.write(css)

    # Old logo pattern to replace
    old_logo_pattern = re.compile(r'<img src="assets/logo\.png"[^>]*>')
    new_logo_html = """<img src="assets/icon.png" alt="NextGen Institute Logo" class="logo-img" height="100" style="height: 100px; width: auto;">
                <span class="logo-text" style="font-size: 1.8rem; font-weight: 800; color: var(--text-main); letter-spacing: -0.03em; text-decoration: none;">NextGen <span style="color: var(--accent-blue);">Institute</span></span>"""
    
    # Old footer logo pattern (might have different indentation)
    new_logo_footer = """<img src="assets/icon.png" alt="NextGen Institute Logo" class="logo-img" height="100" style="height: 100px; width: auto;">
                    <span class="logo-text" style="font-size: 1.8rem; font-weight: 800; color: var(--text-dark); letter-spacing: -0.03em; text-decoration: none;">NextGen <span style="color: var(--accent-blue);">Institute</span></span>"""

    # We need to distinguish header logo vs footer logo because the footer background is dark!
    # In footer, var(--text-main) is dark. We should use var(--text-dark) which is white!
    
    for fpath in html_files + js_files:
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Replace text
        content = content.replace("NextGen Hub", "NextGen Institute")
        content = content.replace("NextGenHub", "NextGenInstitute")
        content = content.replace("nextgenhub", "nextgeninstitute")
        content = content.replace("nextgen-datahub", "nextgen-institute")
        
        # Replace logo tags carefully
        # In header:
        content = re.sub(
            r'(<header>[\s\S]*?)<img src="assets/logo\.png"[^>]*>',
            lambda m: m.group(1) + new_logo_html,
            content
        )
        # In footer (or anywhere else):
        content = re.sub(
            r'(<footer[\s\S]*?)<img src="assets/logo\.png"[^>]*>',
            lambda m: m.group(1) + new_logo_footer,
            content
        )
        
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)

    print("All files renamed and updated successfully!")

if __name__ == "__main__":
    update_files()
