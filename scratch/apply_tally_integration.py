with open("internships.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("\r\n", "\n")

# Replace Registration Modal and script block in internships.html
old_modal_and_script = """    <!-- Registration Modal -->
    <div class="modal-overlay" id="registrationModal">
        <div class="modal-content glass-panel">
            <button class="modal-close" id="modalCloseBtn" aria-label="Close Modal">&times;</button>
            <h3 class="modal-title" id="modalTitle">Register for Internship</h3>
            <p class="modal-subtitle" id="modalSubtitle" data-i18n="form_modal_sub">Please fill out the form below to apply.</p>
            
            <form class="modal-form" id="internshipForm" method="POST">
                <input type="hidden" id="selectedRole" name="role">
                <input type="hidden" name="entry.2072862761" id="universityHidden">
                <input type="hidden" name="entry.389164000" id="collegeHidden">
                
                <div class="form-group">
                    <label for="fullName" data-i18n="form_name_label">Full Name</label>
                    <input type="text" name="entry.1171089655" id="fullName" required placeholder="Enter your full name">
                </div>
                
                <div class="form-group">
                    <label for="emailAddress" data-i18n="form_email_label">Email Address</label>
                    <input type="email" name="entry.46744813" id="emailAddress" required placeholder="Enter your email">
                </div>
                
                <div class="form-group">
                    <label for="phoneNumber" data-i18n="form_phone_label">Phone Number</label>
                    <input type="tel" name="entry.1536865297" id="phoneNumber" required placeholder="Enter your phone number">
                </div>

                <div class="form-group">
                    <label for="universityInput" data-i18n="form_uni_label">University & College</label>
                    <input type="text" id="universityInput" required placeholder="e.g. Cairo University, Faculty of Engineering">
                </div>

                <button type="submit" class="btn btn-primary w-100" style="margin-top: 15px; width: 100%;" data-i18n="form_submit_btn">Submit Application</button>
            </form>
            
            <!-- Hidden iframe to handle Google Form submit natively without redirecting -->
            <iframe name="hidden_iframe" id="hidden_iframe" style="display:none;"></iframe>
            
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
                const trackName = selectedRoleInput.value;
                const uniVal = document.getElementById('universityInput').value;
                
                // Hide form and show success screen instantly
                form.style.display = 'none';
                successScreen.classList.add('show');
                
                // If it is the Data Analytics track, configure native POST submit to Google Forms
                if (trackName && trackName.toLowerCase().includes("data_analytics")) {
                    // Split the university field by comma to separate University and College
                    const parts = uniVal.split(',');
                    document.getElementById('universityHidden').value = parts[0] ? parts[0].trim() : uniVal;
                    document.getElementById('collegeHidden').value = parts[1] ? parts[1].trim() : "";
                    
                    form.action = "https://docs.google.com/forms/d/e/1FAIpQLSdCA-mxNAnhtxBgmf0PnZGKLWqX1e495YEDBvAWUsLetZRY_A/formResponse";
                    form.target = "hidden_iframe";
                    
                    console.log("Submitting native Google Form for Data Analytics...");
                } else {
                    // For other tracks, bypass Google Forms and handle purely locally
                    e.preventDefault();
                    form.action = "";
                    form.target = "";
                    console.log("Simulating local success for other track:", trackName);
                }
            });
        });
    </script>"""

new_modal_and_script = """    <!-- Registration Modal with Embedded Tally Form -->
    <div class="modal-overlay" id="registrationModal">
        <div class="modal-content glass-panel" style="max-width: 650px; padding: 20px; width: 95%; height: auto; max-height: 90vh; display: flex; flex-direction: column; overflow: hidden;">
            <button class="modal-close" id="modalCloseBtn" aria-label="Close Modal" style="top: 10px; right: 10px; z-index: 9999;">&times;</button>
            <iframe id="tallyIframe" src="about:blank" width="100%" height="600" frameborder="0" marginheight="0" marginwidth="0" title="Registration Form" style="border: none; border-radius: 12px; background: transparent; flex-grow: 1; min-height: 550px;"></iframe>
        </div>
    </div>

    <script>
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

html = html.replace(old_modal_and_script, new_modal_and_script)

with open("internships.html", "w", encoding="utf-8") as f:
    f.write(html)

print("internships.html updated with Tally.so iframe integration successfully!")
