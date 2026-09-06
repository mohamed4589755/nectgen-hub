from PIL import Image

# Load the image
img_path = 'C:/Users/Mohamed/.gemini/antigravity/brain/76064903-6916-4b75-956b-4b8d945ec252/media__1783560682009.png'
img = Image.open(img_path).convert('RGBA')
width, height = img.size

# Let's inspect some pixels on the top-left to estimate background color
pixels = img.load()
print("Top-left background sample pixels (R, G, B, A):")
for r in range(5):
    for c in range(5):
        print(f"({r},{c}): {pixels[c, r]}")

# Let's analyze where the logo icon ends and text begins
# Let's check each x column and count how many pixels are distinct from the background.
# We'll assume background is close to the color at (0,0) which we will print.
bg_color = pixels[0, 0]
print("Background reference color:", bg_color)

# We can scan the columns and see how many non-background pixels are in each column.
col_counts = []
for x in range(width):
    non_bg_count = 0
    for y in range(height):
        p = pixels[x, y]
        # Calculate Euclidean distance in RGB space to background color
        dist = sum((p[i] - bg_color[i]) ** 2 for i in range(3)) ** 0.5
        if dist > 30: # Threshold of 30 for difference
            non_bg_count += 1
    col_counts.append(non_bg_count)

print("Column non-background pixel counts:")
for x in range(width):
    if col_counts[x] > 0 or (x > 0 and col_counts[x-1] > 0):
        print(f"Col {x}: {col_counts[x]}")
