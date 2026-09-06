with open("styles.css", "r", encoding="utf-8") as f:
    content = f.read()

# Let's count opening and closing braces
open_braces = content.count("{")
close_braces = content.count("}")

print(f"Total opening braces: {open_braces}")
print(f"Total closing braces: {close_braces}")

if open_braces != close_braces:
    print("Warning: Braces mismatch! There is a syntax error in the CSS file!")
else:
    print("Braces match! No simple brace count syntax error.")

# Let's inspect the last 100 lines safely (ASCII only) to check for missing braces or parsing issues
lines = content.splitlines()
print("\\nLast 40 lines of styles.css:")
for idx in range(max(0, len(lines) - 40), len(lines)):
    ascii_line = "".join(c if ord(c) < 128 else "?" for c in lines[idx])
    print(f"Line {idx+1}: {ascii_line}")
