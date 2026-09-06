import glob

# 1. Update all HTML files
html_script_to_remove = """    <script>
        if (localStorage.getItem('selectedTheme') === 'dark') {
            document.documentElement.classList.add('dark-theme');
        }
    </script>"""

# Normalizing to single newlines
html_script_to_remove_norm = html_script_to_remove.replace("\r\n", "\n")

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    html = html.replace("\r\n", "\n")
    
    if html_script_to_remove_norm in html:
        html = html.replace(html_script_to_remove_norm, "")
        print(f"Removed inline script from {filepath}")
    else:
        # Try finding it with different spacing/indents
        # Fallback regex-free replacement
        temp = html.replace(" ", "").replace("\n", "")
        script_compact = "if(localStorage.getItem('selectedTheme')==='dark'){document.documentElement.classList.add('dark-theme');}"
        if script_compact in temp:
            # Let's locate and remove it line by line
            lines = html.split("\n")
            start_idx = -1
            end_idx = -1
            for idx, line in enumerate(lines):
                if "<script>" in line and idx < len(lines) - 3:
                    if "localStorage.getItem('selectedTheme') === 'dark'" in lines[idx+1]:
                        start_idx = idx
                        end_idx = idx + 4 # <script>, if, classList, }, </script>
                        break
            if start_idx != -1:
                del lines[start_idx:end_idx+1]
                html = "\n".join(lines)
                print(f"Removed inline script via fallback from {filepath}")
            else:
                print(f"Could not find exact script to remove in {filepath}")
        else:
            print(f"Script not present in {filepath}")
            
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)


# 2. Update main.js
with open("main.js", "r", encoding="utf-8") as f:
    js = f.read()

js = js.replace("\r\n", "\n")

# Remove top theme check
old_top_check = """// Instant theme application to prevent light-theme flash
if (localStorage.getItem('selectedTheme') === 'dark') {
    document.documentElement.classList.add('dark-theme');
    document.body.classList.add('dark-theme');
}"""

new_top_check = """// Force light theme and clean up old theme settings
localStorage.setItem('selectedTheme', 'light');
document.documentElement.classList.remove('dark-theme');
document.body.classList.remove('dark-theme');"""

if old_top_check in js:
    js = js.replace(old_top_check, new_top_check)
    print("Updated top theme check in main.js")
else:
    # Try alternate indentation or text
    print("Could not find exact top theme check in main.js, searching by lines")
    lines = js.split("\n")
    if "localStorage.getItem('selectedTheme') === 'dark'" in lines[1]:
        lines[0:5] = [new_top_check]
        js = "\n".join(lines)
        print("Updated top theme check in main.js via line-index")

# Remove Dark Mode Switcher block
# We will find the comment '// --- Dark Mode Switcher ---' up to 'initTheme();' and 'setTimeout(initTheme, 100);'
lines = js.split("\n")
start_idx = -1
end_idx = -1
for idx, line in enumerate(lines):
    if "// --- Dark Mode Switcher ---" in line:
        start_idx = idx
    if start_idx != -1 and "setTimeout(initTheme, 100);" in line:
        end_idx = idx
        break

if start_idx != -1 and end_idx != -1:
    del lines[start_idx:end_idx+1]
    js = "\n".join(lines)
    print("Removed Dark Mode Switcher block from main.js")
else:
    print("Could not locate Dark Mode Switcher block in main.js")

with open("main.js", "w", encoding="utf-8") as f:
    f.write(js)

print("main.js updated successfully!")
