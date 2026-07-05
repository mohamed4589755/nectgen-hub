import os

filepath = r"C:\NextGen Hub Website\scratch\translate_html.py"
if os.path.exists(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    old_tag = '<textarea id="message" class="form-control" data-i18n-placeholder="contact_form_message" placeholder="Tell us about your background or inquiry details..." required></textarea>'
    new_tag = '<textarea id="message" class="form-control" data-i18n-placeholder="contact_form_message" placeholder="Tell us about your background or inquiry details..."></textarea>'
    
    if old_tag in content:
        content = content.replace(old_tag, new_tag)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated template in translate_html.py")
    else:
        print("Tag not found in translate_html.py template, probably already updated or not defined there.")
