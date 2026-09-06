import re

# 1. Update bootcamps.html
with open("bootcamps.html", "r", encoding="utf-8") as f:
    html = f.read()

# Define the new bootcamps grid section html
new_grid_html = """    <!-- Bootcamps Grid Section -->
    <section class="fade-up section-padding">
        <div class="container">
            <div class="section-title-wrap text-center">
                <h2 class="section-title" data-i18n="boot_grid_title">Curriculum & Programs</h2>
                <p class="section-subtitle" data-i18n="boot_grid_sub">Choose your learning path. Our cohort-based bootcamps feature live interactive sessions, hands-on lab projects, and certified graduation certificates.</p>
            </div>

            <div class="cards-grid">
                <!-- Card 1: AI & ML Bootcamp -->
                <div class="card glass-panel" id="bootCard1" style="padding: 0; overflow: hidden;">
                    <div class="card-image-wrap">
                        <img src="assets/intern_ml_engineer.jpg?v=8" alt="AI & Machine Learning Bootcamp">
                    </div>
                    <div class="card-body" style="padding: 28px 24px; display: flex; flex-direction: column; flex-grow: 1;">
                        <div class="card-tags">
                            <span class="tag tag-highlight" data-i18n="boot_role1_tag1">AI & Machine Learning</span>
                            <span class="tag" data-i18n="boot_role1_tag2">Online</span>
                            <span class="tag" data-i18n="boot_role1_tag3">Certified</span>
                        </div>
                        <h3 class="card-title" data-i18n="boot_role1_title">AI & Machine Learning Bootcamp</h3>
                        <p class="card-desc" data-i18n="boot_role1_desc">
                            Master mathematical foundations, PyTorch, supervised learning algorithms, neural network design, computer vision, NLP, and model deployment using FastAPI and Docker.
                        </p>
                        <div class="card-footer" style="margin-top: auto; display: flex; align-items: center; justify-content: space-between; width: 100%;">
                            <span style="font-size: 0.85rem; color: var(--text-muted);"><span data-i18n="boot_duration_label">Duration:</span> <b data-i18n="boot_duration_3m">3 Months</b></span>
                            <a href="contact.html?bootcamp=AI_ML" class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem;" id="applyBoot1" data-i18n="boot_apply_btn">Register Now</a>
                        </div>
                    </div>
                </div>

                <!-- Card 2: Data Analytics Bootcamp -->
                <div class="card glass-panel" id="bootCard2" style="padding: 0; overflow: hidden;">
                    <div class="card-image-wrap">
                        <img src="assets/intern_data_analytics.jpg?v=8" alt="Data Analytics Bootcamp">
                    </div>
                    <div class="card-body" style="padding: 28px 24px; display: flex; flex-direction: column; flex-grow: 1;">
                        <div class="card-tags">
                            <span class="tag tag-highlight" data-i18n="boot_role2_tag1">Data Analytics</span>
                            <span class="tag" data-i18n="boot_role2_tag2">Online</span>
                            <span class="tag" data-i18n="boot_role2_tag3">Certified</span>
                        </div>
                        <h3 class="card-title" data-i18n="boot_role2_title">Data Analytics Bootcamp</h3>
                        <p class="card-desc" data-i18n="boot_role2_desc">
                            Transform into a business intelligence expert. Write advanced SQL queries, design interactive dashboards in PowerBI/Tableau, and wrangle data using Pandas and NumPy.
                        </p>
                        <div class="card-footer" style="margin-top: auto; display: flex; align-items: center; justify-content: space-between; width: 100%;">
                            <span style="font-size: 0.85rem; color: var(--text-muted);"><span data-i18n="boot_duration_label">Duration:</span> <b data-i18n="boot_duration_3m">3 Months</b></span>
                            <a href="contact.html?bootcamp=Data_Analytics" class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem;" id="applyBoot2" data-i18n="boot_apply_btn">Register Now</a>
                        </div>
                    </div>
                </div>

                <!-- Card 3: Flutter Developer Bootcamp -->
                <div class="card glass-panel" id="bootCard3" style="padding: 0; overflow: hidden;">
                    <div class="card-image-wrap">
                        <img src="assets/intern_flutter.jpg?v=9" alt="Flutter Developer Bootcamp">
                    </div>
                    <div class="card-body" style="padding: 28px 24px; display: flex; flex-direction: column; flex-grow: 1;">
                        <div class="card-tags">
                            <span class="tag tag-highlight" data-i18n="boot_role3_tag1">Flutter Development</span>
                            <span class="tag" data-i18n="boot_role3_tag2">Online</span>
                            <span class="tag" data-i18n="boot_role3_tag3">Certified</span>
                        </div>
                        <h3 class="card-title" data-i18n="boot_role3_title">Flutter Developer Bootcamp</h3>
                        <p class="card-desc" data-i18n="boot_role3_desc">
                            Build fully functional native iOS and Android apps. Master Dart programming language, fluid UI layout widgets, advanced state management, and web API integration.
                        </p>
                        <div class="card-footer" style="margin-top: auto; display: flex; align-items: center; justify-content: space-between; width: 100%;">
                            <span style="font-size: 0.85rem; color: var(--text-muted);"><span data-i18n="boot_duration_label">Duration:</span> <b data-i18n="boot_duration_3m">3 Months</b></span>
                            <a href="contact.html?bootcamp=Flutter_Dev" class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem;" id="applyBoot3" data-i18n="boot_apply_btn">Register Now</a>
                        </div>
                    </div>
                </div>

                <!-- Card 4: Front-End Web Developer Bootcamp -->
                <div class="card glass-panel" id="bootCard4" style="padding: 0; overflow: hidden;">
                    <div class="card-image-wrap">
                        <img src="assets/intern_frontend.jpg?v=8" alt="Front-End Web Developer Bootcamp">
                    </div>
                    <div class="card-body" style="padding: 28px 24px; display: flex; flex-direction: column; flex-grow: 1;">
                        <div class="card-tags">
                            <span class="tag tag-highlight" data-i18n="boot_role4_tag1">Front-End Web Dev</span>
                            <span class="tag" data-i18n="boot_role4_tag2">Online</span>
                            <span class="tag" data-i18n="boot_role4_tag3">Certified</span>
                        </div>
                        <h3 class="card-title" data-i18n="boot_role4_title">Front-End Web Developer Bootcamp</h3>
                        <p class="card-desc" data-i18n="boot_role4_desc">
                            Create responsive, pixel-perfect user interfaces. Learn advanced CSS animations, flexbox/grid layouts, semantic HTML5, DOM manipulation, and interactive JS modules.
                        </p>
                        <div class="card-footer" style="margin-top: auto; display: flex; align-items: center; justify-content: space-between; width: 100%;">
                            <span style="font-size: 0.85rem; color: var(--text-muted);"><span data-i18n="boot_duration_label">Duration:</span> <b data-i18n="boot_duration_3m">3 Months</b></span>
                            <a href="contact.html?bootcamp=Frontend_Dev" class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem;" id="applyBoot4" data-i18n="boot_apply_btn">Register Now</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>"""

# Using regex to find the entire Schedule Table Section and replace it
pattern = r"<!-- Schedule Table Section -->.*?<!-- FAQ Section -->"
match = re.search(pattern, html, re.DOTALL)
if match:
    html = re.sub(pattern, new_grid_html + "\n\n    <!-- FAQ Section -->", html, flags=re.DOTALL)
    print("bootcamps.html schedule section replaced successfully!")
else:
    print("Error: Could not find the Schedule Table Section in bootcamps.html!")

with open("bootcamps.html", "w", encoding="utf-8") as f:
    f.write(html)


# 2. Update lang.js
with open("lang.js", "r", encoding="utf-8") as f:
    js = f.read()

# Define English translations
en_replace = """boot_sub: "From foundation to production. Choose a path, roll up your sleeves, and master the technical frameworks defining our century.",
        boot_grid_title: "Curriculum & Programs",
        boot_grid_sub: "Choose your learning path. Our cohort-based bootcamps feature live interactive sessions, hands-on lab projects, and certified graduation certificates.",
        boot_role1_tag1: "AI & ML",
        boot_role1_tag2: "Online",
        boot_role1_tag3: "Certified",
        boot_role1_title: "AI & Machine Learning Bootcamp",
        boot_role1_desc: "Master mathematical foundations, PyTorch, supervised learning algorithms, neural network design, computer vision, NLP, and model deployment using FastAPI and Docker.",
        boot_role2_tag1: "Data Analytics",
        boot_role2_tag2: "Online",
        boot_role2_tag3: "Certified",
        boot_role2_title: "Data Analytics Bootcamp",
        boot_role2_desc: "Transform into a business intelligence expert. Write advanced SQL queries, design interactive dashboards in PowerBI/Tableau, and wrangle data using Pandas and NumPy.",
        boot_role3_tag1: "Flutter Dev",
        boot_role3_tag2: "Online",
        boot_role3_tag3: "Certified",
        boot_role3_title: "Flutter Developer Bootcamp",
        boot_role3_desc: "Build fully functional native iOS and Android apps. Master Dart programming language, fluid UI layout widgets, advanced state management, and web API integration.",
        boot_role4_tag1: "Front-End",
        boot_role4_tag2: "Online",
        boot_role4_tag3: "Certified",
        boot_role4_title: "Front-End Web Developer Bootcamp",
        boot_role4_desc: "Create responsive, pixel-perfect user interfaces. Learn advanced CSS animations, flexbox/grid layouts, semantic HTML5, DOM manipulation, and interactive JS modules.",
        boot_duration_label: "Duration:",
        boot_duration_3m: "3 Months",
        boot_apply_btn: "Register Now","""

# Define Arabic translations
ar_replace = """boot_sub: "من الأساسيات إلى بيئة الإنتاج الفعلي. اختر مساراً، وابدأ التعلم، واحترف الأطر التقنية التي ترسم ملامح عصرنا الحالي.",
        boot_grid_title: "المناهج والبرامج التدريبية",
        boot_grid_sub: "اختر مسار التعلم الخاص بك. تتميز معسكراتنا بنظام المجموعات التفاعلية، والمشاريع المعملية التطبيقية، وشهادات تخرج معتمدة.",
        boot_role1_tag1: "الذكاء الاصطناعي وتعلم الآلة",
        boot_role1_tag2: "عبر الإنترنت",
        boot_role1_tag3: "شهادة معتمدة",
        boot_role1_title: "معسكر الذكاء الاصطناعي وتعلم الآلة",
        boot_role1_desc: "أتقن الأسس الرياضية، مكتبة PyTorch، خوارزميات التعلم الخاضع للإشراف، تصميم الشبكات العصبية، رؤية الكمبيوتر، معالجة اللغات الطبيعية، ونشر النماذج باستخدام FastAPI و Docker.",
        boot_role2_tag1: "تحليل البيانات",
        boot_role2_tag2: "عبر الإنترنت",
        boot_role2_tag3: "شهادة معتمدة",
        boot_role2_title: "معسكر تحليل البيانات",
        boot_role2_desc: "تحوّل إلى خبير في ذكاء الأعمال. اكتب استعلامات SQL متقدمة، وصمم لوحات معلومات تفاعلية في PowerBI/Tableau، وعالج البيانات باستخدام Pandas و NumPy.",
        boot_role3_tag1: "تطوير فلاتر",
        boot_role3_tag2: "عبر الإنترنت",
        boot_role3_tag3: "شهادة معتمدة",
        boot_role3_title: "معسكر تطوير تطبيقات فلاتر (Flutter)",
        boot_role3_desc: "ابنِ تطبيقات أصلية تعمل بكامل طاقتها لنظامي iOS و Android. أتقن لغة البرمجة Dart، تخطيط الواجهات التفاعلية، إدارة الحالة المتقدمة، ودمج واجهات البرمجة APIs.",
        boot_role4_tag1: "تطوير واجهات الويب",
        boot_role4_tag2: "عبر الإنترنت",
        boot_role4_tag3: "شهادة معتمدة",
        boot_role4_title: "معسكر تطوير واجهات الويب (Front-End)",
        boot_role4_desc: "أنشئ واجهات مستخدم متجاوبة وبكسل مثالي. تعلم الرسوم المتحركة المتقدمة بـ CSS، تخطيطات flexbox/grid، هيكلية HTML5، ومعالجة الـ DOM، ووحدات Vanilla JS التفاعلية.",
        boot_duration_label: "المدة:",
        boot_duration_3m: "٣ أشهر",
        boot_apply_btn: "سجل الآن","""

# Let's perform key replacements in lang.js
js = js.replace('boot_sub: "From foundation to production. Choose a path, roll up your sleeves, and master the technical frameworks defining our century.",', en_replace)
js = js.replace('boot_sub: "من الأساسيات إلى بيئة الإنتاج الفعلي. اختر مساراً، وابدأ التعلم، واحترف الأطر التقنية التي ترسم ملامح عصرنا الحالي.",', ar_replace)

with open("lang.js", "w", encoding="utf-8") as f:
    f.write(js)

print("lang.js successfully updated with bootcamps translations!")
