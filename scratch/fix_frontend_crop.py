from PIL import Image, ImageOps
import numpy as np

img_path = r"C:\NextGen Hub Website\assets\bootcamp_frontend.png"
img = Image.open(img_path).convert("RGBA")
width, height = img.size

# We want 16:9 aspect ratio (width / height = 16 / 9)
# Current aspect ratio is 1000 / 470 = 2.127 (wider than 16:9)
# To fit a 2.127 image inside 16:9 without cropping left/right during object-fit:cover,
# the image height must be increased to: target_height = width * 9 / 16 = 1000 * 9 / 16 = 562.5 (563 px)

target_width = width
target_height = int(width * 9 / 16) # 562

# Sample edge colors from the top and bottom of original image
# Let's create a background image of target_width x target_height filled with the top/bottom background purple
top_color = img.getpixel((width // 2, 5))
bottom_color = img.getpixel((width // 2, height - 5))

# Create 16:9 canvas
new_img = Image.new("RGBA", (target_width, target_height), top_color)

# Paste original image in the vertical center of the 16:9 canvas
paste_y = (target_height - height) // 2
new_img.paste(img, (0, paste_y), img)

# Also let's check if we want extra left padding so text is safely away from the left border:
# Let's shift the image 40px to the right and fill left with left-edge color
shift_x = 45
left_color = img.getpixel((5, height // 2))

final_img = Image.new("RGBA", (target_width + shift_x, target_height), left_color)
final_img.paste(new_img, (shift_x, 0), new_img)

# Crop back to exact 16:9 ratio
final_16_9 = final_img.resize((target_width, target_height), Image.Resampling.LANCZOS)
final_16_9.save(r"C:\NextGen Hub Website\assets\bootcamp_frontend.png", "PNG")

print(f"Fixed bootcamp_frontend.png to 16:9 ({target_width}x{target_height}) with safe margin!")
