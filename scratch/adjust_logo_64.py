import glob

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Replace inline logo height from 32px to 64px
    content = content.replace(
        'height="32" style="height: 32px; width: auto;"',
        'height="64" style="height: 64px; width: auto;"'
    )
    
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(content)

print("HTML inline logo heights adjusted to 64px successfully!")
