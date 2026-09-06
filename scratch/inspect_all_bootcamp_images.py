from PIL import Image
import glob
import os

for f in glob.glob(r"C:\NextGen Hub Website\assets\bootcamp_*.png"):
    img = Image.open(f)
    print(f"{os.path.basename(f)}: Size {img.size}, Aspect Ratio {img.size[0]/img.size[1]:.2f}")
