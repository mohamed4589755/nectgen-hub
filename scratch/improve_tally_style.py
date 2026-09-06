with open("internships.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("\r\n", "\n")

# Replace Tally modal container with a highly optimized styling (padding: 0, overflow: hidden, floating close button)
old_tally_modal = """    <!-- Registration Modal with Embedded Tally Form -->
    <div class="modal-overlay" id="registrationModal">
        <div class="modal-content glass-panel" style="max-width: 650px; padding: 20px; width: 95%; height: auto; max-height: 90vh; display: flex; flex-direction: column; overflow: hidden;">
            <button class="modal-close" id="modalCloseBtn" aria-label="Close Modal" style="top: 10px; right: 10px; z-index: 9999;">&times;</button>
            <iframe id="tallyIframe" src="about:blank" width="100%" height="600" frameborder="0" marginheight="0" marginwidth="0" title="Registration Form" style="border: none; border-radius: 12px; background: transparent; flex-grow: 1; min-height: 550px;"></iframe>
        </div>
    </div>"""

new_tally_modal = """    <!-- Registration Modal with Embedded Tally Form -->
    <div class="modal-overlay" id="registrationModal">
        <div class="modal-content glass-panel" style="max-width: 600px; padding: 0 !important; width: 95%; height: 650px; overflow: hidden; border-radius: 20px; border: 1px solid var(--glass-border); box-shadow: var(--shadow-lg);">
            <!-- Elegant circular glass close button -->
            <button class="modal-close" id="modalCloseBtn" aria-label="Close Modal" style="position: absolute; top: 16px; right: 16px; z-index: 9999; background: rgba(15, 23, 42, 0.06); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.3rem; border: 1px solid rgba(15, 23, 42, 0.08); color: var(--text-main); cursor: pointer; transition: all 0.2s ease;">&times;</button>
            
            <iframe id="tallyIframe" src="about:blank" width="100%" height="100%" frameborder="0" marginheight="0" marginwidth="0" title="Registration Form" style="border: none; border-radius: 20px; background: var(--bg-secondary); width: 100%; height: 100%; display: block;"></iframe>
        </div>
    </div>"""

html = html.replace(old_tally_modal, new_tally_modal)

# Let's add hover style override for the close button inside internships.html (or in javascript dynamically)
# We can inject a style tag inside internships.html head to handle hover styles for this circular button cleanly
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

html = html.replace("</head>", style_block)

with open("internships.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Tally iframe modal container styled and polished successfully!")
