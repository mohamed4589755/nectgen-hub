from PIL import Image

img_path = r"C:\Users\Mohamed\.gemini\antigravity\brain\76064903-6916-4b75-956b-4b8d945ec252\media__1783634748650.jpg"
img = Image.open(img_path)
width, height = img.size

print(f"Format: {img.format}")
print(f"Size: {width}x{height} (width, height)")
print(f"Aspect ratio: {width / height:.3f}")

# Sample bottom-middle background color
bg_sample = img.getpixel((width // 2, height - 5))
print(f"Sampled background color near bottom-center: {bg_sample}")
