with open("lang.js", "r", encoding="utf-8") as f:
    content = f.read()

# Let's search for "ar:" or similar strings in the file safely
for idx, line in enumerate(content.splitlines()):
    if "ar" in line or "translations" in line:
        ascii_line = "".join(c if ord(c) < 128 else "?" for c in line)
        print(f"Line {idx+1}: {ascii_line.strip()}")
