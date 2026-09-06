# Update diplomas.html
with open("diplomas.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("\r\n", "\n")

# Replace descriptions
html = html.replace(
    'content="Enroll in NextGen Institute\'s professional diplomas in AI and Data Analytics. Comprehensive 6 to 9-month programs with industry certification and co-op placement."',
    'content="Enroll in NextGen Institute\'s professional diplomas in AI and Data Analytics. Comprehensive 4-month programs with industry certification and co-op placement."'
)

html = html.replace(
    '<p class="section-subtitle" data-i18n="diploma_sub">Comprehensive 6 to 9-month programs built to take you from absolute foundations to job-ready expertise with direct placement opportunities.</p>',
    '<p class="section-subtitle" data-i18n="diploma_sub">Comprehensive 4-month programs built to take you from absolute foundations to job-ready expertise with direct placement opportunities.</p>'
)

# Replace 5 Months text inside cards
html = html.replace(
    '<b data-i18n="diploma_duration_5m">5 Months</b>',
    '<b data-i18n="diploma_duration_5m">4 Months</b>'
)

with open("diplomas.html", "w", encoding="utf-8") as f:
    f.write(html)

print("diplomas.html updated successfully!")


# Update lang.js
with open("lang.js", "r", encoding="utf-8") as f:
    lang = f.read()

lang = lang.replace("\r\n", "\n")

# Replace English values
lang = lang.replace(
    'diploma_sub: "Comprehensive 6 to 9-month programs built to take you from absolute foundations to job-ready expertise with direct placement opportunities.",',
    'diploma_sub: "Comprehensive 4-month programs built to take you from absolute foundations to job-ready expertise with direct placement opportunities.",'
)
lang = lang.replace(
    'diploma_duration_5m: "5 Months",',
    'diploma_duration_5m: "4 Months",'
)

# Replace Arabic values
lang = lang.replace(
    'diploma_sub: "برامج شاملة مدتها من ٦ إلى ٩ أشهر مصممة لتأخذك من الأساسيات الصفرية إلى الخبرة الجاهزة للعمل مع فرص تدريب مباشر.",',
    'diploma_sub: "برامج شاملة مدتها ٤ أشهر مصممة لتأخذك من الأساسيات الصفرية إلى الخبرة الجاهزة للعمل مع فرص تدريب مباشر.",'
)
lang = lang.replace(
    'diploma_duration_5m: "٥ أشهر",',
    'diploma_duration_5m: "٤ أشهر",'
)

with open("lang.js", "w", encoding="utf-8") as f:
    f.write(lang)

print("lang.js updated successfully!")
