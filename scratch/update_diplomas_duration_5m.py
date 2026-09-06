# 1. Update lang.js
with open("lang.js", "r", encoding="utf-8") as f:
    lang = f.read()

lang = lang.replace('diploma_duration_5m: "4 Months"', 'diploma_duration_5m: "5 Months"')
lang = lang.replace('diploma_duration_5m: "٤ شهور"', 'diploma_duration_5m: "٥ شهور"')
lang = lang.replace('diploma_sub: "Comprehensive 4-month programs', 'diploma_sub: "Comprehensive 5-month programs')
lang = lang.replace('diploma_sub: "برامج شاملة مدتها ٤ أشهر', 'diploma_sub: "برامج شاملة مدتها ٥ أشهر')

with open("lang.js", "w", encoding="utf-8") as f:
    f.write(lang)

print("lang.js updated successfully!")


# 2. Update diplomas.html
with open("diplomas.html", "r", encoding="utf-8") as f:
    diplomas = f.read()

diplomas = diplomas.replace("Comprehensive 4-month programs", "Comprehensive 5-month programs")
diplomas = diplomas.replace('<b data-i18n="diploma_duration_5m">4 Months</b>', '<b data-i18n="diploma_duration_5m">5 Months</b>')

with open("diplomas.html", "w", encoding="utf-8") as f:
    f.write(diplomas)

print("diplomas.html updated successfully!")
