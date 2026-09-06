import re

with open("styles.css", "r", encoding="utf-8") as f:
    lines = f.readlines()

print("Background declarations in styles.css:")
for idx, line in enumerate(lines):
    if "background" in line or "background-color" in line:
        # Check if it has a hardcoded hex color like #FFF, #FFFFFF, #FFF... or rgb/rgba or common colors
        match = re.search(r"background(-color)?\s*:\s*([^;]+);", line)
        if match:
            value = match.group(2).strip()
            # If it doesn't use var(--) or gradient, let's print it to check
            if "var(" not in value and "linear-gradient" not in value and "url(" not in value and "none" not in value and "transparent" not in value:
                print(f"Line {idx+1}: {line.strip()}")
