from PIL import Image

img_path = 'C:/Users/Mohamed/.gemini/antigravity/brain/76064903-6916-4b75-956b-4b8d945ec252/media__1783560682009.png'
img = Image.open(img_path).convert('RGBA')
width, height = img.size
pixels = img.load()

# Projected corner colors for background slate-blue gradient
c_tl = (95, 122, 131)
c_bl = (110, 152, 169)
c_br = (133, 179, 202)
# Extrapolate top-right based on BL -> BR shift
c_tr = (c_tl[0] + (c_br[0] - c_bl[0]), c_tl[1] + (c_br[1] - c_bl[1]), c_tl[2] + (c_br[2] - c_bl[2]))
print("Estimated TR background color:", c_tr)

# Create a cleaned image
cleaned_img = Image.new('RGBA', (width, height))
cleaned_pixels = cleaned_img.load()

# Test different thresholds
for threshold in [15, 20, 25, 30, 35, 40, 45, 50]:
    transparent_count = 0
    for x in range(width):
        for y in range(height):
            # Bilinear interpolation
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
                transparent_count += 1
                
    pct = (transparent_count / (width * height)) * 100
    print(f"Threshold {threshold}: {transparent_count} transparent ({pct:.2f}%)")
