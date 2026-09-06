from PIL import Image

# Open the original image
img_path = "assets/intern_data_analytics.jpg"
img = Image.open(img_path)
width, height = img.size

# Sample background color from top-left corner (0, 0)
bg_color = img.getpixel((5, 5))
print(f"Sampled background color: {bg_color}")

# Calculate target height for 16:9 aspect ratio
target_height = int(width * 9 / 16) # 870 * 9 / 16 = 489
print(f"Original size: {width}x{height}")
print(f"Target size: {width}x{target_height}")

# Create new image with sampled background color
new_img = Image.new("RGB", (width, target_height), bg_color)

# Paste the original image in the vertical center
y_offset = (target_height - height) // 2 # (489 - 348) // 2 = 70
new_img.paste(img, (0, y_offset))

# Save the padded image
new_img.save(img_path, "JPEG", quality=95)
print("Image padded to 16:9 successfully and saved!")
