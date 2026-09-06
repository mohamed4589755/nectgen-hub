from PIL import Image

# Open the original image
img_path = r"C:\Users\Mohamed\.gemini\antigravity\brain\76064903-6916-4b75-956b-4b8d945ec252\media__1783634748650.jpg"
img = Image.open(img_path)
width, height = img.size

# Sample background color from the left edge (near middle-left)
bg_color = img.getpixel((5, height // 2))
print(f"Sampled left-edge background color: {bg_color}")

# Calculate target width for 16:9 aspect ratio (784 x 441)
target_width = int(height * 16 / 9)
print(f"Original size: {width}x{height}")
print(f"Target size: {target_width}x{height}")

# Create new image with sampled background color
new_img = Image.new("RGB", (target_width, height), bg_color)

# Paste the original image in the horizontal center
x_offset = (target_width - width) // 2
new_img.paste(img, (x_offset, 0))

# Save the padded image to the assets folder directly
out_path = "assets/intern_flutter.jpg"
new_img.save(out_path, "JPEG", quality=95)
print("Image successfully padded and saved to assets/intern_flutter.jpg!")
