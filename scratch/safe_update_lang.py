with open("lang.js", "r", encoding="utf-8") as f:
    js = f.read()

# 1. Update English translations (under 'en' object)
# Note: we need to replace exact key-value pairs
js = js.replace('intern_role1_tag3: "Paid",', 'intern_role1_tag3: "Free",')
js = js.replace('intern_role2_tag2: "Hybrid",', 'intern_role2_tag2: "Remote",')
js = js.replace('intern_role2_tag3: "Paid",', 'intern_role2_tag3: "Free",')
js = js.replace('intern_role3_tag3: "Paid",', 'intern_role3_tag3: "Free",')
js = js.replace('intern_role4_tag2: "Hybrid",', 'intern_role4_tag2: "Remote",')
js = js.replace('intern_role4_tag3: "Paid",', 'intern_role4_tag3: "Free",')

# Add intern_duration_1m to English list
old_en_durations = """        intern_duration_label: "Duration:",
        intern_duration_3m: "3 Months",
        intern_duration_6m: "6 Months","""

new_en_durations = """        intern_duration_label: "Duration:",
        intern_duration_1m: "1 Month (Oct 1 - Nov 1)",
        intern_duration_3m: "3 Months",
        intern_duration_6m: "6 Months","""

js = js.replace(old_en_durations, new_en_durations)


# 2. Update Arabic translations (under 'ar' object)
js = js.replace('intern_role1_tag3: "مدفوع",', 'intern_role1_tag3: "مجاني",')
js = js.replace('intern_role2_tag2: "هجين",', 'intern_role2_tag2: "عن بعد",')
js = js.replace('intern_role2_tag3: "مدفوع",', 'intern_role2_tag3: "مجاني",')
js = js.replace('intern_role3_tag3: "مدفوع",', 'intern_role3_tag3: "مجاني",')
js = js.replace('intern_role4_tag2: "هجين",', 'intern_role4_tag2: "عن بعد",')
js = js.replace('intern_role4_tag3: "مدفوع",', 'intern_role4_tag3: "مجاني",')

# Add intern_duration_1m to Arabic list
old_ar_durations = """        intern_duration_label: "المدة:",
        intern_duration_3m: "٣ أشهر",
        intern_duration_6m: "٦ أشهر","""

new_ar_durations = """        intern_duration_label: "المدة:",
        intern_duration_1m: "شهر واحد (١ أكتوبر - ١ نوفمبر)",
        intern_duration_3m: "٣ أشهر",
        intern_duration_6m: "٦ أشهر","""

js = js.replace(old_ar_durations, new_ar_durations)

with open("lang.js", "w", encoding="utf-8") as f:
    f.write(js)

print("lang.js successfully updated with new internship details!")


# 3. Update internships.html
with open("internships.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace duration tags
html = html.replace('data-i18n="intern_duration_3m">3 Months</b>', 'data-i18n="intern_duration_1m">1 Month (Oct 1 - Nov 1)</b>')

# Replace tag text in initial HTML
# Role 1 tags: Remote, Paid -> Remote, Free
html = html.replace('<span class="tag" data-i18n="intern_role1_tag3">Paid</span>', '<span class="tag" data-i18n="intern_role1_tag3">Free</span>')

# Role 2 tags: Hybrid, Paid -> Remote, Free
html = html.replace('<span class="tag" data-i18n="intern_role2_tag2">Hybrid</span>', '<span class="tag" data-i18n="intern_role2_tag2">Remote</span>')
html = html.replace('<span class="tag" data-i18n="intern_role2_tag3">Paid</span>', '<span class="tag" data-i18n="intern_role2_tag3">Free</span>')

# Role 3 tags: Remote, Paid -> Remote, Free
html = html.replace('<span class="tag" data-i18n="intern_role3_tag3">Paid</span>', '<span class="tag" data-i18n="intern_role3_tag3">Free</span>')

# Role 4 tags: Hybrid, Paid -> Remote, Free
html = html.replace('<span class="tag" data-i18n="intern_role4_tag2">Hybrid</span>', '<span class="tag" data-i18n="intern_role4_tag2">Remote</span>')
html = html.replace('<span class="tag" data-i18n="intern_role4_tag3">Paid</span>', '<span class="tag" data-i18n="intern_role4_tag3">Free</span>')

with open("internships.html", "w", encoding="utf-8") as f:
    f.write(html)

print("internships.html successfully updated with new duration and tags!")
