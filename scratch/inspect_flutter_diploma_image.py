from PIL import Image
import os

img_path = r"C:\Users\Mohamed\.gemini\antigravity\brain\76064903-6916-4b75-956b-4b8d945ec252\media__1788594987269.png"

if os.path.exists(img_path):
    img = Image.open(img_path)
    print(f"Original Image Size: {img.size}, Format: {img.format}, Mode: {img.mode}")
    
    # Save a clean copy to assets directory
    out_path = r"C:\NextGen Hub Website\assets\diploma_flutter.png"
    img.save(out_path, "PNG")
    print(f"Saved copy to {out_path} successfully!")
else:
    print(f"Error: Could not find image at {img_path}")
