# 1. Update lang.js
with open("lang.js", "r", encoding="utf-8") as f:
    js = f.read()

# Replace English duration keys
js = js.replace('boot_duration_3m: "3 Months",', 'boot_duration_2m: "2 Months",')
js = js.replace('diploma_duration_6m: "6 Months",', 'diploma_duration_5m: "5 Months",')

# Replace Arabic duration keys
js = js.replace('boot_duration_3m: "٣ أشهر",', 'boot_duration_2m: "شهرين",')
js = js.replace('diploma_duration_6m: "٦ أشهر",', 'diploma_duration_5m: "٥ أشهر",')

with open("lang.js", "w", encoding="utf-8") as f:
    f.write(js)

print("lang.js durations updated successfully!")


# 2. Update bootcamps.html
with open("bootcamps.html", "r", encoding="utf-8") as f:
    html_boot = f.read()

html_boot = html_boot.replace('data-i18n="boot_duration_3m">3 Months</b>', 'data-i18n="boot_duration_2m">2 Months</b>')

with open("bootcamps.html", "w", encoding="utf-8") as f:
    f.write(html_boot)

print("bootcamps.html durations updated successfully!")


# 3. Update diplomas.html
with open("diplomas.html", "r", encoding="utf-8") as f:
    html_dip = f.read()

html_dip = html_dip.replace('data-i18n="diploma_duration_6m">6 Months</b>', 'data-i18n="diploma_duration_5m">5 Months</b>')

with open("diplomas.html", "w", encoding="utf-8") as f:
    f.write(html_dip)

print("diplomas.html durations updated successfully!")
