# 1. Update lang.js translations
with open("lang.js", "r", encoding="utf-8") as f:
    js = f.read()

en_form_keys = """        intern_role4_desc: "Design and implement responsive, high-performance web user interfaces. Write clean, semantic markup, advanced CSS styling, and interactive JavaScript modules.",
        form_name_label: "Full Name",
        form_email_label: "Email Address",
        form_phone_label: "Phone Number",
        form_uni_label: "University & Major",
        form_cv_label: "Resume Link (Google Drive/Dropbox)",
        form_submit_btn: "Submit Application",
        form_success_title: "Application Submitted!",
        form_success_desc: "Thank you for applying. Our team will review your CV and contact you soon.",
        form_close_btn: "Close",
        form_modal_sub: "Please fill out the form below to apply.","""

ar_form_keys = """        intern_role4_desc: "صمم ونفذ واجهات ويب سريعة وعصرية ومتجاوبة بالكامل. اكتب أكواد نظيفة للهيكل والتنسيق وتفاعل مع Vanilla JS/React.",
        form_name_label: "الاسم الكامل",
        form_email_label: "البريد الإلكتروني",
        form_phone_label: "رقم الهاتف",
        form_uni_label: "الجامعة والتخصص",
        form_cv_label: "رابط السيرة الذاتية (Google Drive / Dropbox)",
        form_submit_btn: "إرسال الطلب",
        form_success_title: "تم إرسال الطلب بنجاح!",
        form_success_desc: "شكرًا لتقديمك. سيقوم فريقنا بمراجعة سيرتك الذاتية والتواصل معك قريبًا.",
        form_close_btn: "إغلاق",
        form_modal_sub: "يرجى ملء النموذج أدناه لتقديم طلبك.", Hellenic: "المزيد","""

# Safely replace inside lang.js
js = js.replace('        intern_role4_desc: "Design and implement responsive, high-performance web user interfaces. Write clean, semantic markup, advanced CSS styling, and interactive JavaScript modules.",', en_form_keys)
js = js.replace('        intern_role4_desc: "صمم ونفذ واجهات ويب سريعة وعصرية ومتجاوبة بالكامل. اكتب أكواد نظيفة للهيكل والتنسيق وتفاعل مع Vanilla JS/React.",', ar_form_keys)

with open("lang.js", "w", encoding="utf-8") as f:
    f.write(js)

print("lang.js successfully updated with form translation keys!")


# 2. Update styles.css with modal styles
with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

modal_css = """
/* apple-style Interactive Registration Modal */
.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(10, 10, 12, 0.4);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 2000;
    opacity: 0;
    visibility: hidden;
    transition: opacity 0.4s ease, visibility 0.4s ease;
}

.modal-overlay.show {
    opacity: 1;
    visibility: visible;
}

.modal-content {
    width: 90%;
    max-width: 500px;
    padding: 40px;
    border-radius: var(--radius-md);
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);
    box-shadow: var(--shadow-hover);
    position: relative;
    transform: translateY(30px);
    transition: transform 0.4s cubic-bezier(0.25, 1, 0.5, 1);
    max-height: 90vh;
    overflow-y: auto;
}

.modal-overlay.show .modal-content {
    transform: translateY(0);
}

.modal-close {
    position: absolute;
    top: 20px;
    right: 20px;
    background: transparent;
    border: none;
    font-size: 1.8rem;
    line-height: 1;
    color: var(--text-muted);
    cursor: pointer;
    transition: var(--transition-smooth);
    padding: 0;
}

body.rtl .modal-close {
    right: auto;
    left: 20px;
}

.modal-close:hover {
    color: var(--text-main);
}

.modal-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--text-main);
    margin-bottom: 8px;
    text-align: center;
}

.modal-subtitle {
    font-size: 0.9rem;
    color: var(--text-muted);
    margin-bottom: 24px;
    text-align: center;
}

.form-group {
    margin-bottom: 16px;
    text-align: left;
}

body.rtl .form-group {
    text-align: right;
}

.form-group label {
    display: block;
    font-size: 0.8rem;
    font-weight: 600;
    color: var(--text-main);
    margin-bottom: 6px;
}

.form-group input {
    width: 100%;
    padding: 10px 14px;
    border-radius: var(--radius-sm);
    background: var(--bg-secondary);
    border: 1px solid var(--glass-border);
    color: var(--text-main);
    font-size: 0.9rem;
    transition: var(--transition-smooth);
}

.form-group input:focus {
    outline: none;
    border-color: var(--accent-blue);
    background: var(--bg-primary);
}

/* Form Success Overlay */
.form-success {
    display: none;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 20px 0;
}

.form-success.show {
    display: flex;
}

.form-success .success-icon {
    margin-bottom: 16px;
    animation: scaleUp 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
}

.form-success h4 {
    font-size: 1.3rem;
    font-weight: 700;
    color: var(--text-main);
    margin-bottom: 8px;
}

.form-success p {
    font-size: 0.9rem;
    color: var(--text-muted);
    max-width: 320px;
    margin-bottom: 15px;
}
"""

if ".modal-overlay" not in css:
    css += modal_css

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("styles.css successfully updated with modal styles!")


# 3. Update internships.html
with open("internships.html", "r", encoding="utf-8") as f:
    html = f.read()

# Define modal and script markup
modal_markup = """
    <!-- Registration Modal -->
    <div class="modal-overlay" id="registrationModal">
        <div class="modal-content glass-panel">
            <button class="modal-close" id="modalCloseBtn" aria-label="Close Modal">&times;</button>
            <h3 class="modal-title" id="modalTitle">Register for Internship</h3>
            <p class="modal-subtitle" id="modalSubtitle" data-i18n="form_modal_sub">Please fill out the form below to apply.</p>
            
            <form class="modal-form" id="internshipForm">
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
            const form = document.getElementById('internshipForm');
            const successScreen = document.getElementById('formSuccess');
            const closeBtn = document.getElementById('modalCloseBtn');
            const successCloseBtn = document.getElementById('successCloseBtn');
            const modalTitle = document.getElementById('modalTitle');
            const selectedRoleInput = document.getElementById('selectedRole');
            
            // Open modal on Apply button click
            document.querySelectorAll('[id^="applyRole"]').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    e.preventDefault();
                    
                    // Find card parent and title
                    const card = btn.closest('.card');
                    const titleText = card.querySelector('.card-title').textContent;
                    const roleId = btn.getAttribute('href').split('role=')[1] || '';
                    
                    selectedRoleInput.value = roleId;
                    modalTitle.textContent = titleText;
                    
                    // Reset Form and View
                    form.reset();
                    form.style.display = 'block';
                    successScreen.classList.remove('show');
                    
                    // Open overlay
                    modal.classList.add('show');
                    document.body.style.overflow = 'hidden'; // Lock scrolling
                });
            });
            
            const closeModal = () => {
                modal.classList.remove('show');
                document.body.style.overflow = ''; // Unlock scrolling
            };
            
            closeBtn.addEventListener('click', closeModal);
            successCloseBtn.addEventListener('click', closeModal);
            
            // Close on overlay click
            modal.addEventListener('click', (e) => {
                if (e.target === modal) {
                    closeModal();
                }
            });
            
            // Form submission logic
            form.addEventListener('submit', (e) => {
                e.preventDefault();
                
                // Collect input values
                const applicationData = {
                    role: selectedRoleInput.value,
                    name: document.getElementById('fullName').value,
                    email: document.getElementById('emailAddress').value,
                    phone: document.getElementById('phoneNumber').value,
                    uni: document.getElementById('university').value,
                    cv: document.getElementById('cvLink').value,
                    timestamp: new Date().toISOString()
                };
                
                console.log("Submitting Internship Application:", applicationData);
                
                // Simulate success API call
                form.style.display = 'none';
                successScreen.classList.add('show');
            });
        });
    </script>
"""

# Append modal and scripts block right before </body> tag
html = html.replace('    <button class="back-to-top" id="backToTop" aria-label="Back to Top">↑</button>', modal_markup + '\n    <button class="back-to-top" id="backToTop" aria-label="Back to Top">↑</button>')

with open("internships.html", "w", encoding="utf-8") as f:
    f.write(html)

print("internships.html successfully updated with inline script and modal markup!")
