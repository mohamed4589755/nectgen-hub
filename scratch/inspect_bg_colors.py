from PIL import Image

img = Image.open("assets/intern_data_analytics.jpg")
width, height = img.size

# Let's sample a few pixels at the edges
print("Bottom edge colors:")
for x in [0, width//4, width//2, 3*width//4, width-1]:
    print(f"  Pixel at ({x}, {height-1}): {img.getpixel((x, height-1))}")

print("\nTop edge colors:")
for x in [0, width//4, width//2, 3*width//4, width-1]:
    print(f"  Pixel at ({x}, 0): {img.getpixel((x, 0))}")

print("\nLeft edge colors:")
for y in [0, height//4, height//2, 3*height//4, height-1]:
    print(f"  Pixel at (0, {y}): {img.getpixel((0, y))}")

print("\nRight edge colors:")
for y in [0, height//4, height//2, 3*height//4, height-1]:
    print(f"  Pixel at ({width-1}, {y}): {img.getpixel((width-1, y))}")
