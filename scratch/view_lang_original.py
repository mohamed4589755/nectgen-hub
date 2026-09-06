with open("lang.js", "r", encoding="utf-8") as f:
    js = f.read()

lines = js.splitlines()
out = []
for idx, line in enumerate(lines):
    if "boot_" in line:
        out.append(f"Line {idx+1}: {line.strip()}")

with open("scratch/boot_keys_original.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out))

print("Original boot keys written to scratch/boot_keys_original.txt")
