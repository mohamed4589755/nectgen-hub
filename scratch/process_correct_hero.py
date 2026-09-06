from PIL import Image

src_path = r"C:\Users\Mohamed\.gemini\antigravity\brain\76064903-6916-4b75-956b-4b8d945ec252\media__1784123991747.jpg"
target_w, target_h = 1200, 896

img = Image.open(src_path)
img_resized = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
img_resized.save("assets/hero_bg.jpg", "JPEG", quality=95)

print("Branded hero image updated successfully at assets/hero_bg.jpg!")
