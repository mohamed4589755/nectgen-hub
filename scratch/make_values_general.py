# Update index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("\r\n", "\n")

# Replace card 1 title & desc
html = html.replace(
    '<h3 class="card-title" data-i18n="index_val1_title">Cutting-Edge AI Curriculums</h3>',
    '<h3 class="card-title" data-i18n="index_val1_title">Industry-Standard Curriculums</h3>'
)
html = html.replace(
    '<p class="card-desc" data-i18n="index_val1_desc">Master neural networks, large language models, and computer vision with tools used by world-class tech firms.</p>',
    '<p class="card-desc" data-i18n="index_val1_desc">Master modern coding frameworks, software architectures, and programming languages used by world-class tech firms.</p>'
)

# Replace card 2 title & desc
html = html.replace(
    '<h3 class="card-title" data-i18n="index_val2_title">Real-world Data Analytics</h3>',
    '<h3 class="card-title" data-i18n="index_val2_title">Practical Project Development</h3>'
)
html = html.replace(
    '<p class="card-desc" data-i18n="index_val2_desc">Translate complex unstructured datasets into actionable business intelligence using Python, SQL, and PowerBI.</p>',
    '<p class="card-desc" data-i18n="index_val2_desc">Build functional production-ready applications and engineering portfolios designed to demonstrate real-world competence.</p>'
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html updated successfully!")


# Update lang.js
with open("lang.js", "r", encoding="utf-8") as f:
    lang = f.read()

lang = lang.replace("\r\n", "\n")

# Replace English translations
lang = lang.replace(
    'index_val1_title: "Cutting-Edge AI Curriculums",',
    'index_val1_title: "Industry-Standard Curriculums",'
)
lang = lang.replace(
    'index_val1_desc: "Master neural networks, large language models, and computer vision with tools used by world-class tech firms.",',
    'index_val1_desc: "Master modern coding frameworks, software architectures, and programming languages used by world-class tech firms.",'
)
lang = lang.replace(
    'index_val2_title: "Real-world Data Analytics",',
    'index_val2_title: "Practical Project Development",'
)
lang = lang.replace(
    'index_val2_desc: "Translate complex unstructured datasets into actionable business intelligence using Python, SQL, and PowerBI.",',
    'index_val2_desc: "Build functional production-ready applications and engineering portfolios designed to demonstrate real-world competence.",'
)

# Replace Arabic translations
lang = lang.replace(
    'index_val1_title: "مناهج ذكاء اصطناعي رائدة",',
    'index_val1_title: "مناهج برمجية وتقنية رائدة",'
)
lang = lang.replace(
    'index_val1_desc: "احترف الشبكات العصبية، النماذج اللغوية الضخمة، والرؤية الحاسوبية باستخدام الأدوات المستعملة في كبرى شركات التقنية.",',
    'index_val1_desc: "أتقن أحدث أطر العمل البرمجية، وهندسة البرمجيات، ولغات البرمجة الأكثر طلباً في سوق العمل العالمي.",'
)
lang = lang.replace(
    'index_val2_title: "تحليلات بيانات واقعية",',
    'index_val2_title: "تطوير مشاريع تطبيقية عملية",'
)
lang = lang.replace(
    'index_val2_desc: "ترجم مجموعات البيانات المعقدة وغير المنظمة إلى رؤى أعمال قابلة للتنفيذ باستخدام Python و SQL و PowerBI.",',
    'index_val2_desc: "ابنِ تطبيقات ونظم متكاملة ومحافظ مشاريع برمجية تُثبت كفاءتك وجاهزيتك للشركات والوظائف الفعلية.",'
)

with open("lang.js", "w", encoding="utf-8") as f:
    f.write(lang)

print("lang.js updated successfully!")
