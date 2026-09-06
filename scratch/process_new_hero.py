from PIL import Image, ImageFilter

# Paths
src_path = r"C:\Users\Mohamed\.gemini\antigravity\brain\76064903-6916-4b75-956b-4b8d945ec252\media__1784122535492.jpg"
target_w, target_h = 1200, 896

# Load source image
img = Image.open(src_path)
w, h = img.size

# --- 1. Option A: Center Crop ---
# Target aspect ratio is 1200/896 = 1.3393
# Source aspect ratio is w/h
crop_w = w
crop_h = int(w * (target_h / target_w))
if crop_h > h:
    crop_h = h
    crop_w = int(h * (target_w / target_h))

x_offset = (w - crop_w) // 2
y_offset = (h - crop_h) // 2

img_crop_center = img.crop((x_offset, y_offset, x_offset + crop_w, y_offset + crop_h))
img_crop_center_resized = img_crop_center.resize((target_w, target_h), Image.Resampling.LANCZOS)
img_crop_center_resized.save("assets/hero_bg_crop_center.jpg", "JPEG", quality=95)
print("Saved assets/hero_bg_crop_center.jpg")

# --- 2. Option B: Top-Weighted Crop ---
# We keep more of the top (y starts at 20 instead of center offset)
y_offset_top = min(30, h - crop_h)
img_crop_top = img.crop((x_offset, y_offset_top, x_offset + crop_w, y_offset_top + crop_h))
img_crop_top_resized = img_crop_top.resize((target_w, target_h), Image.Resampling.LANCZOS)
img_crop_top_resized.save("assets/hero_bg_crop_top.jpg", "JPEG", quality=95)
print("Saved assets/hero_bg_crop_top.jpg")

# --- 3. Option C: Blur Padded ---
# Background: Stretched and blurred version
bg_img = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
bg_img = bg_img.filter(ImageFilter.GaussianBlur(50)) # heavy blur

# Foreground: Resize source image to fit height (896px)
fg_h = target_h
fg_w = int(w * (fg_h / h))
fg_img = img.resize((fg_w, fg_h), Image.Resampling.LANCZOS)

# Paste foreground centered on background
paste_x = (target_w - fg_w) // 2
bg_img.paste(fg_img, (paste_x, 0))
bg_img.save("assets/hero_bg_blur_pad.jpg", "JPEG", quality=95)
print("Saved assets/hero_bg_blur_pad.jpg")
