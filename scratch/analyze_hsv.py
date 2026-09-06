from PIL import Image
import colorsys

img_path = 'C:/Users/Mohamed/.gemini/antigravity/brain/76064903-6916-4b75-956b-4b8d945ec252/media__1783560682009.png'
img = Image.open(img_path).convert('RGBA')
width, height = img.size

# Crop the icon region (left side, width around 85)
icon_crop = img.crop((0, 0, 85, height))
icon_pixels = icon_crop.load()

# Let's inspect the HSV values of the pixels in the cropped icon
# We want to see the hue (H), saturation (S), and value (V) of background vs icon pixels
stats = []
for x in range(85):
    for y in range(height):
        r, g, b, a = icon_pixels[x, y]
        # Convert RGB to HSV
        h, s, v = colorsys.rgb_to_hsv(r/255.0, g/255.0, b/255.0)
        stats.append((r, g, b, h, s, v))

# Let's group by saturation ranges and print the count and average RGB
from collections import defaultdict
sat_groups = defaultdict(list)
for r, g, b, h, s, v in stats:
    bin_idx = int(s * 10) # Bins of 0.1
    sat_groups[bin_idx].append((r, g, b))

print("Saturation distribution in cropped icon:")
for b in sorted(sat_groups.keys()):
    count = len(sat_groups[b])
    avg_r = sum(p[0] for p in sat_groups[b]) / count
    avg_g = sum(p[1] for p in sat_groups[b]) / count
    avg_b = sum(p[2] for p in sat_groups[b]) / count
    print(f"Sat {b/10:.1f} - {(b+1)/10:.1f}: {count} pixels, Avg RGB: ({avg_r:.1f}, {avg_g:.1f}, {avg_b:.1f})")
