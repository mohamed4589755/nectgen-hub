import glob

# The HTML block to remove
cv_html_block = """                <div class="form-group">
                    <label for="cvLink" data-i18n="form_cv_label">Resume Link (Google Drive/Dropbox)</label>
                    <input type="url" id="cvLink" required placeholder="https://drive.google.com/...">
                </div>"""

# The JS property to remove or modify
cv_js_property = "                    cv: document.getElementById('cvLink').value,"

for filepath in ["internships.html", "bootcamps.html", "diplomas.html"]:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Remove HTML field
    if cv_html_block in content:
        content = content.replace(cv_html_block, "")
        print(f"Removed CV HTML block from {filepath}")
    else:
        # Try replacing with flexible whitespaces/newlines just in case
        import re
        pattern = r'\s*<div class="form-group">\s*<label for="cvLink".*?</div>'
        content, count = re.subn(pattern, "", content, flags=re.DOTALL)
        if count > 0:
            print(f"Removed CV HTML block (regex) from {filepath}")
        else:
            print(f"Warning: CV HTML block not found in {filepath}!")

    # Remove Javascript property
    if cv_js_property in content:
        content = content.replace(cv_js_property, "")
        print(f"Removed CV JS property from {filepath}")
    else:
        # Try regex replace for JS property
        import re
        pattern = r'\s*cv:\s*document\.getElementById\(\'cvLink\'\)\.value,?'
        content, count = re.subn(pattern, "", content)
        if count > 0:
            print(f"Removed CV JS property (regex) from {filepath}")
        else:
            print(f"Warning: CV JS property not found in {filepath}!")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("CV field removal completed successfully!")
