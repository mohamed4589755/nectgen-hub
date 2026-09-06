with open("internships.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("\r\n", "\n")

# Replace form HTML structure (lines 247 to 273)
old_form_html = """            <form class="modal-form" id="internshipForm">
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
            </form>"""

new_form_html = """            <form class="modal-form" id="internshipForm" method="POST">
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
            <iframe name="hidden_iframe" id="hidden_iframe" style="display:none;"></iframe>"""

html = html.replace(old_form_html, new_form_html)

# Replace Javascript submit logic
old_js_logic = """            // Form submission logic
            form.addEventListener('submit', (e) => {
                e.preventDefault();
                
                const trackName = selectedRoleInput.value;
                const nameVal = document.getElementById('fullName').value;
                const emailVal = document.getElementById('emailAddress').value;
                const phoneVal = document.getElementById('phoneNumber').value;
                const uniValue = document.getElementById('university').value;
                
                // Split the university field by comma to separate University and College
                const parts = uniValue.split(',');
                const universityPart = parts[0] ? parts[0].trim() : uniValue;
                const collegePart = parts[1] ? parts[1].trim() : "";
                
                console.log("Submitting Internship Application:", {
                    track: trackName,
                    name: nameVal,
                    email: emailVal,
                    phone: phoneVal,
                    university: universityPart,
                    college: collegePart
                });
                
                // Visual feedback: disable button and show loading state
                const submitBtn = form.querySelector('button[type="submit"]');
                const originalBtnText = submitBtn.textContent;
                submitBtn.disabled = true;
                submitBtn.textContent = "Submitting...";
                
                // We only submit to the Google Form if it is the Data Analytics track
                if (trackName && trackName.toLowerCase().includes("data_analytics")) {
                    const formActionUrl = "https://docs.google.com/forms/d/e/1FAIpQLSdCA-mxNAnhtxBgmf0PnZGKLWqX1e495YEDBvAWUsLetZRY_A/formResponse";
                    
                    // Create URLSearchParams to match Google Form format
                    const formData = new URLSearchParams();
                    formData.append('entry.1171089655', nameVal);
                    formData.append('entry.46744813', emailVal);
                    formData.append('entry.1536865297', phoneVal);
                    formData.append('entry.2072862761', universityPart);
                    formData.append('entry.389164000', collegePart);
                    
                    fetch(formActionUrl, {
                        method: 'POST',
                        mode: 'no-cors', // Standard way to bypass CORS for Google Form submissions
                        headers: {
                            'Content-Type': 'application/x-www-form-urlencoded'
                        },
                        body: formData
                    })
                    .then(() => {
                        // Show success screen
                        form.style.display = 'none';
                        successScreen.classList.add('show');
                    })
                    .catch((error) => {
                        console.error("Google Form submission error:", error);
                        // Safe fallback: show success screen to student even if fetch fails
                        form.style.display = 'none';
                        successScreen.classList.add('show');
                    })
                    .finally(() => {
                        submitBtn.disabled = false;
                        submitBtn.textContent = originalBtnText;
                    });
                } else {
                    // For other tracks, simulate success locally for now
                    setTimeout(() => {
                        form.style.display = 'none';
                        successScreen.classList.add('show');
                        submitBtn.disabled = false;
                        submitBtn.textContent = originalBtnText;
                    }, 600);
                }
            });"""

new_js_logic = """            // Form submission logic
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
            });"""

html = html.replace(old_js_logic, new_js_logic)

with open("internships.html", "w", encoding="utf-8") as f:
    f.write(html)

print("internships.html updated with direct HTML Google Form submission successfully!")
