import glob

def revert_icon():
    for filepath in glob.glob("*.html"):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        content = content.replace('src="assets/icon.svg"', 'src="assets/icon.png"')
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
            
    print("Reverted to icon.png successfully!")

revert_icon()
