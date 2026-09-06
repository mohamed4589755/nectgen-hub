from PIL import Image

img_path = r"C:\Users\Mohamed\.gemini\antigravity\brain\76064903-6916-4b75-956b-4b8d945ec252\media__1783587682920.jpg"
img = Image.open(img_path)
print(f"Format: {img.format}")
print(f"Size: {img.size} (width, height)")
print(f"Aspect ratio: {img.size[0] / img.size[1]:.3f}")
