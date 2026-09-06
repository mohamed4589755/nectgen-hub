import glob

# Search blocks
old_footer_social = """                <div class="social-links" style="margin-top: 16px;">
                    <a href="https://www.linkedin.com/company/nextgen-institute/" class="social-icon" aria-label="LinkedIn" target="_blank">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/>
                            <rect x="2" y="9" width="4" height="12"/>
                            <circle cx="4" cy="4" r="2"/>
                        </svg>
                    </a>
                    <a href="#" class="social-icon" aria-label="Facebook" target="_blank">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>
                        </svg>
                    </a>
                    <a href="#" class="social-icon" aria-label="Instagram" target="_blank">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <rect x="2" y="2" width="20" height="20" rx="5" ry="5"/>
                            <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/>
                            <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/>
                        </svg>
                    </a>
                    <a href="#" class="social-icon" aria-label="GitHub" target="_blank">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/>
                        </svg>
                    </a>
                </div>"""

new_footer_social = """                <div class="social-links" style="margin-top: 16px;">
                    <a href="https://www.linkedin.com/company/nextgen-institute/" class="social-icon" aria-label="LinkedIn" target="_blank">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/>
                            <rect x="2" y="9" width="4" height="12"/>
                            <circle cx="4" cy="4" r="2"/>
                        </svg>
                    </a>
                    <a href="https://wa.me/201206751361" class="social-icon" aria-label="WhatsApp" target="_blank">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M17.49 15.3c-.3-.15-1.78-.88-2.05-.98-.27-.1-.47-.15-.67.15-.2.3-.77 1.28-.95 1.48-.18.2-.36.23-.66.08a10.05 10.05 0 0 1-2.48-1.53 11.08 11.08 0 0 1-1.72-2.14c-.18-.3-.02-.47.13-.62.14-.14.3-.35.45-.53.15-.17.2-.3.3-.5.1-.2.05-.38-.02-.53-.07-.15-.67-1.62-.92-2.22-.25-.6-.5-0.51-.67-.51h-.57c-.2 0-.52.07-.8.37a3.84 3.84 0 0 0-1.2 2.8c0 1.63.83 3.19 1.2 3.69.04.05 2.42 3.7 5.87 5.19 2.87 1.24 3.73 1.05 4.39.99a4.67 4.67 0 0 0 3.09-2.18c.25-.68.25-1.27.18-1.38-.08-.11-.28-.18-.58-.33z"/>
                            <path d="M12 2C6.48 2 2 6.48 2 12c0 2.17.7 4.19 1.89 5.84L2 22l4.28-1.83A9.9 9.9 0 0 0 12 22c5.52 0 10-4.48 10-10S17.52 2 12 2zM12 20a7.92 7.92 0 0 1-4.08-1.12l-.29-.17-2.52 1.08.68-2.42-.19-.3A7.95 7.95 0 0 1 4 12c0-4.41 3.59-8 8-8s8 3.59 8 8-3.59 8-8 8z"/>
                        </svg>
                    </a>
                </div>"""

# Normalize spacing for matching
old_footer_social_normalized = "\n".join([line.strip() for line in old_footer_social.split("\n") if line.strip()])

# Update footers in all HTML files
for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    content = content.replace("\r\n", "\n")
    
    # We will search and replace the footer block. To be safe against indentation differences, we can match lines.
    lines = content.split("\n")
    found_start = -1
    for i in range(len(lines) - 25):
        chunk = "\n".join([line.strip() for line in lines[i:i+26] if line.strip()])
        if chunk.startswith(old_footer_social_normalized[:200]) and chunk.endswith(old_footer_social_normalized[-200:]):
            found_start = i
            break
            
    if found_start != -1:
        # Replace the 26 lines starting at found_start
        # Preserve the indentation of the first line
        indent = len(lines[found_start]) - len(lines[found_start].lstrip())
        indent_str = " " * indent
        
        indented_new_social = "\n".join([indent_str + line.strip() for line in new_footer_social.split("\n")])
        
        # Replace lines from found_start to found_start + 26
        # Find the actual end line by checking how many lines had non-empty content
        non_empty_count = 0
        idx = found_start
        while non_empty_count < 26 and idx < len(lines):
            if lines[idx].strip():
                non_empty_count += 1
            idx += 1
        
        lines[found_start:idx] = [indented_new_social]
        content = "\n".join(lines)
        print(f"Updated footer social links in {filepath}")
    else:
        print(f"Footer social links not found in {filepath} using standard block, trying fallback")
        # Fallback exact replace
        content = content.replace(old_footer_social, new_footer_social)
        
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

# Update contact.html Follow Us block
with open("contact.html", "r", encoding="utf-8") as f:
    contact_content = f.read()

contact_content = contact_content.replace("\r\n", "\n")

old_contact_follow = """                    <div class="social-links">
                        <a href="https://www.linkedin.com/company/nextgen-institute/" class="social-icon" aria-label="LinkedIn" target="_blank">in</a>
                        <a href="#" class="social-icon" aria-label="Facebook" target="_blank">fb</a>
                        <a href="#" class="social-icon" aria-label="Instagram" target="_blank">ig</a>
                        <a href="#" class="social-icon" aria-label="GitHub">git</a>
                    </div>"""

new_contact_follow = """                    <div class="social-links">
                        <a href="https://www.linkedin.com/company/nextgen-institute/" class="social-icon" aria-label="LinkedIn" target="_blank">in</a>
                        <a href="https://wa.me/201206751361" class="social-icon" aria-label="WhatsApp" target="_blank">wa</a>
                    </div>"""

contact_content = contact_content.replace(old_contact_follow, new_contact_follow)

with open("contact.html", "w", encoding="utf-8") as f:
    f.write(contact_content)

print("contact.html Follow Us block updated successfully!")
