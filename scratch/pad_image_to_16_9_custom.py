from PIL import Image

# Open the original image
img_path = "assets/intern_data_analytics.jpg"
img = Image.open(img_path)
width, height = img.size

# Deep dark navy background color to match the image's overall theme
bg_color = (24, 40, 65)

# Calculate target height for 16:9 aspect ratio (870 x 489)
target_height = int(width * 9 / 16)
print(f"Original size: {width}x{height}")
print(f"Target size: {width}x{target_height}")

# Create a new image filled with the dark navy color
new_img = Image.new("RGB", (width, target_height), bg_color)

# Paste the original image in the vertical center
y_offset = (target_height - height) // 2
new_img.paste(img, (0, y_offset))

# Save the padded image
new_img.save(img_path, "JPEG", quality=95)
print("Image successfully padded with custom dark navy and saved!")
