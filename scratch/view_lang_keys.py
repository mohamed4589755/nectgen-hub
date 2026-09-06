with open("lang.js", "r", encoding="utf-8") as f:
    js = f.read()

# Let's find and print all lines containing "intern_" keys
lines = js.splitlines()
print("Internship translation keys in lang.js:")
for idx, line in enumerate(lines):
    if "intern_" in line or "duration_" in line:
        print(f"Line {idx+1}: {line.strip()}")
