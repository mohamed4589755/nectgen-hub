import re

# 1. Update lang.js translations
with open("lang.js", "r", encoding="utf-8") as f:
    lang_content = f.read()

# Define the new english internship translations block
en_intern_translations = """        // Internships Page
        intern_tag: "Career Acceleration",
        intern_title: "Internship <span class='gradient-text'>Opportunities</span>",
        intern_sub: "Real tasks, real systems, and actual mentorship. Gain production-level experience that makes you stand out to global recruiters.",
        intern_list_title: "Open Roles",
        intern_list_sub: "Select a track matching your career aspirations. We accept candidates for our Summer and Autumn cohorts.",
        intern_role1_tag1: "AI & ML",
        intern_role1_tag2: "Remote",
        intern_role1_tag3: "Paid",
        intern_role1_title: "AI & Machine Learning Intern",
        intern_role1_desc: "Assist in evaluating, training, and deploying deep learning models. Work with NLP, computer vision, and RAG pipelines while setting up MLOps orchestration.",
        intern_duration_label: "Duration:",
        intern_duration_3m: "3 Months",
        intern_duration_6m: "6 Months",
        intern_apply_btn: "Apply Now",
        intern_role2_tag1: "Data Analytics",
        intern_role2_tag2: "Hybrid",
        intern_role2_tag3: "Paid",
        intern_role2_title: "Data Analytics Intern",
        intern_role2_desc: "Transform complex datasets into actionable business intelligence. Write efficient SQL queries, design interactive dashboards, and perform EDA with Python.",
        intern_role3_tag1: "Flutter Dev",
        intern_role3_tag2: "Remote",
        intern_role3_tag3: "Paid",
        intern_role3_title: "Flutter Developer Intern",
        intern_role3_desc: "Build beautiful, fluid cross-platform mobile apps for iOS and Android. Implement responsive UI widgets, state management, and API integrations.",
        intern_role4_tag1: "Front-End",
        intern_role4_tag2: "Hybrid",
        intern_role4_tag3: "Paid",
        intern_role4_title: "Front-End Web Developer Intern",
        intern_role4_desc: "Design and implement responsive, high-performance web user interfaces. Write clean, semantic markup, advanced CSS styling, and interactive JavaScript modules.",
        intern_benefits_tag: "Benefits","""

# Define the new arabic internship translations block
ar_intern_translations = """        // Internships Page
        intern_tag: "تسريع المسار المهني",
        intern_title: "فرص <span class='gradient-text'>التدريب العملي</span>",
        intern_sub: "مهام حقيقية، أنظمة إنتاجية واقعية، وتوجيه إرشادي فعلي. اكتسب خبرة عملية تبرزك أمام مسؤولي التوظيف العالميين.",
        intern_list_title: "الوظائف المتاحة",
        intern_list_sub: "اختر المسار الذي يتوافق مع تطلعاتك المهنية. نحن نقبل المرشحين لمجموعات الصيف والخريف.",
        intern_role1_tag1: "الذكاء الاصطناعي وتعلم الآلة",
        intern_role1_tag2: "عن بعد",
        intern_role1_tag3: "مدفوع",
        intern_role1_title: "متدرب الذكاء الاصطناعي وتعلم الآلة",
        intern_role1_desc: "ساعد في تقييم وتدريب ونشر نماذج التعلم العميق. اعمل مع معالجة اللغات الطبيعية ورؤية الكمبيوتر RAG مع إعداد تدفقات MLOps.",
        intern_duration_label: "المدة:",
        intern_duration_3m: "٣ أشهر",
        intern_duration_6m: "٦ أشهر",
        intern_apply_btn: "قدم الآن",
        intern_role2_tag1: "تحليل البيانات",
        intern_role2_tag2: "هجين",
        intern_role2_tag3: "مدفوع",
        intern_role2_title: "متدرب تحليل البيانات",
        intern_role2_desc: "حول البيانات المعقدة إلى رؤى أعمال قابلة للتنفيذ. اكتب استعلامات SQL فعالة، وصمم لوحات معلومات تفاعلية، وقم بإجراء تحليلات استكشافية بـ Python.",
        intern_role3_tag1: "تطوير فلاتر",
        intern_role3_tag2: "عن بعد",
        intern_role3_tag3: "مدفوع",
        intern_role3_title: "متدرب تطوير تطبيقات فلاتر (Flutter)",
        intern_role3_desc: "ابنِ تطبيقات موبايل جميلة وسريعة ومتقاطعة المنصات لنظامي iOS و Android. قم ببرمجة الواجهات وإدارة الحالة وربط الـ APIs.",
        intern_role4_tag1: "تطوير واجهات الويب",
        intern_role4_tag2: "هجين",
        intern_role4_tag3: "مدفوع",
        intern_role4_title: "متدرب تطوير واجهات الويب (Front-End)",
        intern_role4_desc: "صمم ونفذ واجهات ويب سريعة وعصرية ومتجاوبة بالكامل. اكتب أكواد نظيفة للهيكل والتنسيق وتفاعل مع Vanilla JS/React.",
        intern_benefits_tag: "المزايا","""

# Replace English block in memory
en_pattern = re.compile(r"// Internships Page.*?\n\s+intern_benefits_tag: \"Benefits\",", re.DOTALL)
lang_content = en_pattern.sub(en_intern_translations, lang_content)

# Replace Arabic block in memory
ar_pattern = re.compile(r"// Internships Page.*?\n\s+intern_benefits_tag: \"المزايا\",", re.DOTALL)
lang_content = ar_pattern.sub(ar_intern_translations, lang_content)

with open("lang.js", "w", encoding="utf-8") as f:
    f.write(lang_content)

print("lang.js translations updated!")


# 2. Update internships.html HTML markup to show 4 cards
with open("internships.html", "r", encoding="utf-8") as f:
    html = f.read()

# Locate the roles grid container in internships.html
old_grid_pattern = re.compile(r"<div class=\"cards-grid\">.*?<!-- Program Highlights / Benefits -->", re.DOTALL)

new_grid_html = """<div class="cards-grid">
                <!-- Role 1: AI & ML -->
                <div class="card glass-panel" id="roleCard1" style="padding: 0; overflow: hidden;">
                    <div class="card-image-wrap">
                        <img src="assets/intern_ml_engineer.jpg" alt="AI & Machine Learning Intern">
                    </div>
                    <div class="card-body" style="padding: 28px 24px; display: flex; flex-direction: column; flex-grow: 1;">
                        <div class="card-tags">
                            <span class="tag tag-highlight" data-i18n="intern_role1_tag1">AI & Machine Learning</span>
                            <span class="tag" data-i18n="intern_role1_tag2">Remote</span>
                            <span class="tag" data-i18n="intern_role1_tag3">Paid</span>
                        </div>
                        <h3 class="card-title" data-i18n="intern_role1_title">AI & Machine Learning Intern</h3>
                        <p class="card-desc" data-i18n="intern_role1_desc">
                            Assist in evaluating, training, and deploying deep learning models. Work with NLP, computer vision, and RAG pipelines while setting up MLOps orchestration.
                        </p>
                        <div class="card-footer" style="margin-top: auto; display: flex; align-items: center; justify-content: space-between; width: 100%;">
                            <span style="font-size: 0.85rem; color: var(--text-muted);"><span data-i18n="intern_duration_label">Duration:</span> <b data-i18n="intern_duration_3m">3 Months</b></span>
                            <a href="contact.html?role=AI_ML" class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem;" id="applyRole1" data-i18n="intern_apply_btn">Apply Now</a>
                        </div>
                    </div>
                </div>

                <!-- Role 2: Data Analytics -->
                <div class="card glass-panel" id="roleCard2" style="padding: 0; overflow: hidden;">
                    <div class="card-image-wrap">
                        <img src="assets/intern_data_analytics.jpg" alt="Data Analytics Intern">
                    </div>
                    <div class="card-body" style="padding: 28px 24px; display: flex; flex-direction: column; flex-grow: 1;">
                        <div class="card-tags">
                            <span class="tag tag-highlight" data-i18n="intern_role2_tag1">Data Analytics</span>
                            <span class="tag" data-i18n="intern_role2_tag2">Hybrid</span>
                            <span class="tag" data-i18n="intern_role2_tag3">Paid</span>
                        </div>
                        <h3 class="card-title" data-i18n="intern_role2_title">Data Analytics Intern</h3>
                        <p class="card-desc" data-i18n="intern_role2_desc">
                            Transform complex datasets into actionable business intelligence. Write efficient SQL queries, design interactive dashboards, and perform EDA with Python.
                        </p>
                        <div class="card-footer" style="margin-top: auto; display: flex; align-items: center; justify-content: space-between; width: 100%;">
                            <span style="font-size: 0.85rem; color: var(--text-muted);"><span data-i18n="intern_duration_label">Duration:</span> <b data-i18n="intern_duration_3m">3 Months</b></span>
                            <a href="contact.html?role=Data_Analytics" class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem;" id="applyRole2" data-i18n="intern_apply_btn">Apply Now</a>
                        </div>
                    </div>
                </div>

                <!-- Role 3: Flutter Developer -->
                <div class="card glass-panel" id="roleCard3" style="padding: 0; overflow: hidden;">
                    <div class="card-image-wrap">
                        <img src="assets/intern_flutter.jpg" alt="Flutter Developer Intern">
                    </div>
                    <div class="card-body" style="padding: 28px 24px; display: flex; flex-direction: column; flex-grow: 1;">
                        <div class="card-tags">
                            <span class="tag tag-highlight" data-i18n="intern_role3_tag1">Flutter Development</span>
                            <span class="tag" data-i18n="intern_role3_tag2">Remote</span>
                            <span class="tag" data-i18n="intern_role3_tag3">Paid</span>
                        </div>
                        <h3 class="card-title" data-i18n="intern_role3_title">Flutter Developer Intern</h3>
                        <p class="card-desc" data-i18n="intern_role3_desc">
                            Build beautiful, fluid cross-platform mobile apps for iOS and Android. Implement responsive UI widgets, state management, and API integrations.
                        </p>
                        <div class="card-footer" style="margin-top: auto; display: flex; align-items: center; justify-content: space-between; width: 100%;">
                            <span style="font-size: 0.85rem; color: var(--text-muted);"><span data-i18n="intern_duration_label">Duration:</span> <b data-i18n="intern_duration_3m">3 Months</b></span>
                            <a href="contact.html?role=Flutter_Dev" class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem;" id="applyRole3" data-i18n="intern_apply_btn">Apply Now</a>
                        </div>
                    </div>
                </div>

                <!-- Role 4: Front-End Web Developer -->
                <div class="card glass-panel" id="roleCard4" style="padding: 0; overflow: hidden;">
                    <div class="card-image-wrap">
                        <img src="assets/intern_frontend.jpg" alt="Front-End Web Developer Intern">
                    </div>
                    <div class="card-body" style="padding: 28px 24px; display: flex; flex-direction: column; flex-grow: 1;">
                        <div class="card-tags">
                            <span class="tag tag-highlight" data-i18n="intern_role4_tag1">Front-End Web Dev</span>
                            <span class="tag" data-i18n="intern_role4_tag2">Hybrid</span>
                            <span class="tag" data-i18n="intern_role4_tag3">Paid</span>
                        </div>
                        <h3 class="card-title" data-i18n="intern_role4_title">Front-End Web Developer Intern</h3>
                        <p class="card-desc" data-i18n="intern_role4_desc">
                            Design and implement responsive, high-performance web user interfaces. Write clean, semantic markup, advanced CSS styling, and interactive JavaScript modules.
                        </p>
                        <div class="card-footer" style="margin-top: auto; display: flex; align-items: center; justify-content: space-between; width: 100%;">
                            <span style="font-size: 0.85rem; color: var(--text-muted);"><span data-i18n="intern_duration_label">Duration:</span> <b data-i18n="intern_duration_3m">3 Months</b></span>
                            <a href="contact.html?role=Frontend_Dev" class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem;" id="applyRole4" data-i18n="intern_apply_btn">Apply Now</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Program Highlights / Benefits -->"""

html = old_grid_pattern.sub(new_grid_html, html)

with open("internships.html", "w", encoding="utf-8") as f:
    f.write(html)

print("internships.html successfully updated with 4 tracks!")
