with open("lang.js", "r", encoding="utf-8") as f:
    js = f.read()

# Normalize line endings
js = js.replace("\r\n", "\n")

# English Replacements
old_en_footer = 'footer_desc: "Empowering creators, students, and engineers in data analytics and artificial intelligence. Shaping tomorrow, today.",'
new_en_footer = 'footer_desc: "Empowering creators, students, and engineers in data analytics, artificial intelligence, web development, and Flutter. Shaping tomorrow, today.",'

old_en_hero = 'index_hero_sub: "At NextGen Institute, we bridge the gap between academic theory and practical innovation. Join our immersive programs in AI, Machine Learning, and Data Analytics to shape the future of technology.",'
new_en_hero = 'index_hero_sub: "At NextGen Institute, we bridge the gap between academic theory and practical innovation. Join our immersive programs in AI, Machine Learning, Data Analytics, Web Development, and Flutter to shape the future of technology.",'

js = js.replace(old_en_footer, new_en_footer)
js = js.replace(old_en_hero, new_en_hero)

# Arabic Replacements
old_ar_footer = 'footer_desc: "تمكين المبتكرين والطلاب والمهندسين في مجالات تحليل البيانات والذكاء الاصطناعي. نشكّل المستقبل اليوم.",'
new_ar_footer = 'footer_desc: "تمكين المبتكرين والطلاب والمهندسين في مجالات تحليل البيانات، الذكاء الاصطناعي، تطوير الويب، وفلاتر. نشكّل المستقبل اليوم.",'

old_ar_hero = 'index_hero_sub: "في NextGen Institute، نسد الفجوة بين النظريات الأكاديمية والابتكار العملي. انضم إلى برامجنا المكثفة في الذكاء الاصطناعي، تعلم الآلة، وتحليل البيانات لتشكيل مستقبل التكنولوجيا.",'
new_ar_hero = 'index_hero_sub: "في NextGen Institute، نسد الفجوة بين النظريات الأكاديمية والابتكار العملي. انضم إلى برامجنا المكثفة في الذكاء الاصطناعي، تعلم الآلة، تحليل البيانات، تطوير الويب، وفلاتر لتشكيل مستقبل التكنولوجيا.",'

js = js.replace(old_ar_footer, new_ar_footer)
js = js.replace(old_ar_hero, new_ar_hero)

with open("lang.js", "w", encoding="utf-8") as f:
    f.write(js)

print("lang.js updated with Web Development and Flutter in all descriptions!")
