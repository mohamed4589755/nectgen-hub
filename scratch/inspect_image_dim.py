from PIL import Image

img = Image.open("assets/intern_data_analytics.jpg")
print(f"Image format: {img.format}")
print(f"Image size: {img.size} (width, height)")
print(f"Aspect ratio: {img.size[0] / img.size[1]:.3f}")
