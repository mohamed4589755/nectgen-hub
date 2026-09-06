from PIL import Image
from collections import Counter

image_path = r"C:\Users\Mohamed\.gemini\antigravity\brain\76064903-6916-4b75-956b-4b8d945ec252\media__1786497554500.png"
image = Image.open(image_path)
image = image.convert("RGB")

# Get colors
colors = image.getdata()

# Find colors that are distinct (not white, grey, or black)
# Let's count them
color_counts = Counter(colors)

print("Top colors:")
for color, count in color_counts.most_common(50):
    r, g, b = color
    # Skip whites/greys/blacks
    if abs(r - g) < 20 and abs(g - b) < 20 and abs(r - b) < 20:
        continue
    hex_color = f"#{r:02x}{g:02x}{b:02x}"
    print(f"Hex: {hex_color}, RGB: {color}, Count: {count}")
