with open(r"C:\NextGen Hub Website\styles.css", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "section-title" in line or "section-subtitle" in line or "cards-grid" in line or "hero" in line:
        # Print surrounding context
        print(f"Line {i+1}: {line.strip()}")
