from PIL import Image

def recolor():
    try:
        img = Image.open("assets/logo.png").convert("RGBA")
        width, height = img.size
        datas = img.getdata()
        
        newData = []
        for y in range(height):
            for x in range(width):
                r, g, b, a = img.getpixel((x, y))
                
                # Only recolor if pixel is not fully transparent
                if a > 0:
                    if x < 300:
                        # Icon area: recolor to light blue #0071E3 (0, 113, 227)
                        # We can blend it to keep some of the gradient or just make it flat.
                        # Let's make it flat for a clean vector look.
                        newData.append((0, 113, 227, a))
                    else:
                        # Text area: recolor to black/dark gray #1D1D1F (29, 29, 31)
                        newData.append((29, 29, 31, a))
                else:
                    newData.append((255, 255, 255, 0))
                    
        img.putdata(newData)
        img.save("assets/logo.png")
        print("Logo recolored successfully!")
    except Exception as e:
        print(f"Error recoloring: {e}")

recolor()
