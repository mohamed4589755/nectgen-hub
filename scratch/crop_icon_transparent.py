from PIL import Image

img_path = 'C:/Users/Mohamed/.gemini/antigravity/brain/76064903-6916-4b75-956b-4b8d945ec252/media__1783560682009.png'
img = Image.open(img_path).convert('RGBA')
width, height = img.size
pixels = img.load()

# Projected corner colors for background slate-blue gradient
c_tl = (95, 122, 131)
c_bl = (110, 152, 169)
c_br = (133, 179, 202)
c_tr = (c_tl[0] + (c_br[0] - c_bl[0]), c_tl[1] + (c_br[1] - c_bl[1]), c_tl[2] + (c_br[2] - c_bl[2]))

# Create transparent image
cleaned_img = Image.new('RGBA', (width, height))
cleaned_pixels = cleaned_img.load()

# Threshold of 45 is ideal to clean background slate-blue without erasing logo parts
threshold = 45

for x in range(width):
    for y in range(height):
        # Bilinear interpolation of background color
        tx = x / (width - 1) if width > 1 else 0
        ty = y / (height - 1) if height > 1 else 0
        
        c_t = [c_tl[i] + tx * (c_tr[i] - c_tl[i]) for i in range(3)]
        c_b = [c_bl[i] + tx * (c_br[i] - c_bl[i]) for i in range(3)]
        
        bg_r = c_t[0] + ty * (c_b[0] - c_t[0])
        bg_g = c_t[1] + ty * (c_b[1] - c_t[1])
        bg_b = c_t[2] + ty * (c_b[2] - c_t[2])
        
        p = pixels[x, y]
        dist = ((p[0] - bg_r)**2 + (p[1] - bg_g)**2 + (p[2] - bg_b)**2)**0.5
        
        if dist < threshold:
            # Set background to transparent
            cleaned_pixels[x, y] = (0, 0, 0, 0)
        else:
            cleaned_pixels[x, y] = p

# Now, crop the icon region (x=0 to x=80, y=0 to y=height)
# We crop it slightly wider (x=80) to make sure we don't cut the arrow tip, then auto-crop (trim)
icon_crop = cleaned_img.crop((0, 0, 80, height))

# Auto-crop (trim) transparent edges
bbox = icon_crop.getbbox()
if bbox:
    icon_final = icon_crop.crop(bbox)
else:
    icon_final = icon_crop

# Save the final icon as assets/icon.png
icon_final.save('assets/icon.png')
print("Cropped transparent icon saved to assets/icon.png! Size:", icon_final.size)
