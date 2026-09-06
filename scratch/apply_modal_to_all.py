import re

# 1. Update lang.js with new translations for diplomas and form keys
with open("lang.js", "r", encoding="utf-8") as f:
    js = f.read()

# Define English translations to insert
en_replace = """boot_apply_btn: "Register Now",
        diploma_grid_title: "Available Specialization Tracks",
        diploma_grid_sub: "Choose a professional track. Each diploma includes weekly coding labs, live case studies, and a final capstone reviewed by industry experts.",
        diploma_role1_tag1: "AI & ML",
        diploma_role1_tag2: "Online",
        diploma_role1_tag3: "Co-Op Placement",
        diploma_role1_title: "AI & Machine Learning Diploma",
        diploma_role1_desc: "A comprehensive specialization covering PyTorch, deep neural networks, computer vision algorithms, large language models (LLMs), fine-tuning techniques, and MLOps pipelines.",
        diploma_role2_tag1: "Data Analytics",
        diploma_role2_tag2: "Online",
        diploma_role2_tag3: "Co-Op Placement",
        diploma_role2_title: "Data Analytics Diploma",
        diploma_role2_desc: "Master the core methods of enterprise business intelligence. Learn SQL database design, Python data analysis, PowerBI dashboard orchestration, and cloud warehousing.",
        diploma_role3_tag1: "Flutter Dev",
        diploma_role3_tag2: "Online",
        diploma_role3_tag3: "Co-Op Placement",
        diploma_role3_title: "Flutter Developer Diploma",
        diploma_role3_desc: "Learn Dart programming, app state management (Bloc/Provider), hardware native features integration, responsive layouts, API bindings, and app store deployment.",
        diploma_role4_tag1: "Front-End",
        diploma_role4_tag2: "Online",
        diploma_role4_tag3: "Co-Op Placement",
        diploma_role4_title: "Front-End Web Developer Diploma",
        diploma_role4_desc: "Master modern UI engineering. Build fully responsive portals using semantic HTML5, advanced CSS, flexbox/grid layout design, JavaScript DOM bindings, and React frameworks.",
        diploma_duration_label: "Duration:",
        diploma_duration_6m: "6 Months",
        diploma_apply_btn: "Register Now",
        boot_grid_title: "Curriculum & Programs",
        boot_grid_sub: "Choose your learning path. Our cohort-based bootcamps feature live interactive sessions, hands-on lab projects, and certified graduation certificates.","""

js = js.replace('boot_apply_btn: "Register Now",', en_replace)

# Define Arabic translations to insert
ar_replace = """boot_apply_btn: "سجل الآن",
        diploma_grid_title: "مسارات التخصص المتاحة",
        diploma_grid_sub: "اختر مسارًا مهنيًا. تتضمن كل دبلومة مختبرات برمجية أسبوعية، ودراسات حالة حية، ومراجعة لمشروع تخرجك النهائي من قبل خبراء الصناعة.",
        diploma_role1_tag1: "الذكاء الاصطناعي وتعلم الآلة",
        diploma_role1_tag2: "عبر الإنترنت",
        diploma_role1_tag3: "توظيف تدريبي",
        diploma_role1_title: "دبلوم الذكاء الاصطناعي وتعلم الآلة",
        diploma_role1_desc: "تخصص شامل يغطي مكتبة PyTorch، الشبكات العصبية العميقة، خوارزميات الرؤية الحاسوبية، النماذج اللغوية الضخمة (LLMs)، تقنيات الضبط الدقيق، وتدفقات MLOps.",
        diploma_role2_tag1: "تحليل البيانات",
        diploma_role2_tag2: "عبر الإنترنت",
        diploma_role2_tag3: "توظيف تدريبي",
        diploma_role2_title: "دبلوم تحليل البيانات",
        diploma_role2_desc: "أتقن الطرق الأساسية لذكاء الأعمال على مستوى المؤسسات. تعلم تصميم قواعد بيانات SQL، تحليل البيانات بـ Python، وإدارة لوحات معلومات PowerBI.",
        diploma_role3_tag1: "تطوير فلاتر",
        diploma_role3_tag2: "عبر الإنترنت",
        diploma_role3_tag3: "توظيف تدريبي",
        diploma_role3_title: "دبلوم تطوير تطبيقات فلاتر (Flutter)",
        diploma_role3_desc: "تعلم برمجة Dart، إدارة حالة التطبيق (Bloc/Provider)، دمج الميزات الأصلية للهاتف، التخطيطات المتجاوبة، وربط الـ APIs، ونشر التطبيق على المتاجر.",
        diploma_role4_tag1: "تطوير واجهات الويب",
        diploma_role4_tag2: "عبر الإنترنت",
        diploma_role4_tag3: "توظيف تدريبي",
        diploma_role4_title: "دبلوم تطوير واجهات الويب (Front-End)",
        diploma_role4_desc: "أتقن هندسة واجهات المستخدم الحديثة. ابنِ بوابات ويب متجاوبة بالكامل باستخدام هيكلية HTML5، تنسيقات CSS المتقدمة، و Vanilla JS ومكتبة React.",
        diploma_duration_label: "المدة:",
        diploma_duration_6m: "٦ أشهر",
        diploma_apply_btn: "سجل الآن",
        boot_grid_title: "المناهج والبرامج التدريبية",
        boot_grid_sub: "اختر مسار التعلم الخاص بك. تتميز معسكراتنا بنظام المجموعات التفاعلية، والمشاريع المعملية التطبيقية، وشهادات تخرج معتمدة.","""

js = js.replace('boot_apply_btn: "سجل الآن",', ar_replace)

with open("lang.js", "w", encoding="utf-8") as f:
    f.write(js)

print("lang.js successfully updated with diplomas translation keys!")


# 2. Update diplomas.html list layout to 4-card grid
with open("diplomas.html", "r", encoding="utf-8") as f:
    html_dip = f.read()

new_diplomas_grid = """    <!-- Diplomas List Section -->
    <section class="fade-up section-padding">
        <div class="container">
            <div class="section-title-wrap text-center">
                <h2 class="section-title" data-i18n="diploma_grid_title">Available Specialization Tracks</h2>
                <p class="section-subtitle" data-i18n="diploma_grid_sub">Choose a professional track. Each diploma includes weekly coding labs, live case studies, and a final capstone reviewed by industry experts.</p>
            </div>

            <div class="cards-grid">
                <!-- Card 1: AI & ML Diploma -->
                <div class="card glass-panel" id="diplomaCard1" style="padding: 0; overflow: hidden;">
                    <div class="card-image-wrap">
                        <img src="assets/intern_ml_engineer.jpg?v=8" alt="AI & Machine Learning Diploma">
                    </div>
                    <div class="card-body" style="padding: 28px 24px; display: flex; flex-direction: column; flex-grow: 1;">
                        <div class="card-tags">
                            <span class="tag tag-highlight" data-i18n="diploma_role1_tag1">AI & Machine Learning</span>
                            <span class="tag" data-i18n="diploma_role1_tag2">Online</span>
                            <span class="tag" data-i18n="diploma_role1_tag3">Co-Op Placement</span>
                        </div>
                        <h3 class="card-title" data-i18n="diploma_role1_title">AI & Machine Learning Diploma</h3>
                        <p class="card-desc" data-i18n="diploma_role1_desc">
                            A comprehensive specialization covering PyTorch, deep neural networks, computer vision algorithms, large language models (LLMs), fine-tuning techniques, and MLOps pipelines.
                        </p>
                        <div class="card-footer" style="margin-top: auto; display: flex; align-items: center; justify-content: space-between; width: 100%;">
                            <span style="font-size: 0.85rem; color: var(--text-muted);"><span data-i18n="diploma_duration_label">Duration:</span> <b data-i18n="diploma_duration_6m">6 Months</b></span>
                            <a href="contact.html?diploma=AI_ML" class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem;" id="applyDiploma1" data-i18n="diploma_apply_btn">Register Now</a>
                        </div>
                    </div>
                </div>

                <!-- Card 2: Data Analytics Diploma -->
                <div class="card glass-panel" id="diplomaCard2" style="padding: 0; overflow: hidden;">
                    <div class="card-image-wrap">
                        <img src="assets/intern_data_analytics.jpg?v=8" alt="Data Analytics Diploma">
                    </div>
                    <div class="card-body" style="padding: 28px 24px; display: flex; flex-direction: column; flex-grow: 1;">
                        <div class="card-tags">
                            <span class="tag tag-highlight" data-i18n="diploma_role2_tag1">Data Analytics</span>
                            <span class="tag" data-i18n="diploma_role2_tag2">Online</span>
                            <span class="tag" data-i18n="diploma_role2_tag3">Co-Op Placement</span>
                        </div>
                        <h3 class="card-title" data-i18n="diploma_role2_title">Data Analytics Diploma</h3>
                        <p class="card-desc" data-i18n="diploma_role2_desc">
                            Master the core methods of enterprise business intelligence. Learn SQL database design, Python data analysis, PowerBI dashboard orchestration, and cloud warehousing.
                        </p>
                        <div class="card-footer" style="margin-top: auto; display: flex; align-items: center; justify-content: space-between; width: 100%;">
                            <span style="font-size: 0.85rem; color: var(--text-muted);"><span data-i18n="diploma_duration_label">Duration:</span> <b data-i18n="diploma_duration_6m">6 Months</b></span>
                            <a href="contact.html?diploma=Data_Analytics" class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem;" id="applyDiploma2" data-i18n="diploma_apply_btn">Register Now</a>
                        </div>
                    </div>
                </div>

                <!-- Card 3: Flutter Developer Diploma -->
                <div class="card glass-panel" id="diplomaCard3" style="padding: 0; overflow: hidden;">
                    <div class="card-image-wrap">
                        <img src="assets/intern_flutter.jpg?v=9" alt="Flutter Developer Diploma">
                    </div>
                    <div class="card-body" style="padding: 28px 24px; display: flex; flex-direction: column; flex-grow: 1;">
                        <div class="card-tags">
                            <span class="tag tag-highlight" data-i18n="diploma_role3_tag1">Flutter Development</span>
                            <span class="tag" data-i18n="diploma_role3_tag2">Online</span>
                            <span class="tag" data-i18n="diploma_role3_tag3">Co-Op Placement</span>
                        </div>
                        <h3 class="card-title" data-i18n="diploma_role3_title">Flutter Developer Diploma</h3>
                        <p class="card-desc" data-i18n="diploma_role3_desc">
                            Learn Dart programming, app state management (Bloc/Provider), hardware native features integration, responsive layouts, API bindings, and app store deployment.
                        </p>
                        <div class="card-footer" style="margin-top: auto; display: flex; align-items: center; justify-content: space-between; width: 100%;">
                            <span style="font-size: 0.85rem; color: var(--text-muted);"><span data-i18n="diploma_duration_label">Duration:</span> <b data-i18n="diploma_duration_6m">6 Months</b></span>
                            <a href="contact.html?diploma=Flutter_Dev" class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem;" id="applyDiploma3" data-i18n="diploma_apply_btn">Register Now</a>
                        </div>
                    </div>
                </div>

                <!-- Card 4: Front-End Web Developer Diploma -->
                <div class="card glass-panel" id="diplomaCard4" style="padding: 0; overflow: hidden;">
                    <div class="card-image-wrap">
                        <img src="assets/intern_frontend.jpg?v=8" alt="Front-End Web Developer Diploma">
                    </div>
                    <div class="card-body" style="padding: 28px 24px; display: flex; flex-direction: column; flex-grow: 1;">
                        <div class="card-tags">
                            <span class="tag tag-highlight" data-i18n="diploma_role4_tag1">Front-End Web Dev</span>
                            <span class="tag" data-i18n="diploma_role4_tag2">Online</span>
                            <span class="tag" data-i18n="diploma_role4_tag3">Co-Op Placement</span>
                        </div>
                        <h3 class="card-title" data-i18n="diploma_role4_title">Front-End Web Developer Diploma</h3>
                        <p class="card-desc" data-i18n="diploma_role4_desc">
                            Master modern UI engineering. Build fully responsive portals using semantic HTML5, advanced CSS, flexbox/grid layout design, JavaScript DOM bindings, and React frameworks.
                        </p>
                        <div class="card-footer" style="margin-top: auto; display: flex; align-items: center; justify-content: space-between; width: 100%;">
                            <span style="font-size: 0.85rem; color: var(--text-muted);"><span data-i18n="diploma_duration_label">Duration:</span> <b data-i18n="diploma_duration_6m">6 Months</b></span>
                            <a href="contact.html?diploma=Frontend_Dev" class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem;" id="applyDiploma4" data-i18n="diploma_apply_btn">Register Now</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>"""

# Replace the diplomas list in diplomas.html using regex
pattern_dip = r"<!-- Diplomas List Section -->.*?<!-- Why Diplomas Section -->"
match_dip = re.search(pattern_dip, html_dip, re.DOTALL)
if match_dip:
    html_dip = re.sub(pattern_dip, new_diplomas_grid + "\n\n    <!-- Why Diplomas Section -->", html_dip, flags=re.DOTALL)
    print("diplomas.html list section replaced with 4-card grid successfully!")
else:
    print("Error: Could not find Diplomas List Section in diplomas.html!")

# Define modal markup and script for diplomas.html
dip_modal_markup = """
    <!-- Registration Modal -->
    <div class="modal-overlay" id="registrationModal">
        <div class="modal-content glass-panel">
            <button class="modal-close" id="modalCloseBtn" aria-label="Close Modal">&times;</button>
            <h3 class="modal-title" id="modalTitle">Register for Diploma</h3>
            <p class="modal-subtitle" id="modalSubtitle" data-i18n="form_modal_sub">Please fill out the form below to apply.</p>
            
            <form class="modal-form" id="diplomaForm">
                <input type="hidden" id="selectedRole" name="role">
                
                <div class="form-group">
                    <label for="fullName" data-i18n="form_name_label">Full Name</label>
                    <input type="text" id="fullName" required placeholder="Enter your full name">
                </div>
                
                <div class="form-group">
                    <label for="emailAddress" data-i18n="form_email_label">Email Address</label>
                    <input type="email" id="emailAddress" required placeholder="Enter your email">
                </div>
                
                <div class="form-group">
                    <label for="phoneNumber" data-i18n="form_phone_label">Phone Number</label>
                    <input type="tel" id="phoneNumber" required placeholder="Enter your phone number">
                </div>

                <div class="form-group">
                    <label for="university" data-i18n="form_uni_label">University & Major</label>
                    <input type="text" id="university" required placeholder="e.g. Cairo University, Computer Science">
                </div>

                <div class="form-group">
                    <label for="cvLink" data-i18n="form_cv_label">Resume Link (Google Drive/Dropbox)</label>
                    <input type="url" id="cvLink" required placeholder="https://drive.google.com/...">
                </div>
                
                <button type="submit" class="btn btn-primary w-100" style="margin-top: 15px; width: 100%;" data-i18n="form_submit_btn">Submit Application</button>
            </form>
            
            <!-- Success Message -->
            <div class="form-success" id="formSuccess">
                <svg class="success-icon" viewBox="0 0 24 24" width="48" height="48" fill="none" stroke="var(--accent-blue)" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="margin: 0 auto 16px;"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
                <h4 data-i18n="form_success_title">Application Submitted!</h4>
                <p data-i18n="form_success_desc">Thank you for applying. Our team will review your CV and contact you soon.</p>
                <button class="btn btn-secondary" id="successCloseBtn" style="margin-top: 15px; padding: 8px 24px;" data-i18n="form_close_btn">Close</button>
            </div>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const modal = document.getElementById('registrationModal');
            const form = document.getElementById('diplomaForm');
            const successScreen = document.getElementById('formSuccess');
            const closeBtn = document.getElementById('modalCloseBtn');
            const successCloseBtn = document.getElementById('successCloseBtn');
            const modalTitle = document.getElementById('modalTitle');
            const selectedRoleInput = document.getElementById('selectedRole');
            
            // Open modal on Apply button click
            document.querySelectorAll('[id^="applyDiploma"]').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    e.preventDefault();
                    
                    const card = btn.closest('.card');
                    const titleText = card.querySelector('.card-title').textContent;
                    const diplomaId = btn.getAttribute('href').split('diploma=')[1] || '';
                    
                    selectedRoleInput.value = diplomaId;
                    modalTitle.textContent = titleText;
                    
                    form.reset();
                    form.style.display = 'block';
                    successScreen.classList.remove('show');
                    
                    modal.classList.add('show');
                    document.body.style.overflow = 'hidden';
                });
            });
            
            const closeModal = () => {
                modal.classList.remove('show');
                document.body.style.overflow = '';
            };
            
            closeBtn.addEventListener('click', closeModal);
            successCloseBtn.addEventListener('click', closeModal);
            
            modal.addEventListener('click', (e) => {
                if (e.target === modal) {
                    closeModal();
                }
            });
            
            form.addEventListener('submit', (e) => {
                e.preventDefault();
                
                const applicationData = {
                    diploma: selectedRoleInput.value,
                    name: document.getElementById('fullName').value,
                    email: document.getElementById('emailAddress').value,
                    phone: document.getElementById('phoneNumber').value,
                    uni: document.getElementById('university').value,
                    cv: document.getElementById('cvLink').value,
                    timestamp: new Date().toISOString()
                };
                
                console.log("Submitting Diploma Application:", applicationData);
                
                form.style.display = 'none';
                successScreen.classList.add('show');
            });
        });
    </script>
"""

# Append modal and scripts block right before </body> tag in diplomas.html
html_dip = html_dip.replace('    <button class="back-to-top" id="backToTop" aria-label="Back to Top">↑</button>', dip_modal_markup + '\n    <button class="back-to-top" id="backToTop" aria-label="Back to Top">↑</button>')

with open("diplomas.html", "w", encoding="utf-8") as f:
    f.write(html_dip)

print("diplomas.html successfully updated with modal script and grid!")


# 3. Update bootcamps.html with registration modal
with open("bootcamps.html", "r", encoding="utf-8") as f:
    html_boot = f.read()

boot_modal_markup = """
    <!-- Registration Modal -->
    <div class="modal-overlay" id="registrationModal">
        <div class="modal-content glass-panel">
            <button class="modal-close" id="modalCloseBtn" aria-label="Close Modal">&times;</button>
            <h3 class="modal-title" id="modalTitle">Register for Bootcamp</h3>
            <p class="modal-subtitle" id="modalSubtitle" data-i18n="form_modal_sub">Please fill out the form below to apply.</p>
            
            <form class="modal-form" id="bootcampForm">
                <input type="hidden" id="selectedRole" name="role">
                
                <div class="form-group">
                    <label for="fullName" data-i18n="form_name_label">Full Name</label>
                    <input type="text" id="fullName" required placeholder="Enter your full name">
                </div>
                
                <div class="form-group">
                    <label for="emailAddress" data-i18n="form_email_label">Email Address</label>
                    <input type="email" id="emailAddress" required placeholder="Enter your email">
                </div>
                
                <div class="form-group">
                    <label for="phoneNumber" data-i18n="form_phone_label">Phone Number</label>
                    <input type="tel" id="phoneNumber" required placeholder="Enter your phone number">
                </div>

                <div class="form-group">
                    <label for="university" data-i18n="form_uni_label">University & Major</label>
                    <input type="text" id="university" required placeholder="e.g. Cairo University, Computer Science">
                </div>

                <div class="form-group">
                    <label for="cvLink" data-i18n="form_cv_label">Resume Link (Google Drive/Dropbox)</label>
                    <input type="url" id="cvLink" required placeholder="https://drive.google.com/...">
                </div>
                
                <button type="submit" class="btn btn-primary w-100" style="margin-top: 15px; width: 100%;" data-i18n="form_submit_btn">Submit Application</button>
            </form>
            
            <!-- Success Message -->
            <div class="form-success" id="formSuccess">
                <svg class="success-icon" viewBox="0 0 24 24" width="48" height="48" fill="none" stroke="var(--accent-blue)" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="margin: 0 auto 16px;"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
                <h4 data-i18n="form_success_title">Application Submitted!</h4>
                <p data-i18n="form_success_desc">Thank you for applying. Our team will review your CV and contact you soon.</p>
                <button class="btn btn-secondary" id="successCloseBtn" style="margin-top: 15px; padding: 8px 24px;" data-i18n="form_close_btn">Close</button>
            </div>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const modal = document.getElementById('registrationModal');
            const form = document.getElementById('bootcampForm');
            const successScreen = document.getElementById('formSuccess');
            const closeBtn = document.getElementById('modalCloseBtn');
            const successCloseBtn = document.getElementById('successCloseBtn');
            const modalTitle = document.getElementById('modalTitle');
            const selectedRoleInput = document.getElementById('selectedRole');
            
            // Open modal on Apply button click
            document.querySelectorAll('[id^="applyBoot"]').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    e.preventDefault();
                    
                    const card = btn.closest('.card');
                    const titleText = card.querySelector('.card-title').textContent;
                    const bootcampId = btn.getAttribute('href').split('bootcamp=')[1] || '';
                    
                    selectedRoleInput.value = bootcampId;
                    modalTitle.textContent = titleText;
                    
                    form.reset();
                    form.style.display = 'block';
                    successScreen.classList.remove('show');
                    
                    modal.classList.add('show');
                    document.body.style.overflow = 'hidden';
                });
            });
            
            const closeModal = () => {
                modal.classList.remove('show');
                document.body.style.overflow = '';
            };
            
            closeBtn.addEventListener('click', closeModal);
            successCloseBtn.addEventListener('click', closeModal);
            
            modal.addEventListener('click', (e) => {
                if (e.target === modal) {
                    closeModal();
                }
            });
            
            form.addEventListener('submit', (e) => {
                e.preventDefault();
                
                const applicationData = {
                    bootcamp: selectedRoleInput.value,
                    name: document.getElementById('fullName').value,
                    email: document.getElementById('emailAddress').value,
                    phone: document.getElementById('phoneNumber').value,
                    uni: document.getElementById('university').value,
                    cv: document.getElementById('cvLink').value,
                    timestamp: new Date().toISOString()
                };
                
                console.log("Submitting Bootcamp Application:", applicationData);
                
                form.style.display = 'none';
                successScreen.classList.add('show');
            });
        });
    </script>
"""

# Append modal and scripts block right before </body> tag in bootcamps.html
html_boot = html_boot.replace('    <button class="back-to-top" id="backToTop" aria-label="Back to Top">↑</button>', boot_modal_markup + '\n    <button class="back-to-top" id="backToTop" aria-label="Back to Top">↑</button>')

with open("bootcamps.html", "w", encoding="utf-8") as f:
    f.write(html_boot)

print("bootcamps.html successfully updated with modal script!")
