with open("internships.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

print("Script blocks found in internships.html:")
for idx, line in enumerate(lines):
    if "<script" in line:
        print(f"Line {idx+1}: {line.strip()}")
