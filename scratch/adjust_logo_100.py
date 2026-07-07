import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Replace inline logo height from 80px to 100px
    content = content.replace(
        'height="80" style="height: 80px; width: auto;"',
        'height="100" style="height: 100px; width: auto;"'
    )
    
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(content)

print("HTML inline logo heights adjusted to 100px successfully!")
