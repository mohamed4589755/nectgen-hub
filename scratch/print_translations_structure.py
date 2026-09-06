with open("lang.js", "r", encoding="utf-8") as f:
    js = f.read()

lines = js.splitlines()
out_lines = []
for idx, line in enumerate(lines):
    if "intern_" in line or "duration_" in line:
        out_lines.append(f"Line {idx+1}: {line.strip()}")

with open("scratch/intern_keys.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out_lines))

print("Keys written to scratch/intern_keys.txt successfully!")
