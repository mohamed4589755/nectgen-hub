from PIL import Image

img_path = 'C:/Users/Mohamed/.gemini/antigravity/brain/76064903-6916-4b75-956b-4b8d945ec252/media__1783560682009.png'
img = Image.open(img_path).convert('RGBA')
width, height = img.size
pixels = img.load()

c_tl = pixels[0, 0]          # Top-Left
c_tr = pixels[width-1, 0]     # Top-Right
c_bl = pixels[0, height-1]    # Bottom-Left
c_br = pixels[width-1, height-1] # Bottom-Right

print("TL:", c_tl)
print("TR:", c_tr)
print("BL:", c_bl)
print("BR:", c_br)

# Bilinear interpolation background remover
cleaned_img = Image.new('RGBA', (width, height))
cleaned_pixels = cleaned_img.load()

for threshold in [15, 20, 25, 30, 35, 40]:
    transparent_count = 0
    for x in range(width):
        for y in range(height):
            # Bilinear interpolation of background color at (x, y)
            tx = x / (width - 1) if width > 1 else 0
            ty = y / (height - 1) if height > 1 else 0
            
            # Interpolate top edge
            c_t = [c_tl[i] + tx * (c_tr[i] - c_tl[i]) for i in range(3)]
            # Interpolate bottom edge
            c_b = [c_bl[i] + tx * (c_br[i] - c_bl[i]) for i in range(3)]
            # Interpolate vertically
            bg_r = c_t[0] + ty * (c_b[0] - c_t[0])
            bg_g = c_t[1] + ty * (c_b[1] - c_t[1])
            bg_b = c_t[2] + ty * (c_b[2] - c_t[2])
            
            p = pixels[x, y]
            dist = ((p[0] - bg_r)**2 + (p[1] - bg_g)**2 + (p[2] - bg_b)**2)**0.5
            
            if dist < threshold:
                transparent_count += 1
                
    pct = (transparent_count / (width * height)) * 100
    print(f"Bilinear Threshold {threshold}: {transparent_count} transparent ({pct:.2f}%)")
