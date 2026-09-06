from PIL import Image

img_path = 'C:/Users/Mohamed/.gemini/antigravity/brain/76064903-6916-4b75-956b-4b8d945ec252/media__1783561248407.png'
img = Image.open(img_path).convert('RGBA')
width, height = img.size
pixels = img.load()

# Crop the icon region (x=70 to x=350, y=0 to y=height)
icon_crop = img.crop((70, 0, 350, height))
w, h = icon_crop.size
crop_pixels = icon_crop.load()

# Smooth white background removal for anti-aliasing preservation
for x in range(w):
    for y in range(h):
        r, g, b, a = crop_pixels[x, y]
        # Calculate distance to pure white
        dist = ((r - 255)**2 + (g - 255)**2 + (b - 255)**2)**0.5
        
        # Smooth alpha interpolation
        if dist < 15.0:
            crop_pixels[x, y] = (0, 0, 0, 0)
        elif dist < 35.0:
            # Interpolate alpha from 0 (transparent) to 255 (opaque)
            factor = (dist - 15.0) / (35.0 - 15.0)
            new_a = int(factor * 255)
            crop_pixels[x, y] = (r, g, b, new_a)

# Auto-crop (trim) empty borders
bbox = icon_crop.getbbox()
if bbox:
    icon_final = icon_crop.crop(bbox)
else:
    icon_final = icon_crop

# Save the final icon as assets/icon.png
icon_final.save('assets/icon.png')
print("High-res cropped transparent icon saved to assets/icon.png! Size:", icon_final.size)
