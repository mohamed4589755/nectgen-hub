from PIL import Image

img_path = 'C:/Users/Mohamed/.gemini/antigravity/brain/76064903-6916-4b75-956b-4b8d945ec252/media__1783561248407.png'
img = Image.open(img_path).convert('RGBA')
width, height = img.size
pixels = img.load()

# Let's inspect the text colors.
# "NextGen" is on the top line (y around 100-200)
# "Institute" is on the bottom line (y around 250-350)
nextgen_colors = []
institute_colors = []

for x in range(350, width):
    for y in range(height):
        p = pixels[x, y]
        # Distance to white
        dist = sum((p[i] - 255)**2 for i in range(3))**0.5
        if dist > 30: # non-white
            if y < height / 2:
                nextgen_colors.append(p[:3])
            else:
                institute_colors.append(p[:3])

# Print average and most common dark color for "NextGen"
from collections import Counter
c_ng = Counter(nextgen_colors).most_common(5)
c_inst = Counter(institute_colors).most_common(5)

print("Top 5 exact colors for 'NextGen' text:")
for color, count in c_ng:
    print(f"Color {color} (hex: #{color[0]:02x}{color[1]:02x}{color[2]:02x}): {count} pixels")

print("\nTop 5 exact colors for 'Institute' text:")
for color, count in c_inst:
    print(f"Color {color} (hex: #{color[0]:02x}{color[1]:02x}{color[2]:02x}): {count} pixels")
