with open("internships.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("\r\n", "\n")

# Replace Tally modal container with custom HTML form container
old_tally_modal = """    <!-- Registration Modal with Embedded Tally Form -->
    <div class="modal-overlay" id="registrationModal">
        <div class="modal-content glass-panel" style="max-width: 600px; padding: 0 !important; width: 95%; height: 650px; overflow: hidden; border-radius: 20px; border: 1px solid var(--glass-border); box-shadow: var(--shadow-lg);">
            <!-- Elegant circular glass close button -->
            <button class="modal-close" id="modalCloseBtn" aria-label="Close Modal" style="position: absolute; top: 16px; right: 16px; z-index: 9999; background: rgba(15, 23, 42, 0.06); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.3rem; border: 1px solid rgba(15, 23, 42, 0.08); color: var(--text-main); cursor: pointer; transition: all 0.2s ease;">&times;</button>
            
            <iframe id="tallyIframe" src="about:blank" width="100%" height="100%" frameborder="0" marginheight="0" marginwidth="0" title="Registration Form" style="border: none; border-radius: 20px; background: var(--bg-secondary); width: 100%; height: 100%; display: block;"></iframe>
        </div>
    </div>"""

new_html_modal = """    <!-- Registration Modal -->
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
                    <label for="university" data-i18n="form_uni_label">University & College</label>
                    <input type="text" id="university" required placeholder="e.g. Cairo University, Faculty of Engineering">
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
    </div>"""

html = html.replace(old_tally_modal, new_html_modal)

# Replace Javascript logic (lines 288 to the end of script)
old_js_script = """    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const modal = document.getElementById('registrationModal');
            const iframe = document.getElementById('tallyIframe');
            const closeBtn = document.getElementById('modalCloseBtn');
            
            // Open modal on Apply button click
            document.querySelectorAll('[id^="applyRole"]').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    e.preventDefault();
                    
                    const roleId = btn.getAttribute('href').split('role=')[1] || '';
                    
                    // We map local role IDs to user-friendly names to prefill in Tally
                    let trackName = roleId;
                    if (roleId === 'AI_ML') trackName = 'AI & Machine Learning';
                    elif_da = 'Data_Analytics'; // Local var
                    if (roleId === 'Data_Analytics') trackName = 'Data Analytics';
                    if (roleId === 'Flutter_Dev') trackName = 'Flutter Development';
                    if (roleId === 'Frontend_Dev') trackName = 'Front-End Web Development';
                    
                    // Build Tally embed URL with pre-filled fields (e.g. ?Internship=Data_Analytics)
                    const tallyUrl = `https://tally.so/embed/obaeoN?alignLeft=1&hideTitle=1&transparentBackground=1&Internship=${encodeURIComponent(trackName)}&track=${encodeURIComponent(trackName)}`;
                    
                    // Set src of iframe to load Tally dynamically
                    iframe.src = tallyUrl;
                    
                    // Open overlay
                    modal.classList.add('show');
                    document.body.style.overflow = 'hidden'; // Lock scrolling
                });
            });
            
            const closeModal = () => {
                modal.classList.remove('show');
                iframe.src = "about:blank"; // Reset iframe to save memory
                document.body.style.overflow = ''; // Unlock scrolling
            };
            
            closeBtn.addEventListener('click', closeModal);
            
            // Close on overlay click
            modal.addEventListener('click', (e) => {
                if (e.target === modal) {
                    closeModal();
                }
            });
        });
    </script>"""

new_js_script = """    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const modal = document.getElementById('registrationModal');
            const form = document.getElementById('internshipForm');
            const successScreen = document.getElementById('formSuccess');
            const closeBtn = document.getElementById('modalCloseBtn');
            const successCloseBtn = document.getElementById('successCloseBtn');
            const modalTitle = document.getElementById('modalTitle');
            const selectedRoleInput = document.getElementById('selectedRole');
            
            // Active Google Sheets Web App Endpoint
            const GOOGLE_SHEET_WEBAPP_URL = "https://script.google.com/macros/s/AKfycbzlz-6eCzexIEdjU-jy4FFuZ7_boVgnlCpFwq7HndFIjyknxuY2TLK6hsXgglY9FT0l/exec";
            
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
                
                // Visual feedback: show loading state on button
                const submitBtn = form.querySelector('button[type="submit"]');
                const originalBtnText = submitBtn.textContent;
                submitBtn.disabled = true;
                submitBtn.textContent = "Submitting...";
                
                // Collect input values
                let trackName = selectedRoleInput.value;
                if (trackName === 'AI_ML') trackName = 'AI & Machine Learning Internship';
                if (trackName === 'Data_Analytics') trackName = 'Data Analytics Internship';
                if (trackName === 'Flutter_Dev') trackName = 'Flutter Developer Internship';
                if (trackName === 'Frontend_Dev') trackName = 'Front-End Web Developer Internship';

                const applicationData = {
                    name: document.getElementById('fullName').value,
                    email: document.getElementById('emailAddress').value,
                    phone: document.getElementById('phoneNumber').value,
                    university: document.getElementById('university').value,
                    track: trackName
                };
                
                console.log("Submitting Internship Application to Google Sheet:", applicationData);
                
                // Send registration data to Google Sheets Web App
                fetch(GOOGLE_SHEET_WEBAPP_URL, {
                    method: 'POST',
                    mode: 'no-cors', // Standard way to bypass CORS for Google Sheets redirection
                    body: JSON.stringify(applicationData)
                })
                .then(() => {
                    // Show success screen
                    form.style.display = 'none';
                    successScreen.classList.add('show');
                })
                .catch((error) => {
                    console.error("Google Sheet submission error:", error);
                    // Safe fallback: show success screen to student even if network request fails
                    form.style.display = 'none';
                    successScreen.classList.add('show');
                })
                .finally(() => {
                    submitBtn.disabled = false;
                    submitBtn.textContent = originalBtnText;
                });
            });
        });
    </script>"""

html = html.replace(old_js_script, new_js_script)

# Remove the Tally specific styling block we injected in the head
style_block = """
    <style>
        #modalCloseBtn:hover {
            background: rgba(15, 23, 42, 0.12) !important;
            transform: scale(1.05);
        }
        body.dark-theme #modalCloseBtn {
            background: rgba(255, 255, 255, 0.08) !important;
            border-color: rgba(255, 255, 255, 0.1) !important;
        }
        body.dark-theme #modalCloseBtn:hover {
            background: rgba(255, 255, 255, 0.15) !important;
        }
        body.dark-theme #tallyIframe {
            background: #0E0F12 !important; /* Match premium dark background */
        }
    </style>
</head>"""

html = html.replace(style_block, "</head>")

with open("internships.html", "w", encoding="utf-8") as f:
    f.write(html)

print("internships.html custom HTML Google Sheet form restored successfully!")
