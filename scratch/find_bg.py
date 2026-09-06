from PIL import Image
from collections import Counter

img_path = 'C:/Users/Mohamed/.gemini/antigravity/brain/76064903-6916-4b75-956b-4b8d945ec252/media__1783560682009.png'
img = Image.open(img_path).convert('RGBA')
width, height = img.size
pixels = img.load()

# Let's count colors with binning to find the dominant color
# We bin each color component into bins of size 8 to group close colors
color_bins = Counter()
for x in range(width):
    for y in range(height):
        p = pixels[x, y]
        binned = (p[0] // 8 * 8, p[1] // 8 * 8, p[2] // 8 * 8)
        color_bins[binned] += 1

# Print the top 10 binned colors
print("Top 10 binned colors:")
for color, count in color_bins.most_common(10):
    pct = (count / (width * height)) * 100
    print(f"Color {color}: {count} pixels ({pct:.2f}%)")
