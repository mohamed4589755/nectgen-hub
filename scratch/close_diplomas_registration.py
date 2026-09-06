# 1. Update lang.js
with open("lang.js", "r", encoding="utf-8") as f:
    lang = f.read()

lang = lang.replace('diploma_apply_btn: "Register Now"', 'diploma_apply_btn: "Registration Closed"')
# For Arabic text (handling potential encoding in string)
lang = lang.replace('diploma_apply_btn: "سجل الآن"', 'diploma_apply_btn: "التسجيل مغلق"')

with open("lang.js", "w", encoding="utf-8") as f:
    f.write(lang)

print("lang.js updated successfully!")


# 2. Update diplomas.html
with open("diplomas.html", "r", encoding="utf-8") as f:
    diplomas = f.read()

diplomas = diplomas.replace("\r\n", "\n")

# Replace all 4 apply buttons with disabled buttons
for i in range(1, 5):
    # Search for applyDiploma{i}
    tag_start = diplomas.find(f'id="applyDiploma{i}"')
    if tag_start != -1:
        a_start = diplomas.rfind('<a ', 0, tag_start)
        a_end = diplomas.find('</a>', tag_start) + 4
        old_a = diplomas[a_start:a_end]
        
        new_a = f'<a href="javascript:void(0)" class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem; pointer-events: none; opacity: 0.6; cursor: not-allowed;" id="applyDiploma{i}" data-i18n="diploma_apply_btn">Registration Closed</a>'
        diplomas = diplomas.replace(old_a, new_a)
        print(f"Updated applyDiploma{i} in diplomas.html")

with open("diplomas.html", "w", encoding="utf-8") as f:
    f.write(diplomas)

print("diplomas.html updated successfully!")
