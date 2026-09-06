from PIL import Image

img = Image.open('assets/icon.png')
width, height = img.size
pixels = img.load()

# Check some outer pixels that are semi-transparent or colored
semi_transparent = 0
opaque_bg_like = 0

for x in range(width):
    for y in range(height):
        r, g, b, a = pixels[x, y]
        if 0 < a < 255:
            semi_transparent += 1
        elif a == 255:
            # Check if this pixel is close to background slate-blue (e.g. R ~ 100, G ~ 140, B ~ 150)
            if 80 < r < 140 and 110 < g < 180 and 120 < b < 210:
                opaque_bg_like += 1

print(f"Icon pixels: {width}x{height}")
print(f"Semi-transparent (anti-aliased edge) pixels: {semi_transparent}")
print(f"Opaque pixels resembling background slate-blue: {opaque_bg_like}")
