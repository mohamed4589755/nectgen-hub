from PIL import Image
import os

img_path = r"C:\NextGen Hub Website\assets\bootcamp_frontend.png"

if os.path.exists(img_path):
    img = Image.open(img_path)
    print(f"assets/bootcamp_frontend.png -> Size: {img.size}, Format: {img.format}, Mode: {img.mode}")
else:
    print("Could not find assets/bootcamp_frontend.png")
