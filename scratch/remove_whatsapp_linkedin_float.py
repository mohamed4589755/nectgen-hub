import glob

# 1. Update HTML files (Remove WhatsApp from footers)
wa_footer_block = """                <a href="https://wa.me/201206751361" class="social-icon" aria-label="WhatsApp" target="_blank">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M17.49 15.3c-.3-.15-1.78-.88-2.05-.98-.27-.1-.47-.15-.67.15-.2.3-.77 1.28-.95 1.48-.18.2-.36.23-.66.08a10.05 10.05 0 0 1-2.48-1.53 11.08 11.08 0 0 1-1.72-2.14c-.18-.3-.02-.47.13-.62.14-.14.3-.35.45-.53.15-.17.2-.3.3-.5.1-.2.05-.38-.02-.53-.07-.15-.67-1.62-.92-2.22-.25-.6-.5-0.51-.67-.51h-.57c-.2 0-.52.07-.8.37a3.84 3.84 0 0 0-1.2 2.8c0 1.63.83 3.19 1.2 3.69.04.05 2.42 3.7 5.87 5.19(2.87 1.24 3.73 1.05 4.39.99a4.67 4.67 0 0 0 3.09-2.18c.25-.68.25-1.27.18-1.38-.08-.11-.28-.18-.58-.33z"/>
                <path d="M12 2C6.48 2 2 6.48 2 12c0 2.17.7 4.19 1.89 5.84L2 22l4.28-1.83A9.9 9.9 0 0 0 12 22c5.52 0 10-4.48 10-10S17.52 2 12 2zM12 20a7.92 7.92 0 0 1-4.08-1.12l-.29-.17-2.52 1.08.68-2.42-.19-.3A7.95 7.95 0 0 1 4 12c0-4.41 3.59-8 8-8s8 3.59 8 8-3.59 8-8 8z"/>
                </svg>
                </a>"""

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    html = html.replace("\r\n", "\n")
    
    # We will search for wa.me link and remove the entire <a> tag block dynamically to be safe
    # from indentation or path line-breaks.
    if "https://wa.me/201206751361" in html:
        # Find start of <a href="https://wa.me/201206751361"...
        start_idx = html.find('href="https://wa.me/201206751361"')
        if start_idx != -1:
            # backtrack to the nearest `<a`
            tag_start = html.rfind('<a', 0, start_idx)
            # find the closing `</a>`
            tag_end = html.find('</a>', start_idx)
            if tag_start != -1 and tag_end != -1:
                block_to_remove = html[tag_start:tag_end + 4]
                html = html.replace(block_to_remove, "")
                print(f"Removed WhatsApp link from footer of {filepath}")
                
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)


# 2. Update contact.html (Follow Us block)
with open("contact.html", "r", encoding="utf-8") as f:
    contact = f.read()

contact = contact.replace("\r\n", "\n")
old_wa_follow = '<a href="https://wa.me/201206751361" class="social-icon" aria-label="WhatsApp" target="_blank">wa</a>'
if old_wa_follow in contact:
    contact = contact.replace(old_wa_follow, "")
    print("Removed WhatsApp from contact.html follow us block")

with open("contact.html", "w", encoding="utf-8") as f:
    f.write(contact)


# 3. Update main.js (Remove LinkedIn Floating Button)
with open("main.js", "r", encoding="utf-8") as f:
    js = f.read()

js = js.replace("\r\n", "\n")

# Find the LinkedIn Floating Button Injection block
lines = js.split("\n")
start_idx = -1
end_idx = -1
for idx, line in enumerate(lines):
    if "LinkedIn Floating Button Injection" in line:
        start_idx = idx
    if start_idx != -1 and "document.body.appendChild(linkedinBtn);" in line:
        end_idx = idx
        break

if start_idx != -1 and end_idx != -1:
    del lines[start_idx:end_idx+1]
    js = "\n".join(lines)
    print("Removed LinkedIn floating button injection from main.js")
else:
    print("Could not locate LinkedIn floating button injection block in main.js")

with open("main.js", "w", encoding="utf-8") as f:
    f.write(js)
