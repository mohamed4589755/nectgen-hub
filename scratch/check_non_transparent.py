from PIL import Image

img = Image.open('assets/icon.png')
width, height = img.size
pixels = img.load()

bg_like_coords = []
for x in range(width):
    for y in range(height):
        r, g, b, a = pixels[x, y]
        if a == 255:
            # Check if this pixel is close to background slate-blue (e.g. R ~ 100, G ~ 140, B ~ 150)
            if 80 < r < 140 and 110 < g < 180 and 120 < b < 210:
                bg_like_coords.append((x, y, (r, g, b)))

print(f"Total bg-like pixels: {len(bg_like_coords)}")
print("First 20 bg-like pixels coordinates and colors:")
for x, y, color in bg_like_coords[:20]:
    print(f"({x}, {y}): {color}")
