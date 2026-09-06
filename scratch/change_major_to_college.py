import glob

# 1. Update lang.js translations
with open("lang.js", "r", encoding="utf-8") as f:
    js = f.read()

js = js.replace("\r\n", "\n")

js = js.replace('form_uni_label: "University & Major",', 'form_uni_label: "University & College",')
js = js.replace('form_uni_label: "الجامعة والتخصص",', 'form_uni_label: "الجامعة والكلية",')

with open("lang.js", "w", encoding="utf-8") as f:
    f.write(js)

print("lang.js updated successfully!")


# 2. Update HTML pages (internships, bootcamps, diplomas)
for filepath in ["internships.html", "bootcamps.html", "diplomas.html"]:
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
        
    html = html.replace("\r\n", "\n")
    
    # Replace label fallback text
    html = html.replace(
        '<label for="university" data-i18n="form_uni_label">University & Major</label>',
        '<label for="university" data-i18n="form_uni_label">University & College</label>'
    )
    
    # Replace input placeholder
    html = html.replace(
        'placeholder="e.g. Cairo University, Computer Science"',
        'placeholder="e.g. Cairo University, Faculty of Engineering"'
    )
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
        
    print(f"{filepath} updated successfully!")
