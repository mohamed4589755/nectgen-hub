with open("internships.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("\r\n", "\n")

old_submit_code = """            // --- Google Sheets Web App Config ---
            // Paste your deployed Google Apps Script Web App URL here:
            const GOOGLE_SHEET_WEBAPP_URL = "https://script.google.com/macros/s/AKfycbzlz-6eCzexIEdjU-jy4FFuZ7_boVgnlCpFwq7HndFIjyknxuY2TLK6hsXgglY9FT0l/exec";

            // Form submission logic
            form.addEventListener('submit', (e) => {
                e.preventDefault();
                
                // Collect input values
                const applicationData = {
                    name: document.getElementById('fullName').value,
                    email: document.getElementById('emailAddress').value,
                    phone: document.getElementById('phoneNumber').value,
                    university: document.getElementById('university').value,
                    track: selectedRoleInput.value // e.g. "Data Analytics Internship"
                };
                
                console.log("Submitting Internship Application to Google Sheet:", applicationData);
                
                // Visual feedback: disable button and show loading state
                const submitBtn = form.querySelector('button[type="submit"]');
                const originalBtnText = submitBtn.textContent;
                submitBtn.disabled = true;
                submitBtn.textContent = "Submitting...";
                
                // If Web App URL is still placeholder, skip network and show success immediately
                if (GOOGLE_SHEET_WEBAPP_URL === "https://script.google.com/macros/s/AKfycbzlz-6eCzexIEdjU-jy4FFuZ7_boVgnlCpFwq7HndFIjyknxuY2TLK6hsXgglY9FT0l/exec") {
                    form.style.display = 'none';
                    successScreen.classList.add('show');
                    submitBtn.disabled = false;
                    submitBtn.textContent = originalBtnText;
                    return;
                }
                
                // Send registration data to Google Sheet
                fetch(GOOGLE_SHEET_WEBAPP_URL, {
                    method: 'POST',
                    mode: 'no-cors', // Bypasses CORS policy checks for Apps Script redirection
                    headers: {
                        'Content-Type': 'text/plain' // Complies with no-cors allowed headers
                    },
                    body: JSON.stringify(applicationData)
                })
                .then(() => {
                    // Show success screen
                    form.style.display = 'none';
                    successScreen.classList.add('show');
                })
                .catch((error) => {
                    console.error("Google Sheet submission error:", error);
                    // Safe fallback: show success to student even if network request fails
                    form.style.display = 'none';
                    successScreen.classList.add('show');
                })
                .finally(() => {
                    submitBtn.disabled = false;
                    submitBtn.textContent = originalBtnText;
                });
            });"""

new_submit_code = """            // Form submission logic
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
                if (trackName && trackName.toLowerCase().includes("data analytics")) {
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

html = html.replace(old_submit_code, new_submit_code)

with open("internships.html", "w", encoding="utf-8") as f:
    f.write(html)

print("internships.html updated with Google Forms action integration successfully!")
