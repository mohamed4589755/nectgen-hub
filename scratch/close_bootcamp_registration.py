# Update bootcamps.html
with open("bootcamps.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("\r\n", "\n")

# Replace each of the 4 bootcamp buttons
old_btn1 = 'href="contact.html?bootcamp=AI_ML" class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem;" id="applyBoot1"'
new_btn1 = 'href="javascript:void(0)" class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem; pointer-events: none; opacity: 0.6; cursor: not-allowed;" id="applyBoot1"'
html = html.replace(old_btn1, new_btn1)

old_btn2 = 'href="contact.html?bootcamp=Data_Analytics" class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem;" id="applyBoot2"'
new_btn2 = 'href="javascript:void(0)" class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem; pointer-events: none; opacity: 0.6; cursor: not-allowed;" id="applyBoot2"'
html = html.replace(old_btn2, new_btn2)

old_btn3 = 'href="contact.html?bootcamp=Flutter_Dev" class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem;" id="applyBoot3"'
new_btn3 = 'href="javascript:void(0)" class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem; pointer-events: none; opacity: 0.6; cursor: not-allowed;" id="applyBoot3"'
html = html.replace(old_btn3, new_btn3)

old_btn4 = 'href="contact.html?bootcamp=Frontend_Dev" class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem;" id="applyBoot4"'
new_btn4 = 'href="javascript:void(0)" class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem; pointer-events: none; opacity: 0.6; cursor: not-allowed;" id="applyBoot4"'
html = html.replace(old_btn4, new_btn4)

with open("bootcamps.html", "w", encoding="utf-8") as f:
    f.write(html)

print("bootcamps.html updated successfully!")


# Update lang.js
with open("lang.js", "r", encoding="utf-8") as f:
    lang = f.read()

lang = lang.replace("\r\n", "\n")

# Replace English and Arabic translation strings
lang = lang.replace('boot_apply_btn: "Register Now",', 'boot_apply_btn: "Registration Closed",')
lang = lang.replace('boot_apply_btn: "سجل الآن",', 'boot_apply_btn: "التسجيل مغلق",')

with open("lang.js", "w", encoding="utf-8") as f:
    f.write(lang)

print("lang.js updated successfully!")
