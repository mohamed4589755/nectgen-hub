from PIL import Image

img_path = 'C:/Users/Mohamed/.gemini/antigravity/brain/76064903-6916-4b75-956b-4b8d945ec252/media__1783561248407.png'
img = Image.open(img_path).convert('RGBA')
width, height = img.size
pixels = img.load()

# Print the 4 corners
print("TL:", pixels[0, 0])
print("TR:", pixels[width-1, 0])
print("BL:", pixels[0, height-1])
print("BR:", pixels[width-1, height-1])

# Scan columns to find where the icon ends (gap between icon and text)
# Background is (255, 255, 255, 255) or close to it
col_non_bg = []
for x in range(width):
    non_bg = 0
    for y in range(height):
        p = pixels[x, y]
        # Distance to white
        dist = sum((p[i] - 255)**2 for i in range(3))**0.5
        if dist > 15: # threshold
            non_bg += 1
    col_non_bg.append(non_bg)

# Print columns with content
print("Non-bg pixel count per column:")
for x in range(width):
    if col_non_bg[x] > 0 or (x > 0 and col_non_bg[x-1] > 0):
        if x % 20 == 0 or col_non_bg[x] == 0:
            print(f"Col {x}: {col_non_bg[x]}")
