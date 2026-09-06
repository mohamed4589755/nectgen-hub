from PIL import Image

img_path = 'C:/Users/Mohamed/.gemini/antigravity/brain/76064903-6916-4b75-956b-4b8d945ec252/media__1783562264793.png'
img = Image.open(img_path).convert('RGBA')
width, height = img.size
pixels = img.load()

# Print the 4 corners
print("TL:", pixels[0, 0])
print("TR:", pixels[width-1, 0])
print("BL:", pixels[0, height-1])
print("BR:", pixels[width-1, height-1])

# Scan columns to find where the icon ends (gap between icon and text)
# We can check which columns are mostly constant (low standard deviation)
col_std = []
for x in range(width):
    colors = [pixels[x, y][:3] for y in range(height)]
    # Average color of column
    avg_r = sum(c[0] for c in colors) / height
    avg_g = sum(c[1] for c in colors) / height
    avg_b = sum(c[2] for c in colors) / height
    # Variance
    var = sum(((c[0]-avg_r)**2 + (c[1]-avg_g)**2 + (c[2]-avg_b)**2) for c in colors) / height
    std = var**0.5
    col_std.append(std)

print("Column standard deviations (foreground has higher std, background has lower std):")
for x in range(width):
    if col_std[x] > 5.0 or (x > 0 and col_std[x-1] > 5.0):
        if x % 10 == 0 or col_std[x] < 5.0:
            print(f"Col {x}: {col_std[x]:.2f}")
