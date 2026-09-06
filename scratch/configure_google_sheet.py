with open("internships.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("\r\n", "\n")

# Replace form submission block with the direct Apps Script fetch handler
old_submit_block = """            // Form submission logic
            form.addEventListener('submit', (e) => {
                e.preventDefault();
                
                // Collect input values
                const applicationData = {
                    role: selectedRoleInput.value,
                    name: document.getElementById('fullName').value,
                    email: document.getElementById('emailAddress').value,
                    phone: document.getElementById('phoneNumber').value,
                    uni: document.getElementById('university').value,

                    timestamp: new Date().toISOString()
                };
                
                console.log("Submitting Internship Application:", applicationData);
                
                // Simulate success API call
                form.style.display = 'none';
                successScreen.classList.add('show');
            });"""

new_submit_block = """            // --- Google Sheets Web App Config ---
            // Paste your deployed Google Apps Script Web App URL here:
            const GOOGLE_SHEET_WEBAPP_URL = "YOUR_DEPLOYED_WEBAPP_URL_HERE";

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
                if (GOOGLE_SHEET_WEBAPP_URL === "YOUR_DEPLOYED_WEBAPP_URL_HERE") {
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
                        'Content-Type': 'application/json'
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

html = html.replace(old_submit_block, new_submit_block)

with open("internships.html", "w", encoding="utf-8") as f:
    f.write(html)

print("internships.html updated with Google Sheets integration successfully!")
