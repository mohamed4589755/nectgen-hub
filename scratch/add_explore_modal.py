# 1. Update lang.js with translation keys for the Explore modal
with open("lang.js", "r", encoding="utf-8") as f:
    js = f.read()

js = js.replace("\r\n", "\n")

# English translation keys insertion (after nav_contact key or index_hero_cta_primary)
en_target = 'index_hero_cta_primary: "Explore Programs",'
en_replacement = """index_hero_cta_primary: "Explore Programs",
        explore_modal_title: "Explore Our Programs",
        explore_modal_sub: "Choose the path that matches your learning style and career goals.",
        explore_card_intern_title: "Internships",
        explore_card_intern_desc: "1-month corporate training with direct engineering mentorship.",
        explore_card_boot_title: "Summer Bootcamps",
        explore_card_boot_desc: "Intensive 2-month practical coding bootcamps for fast skill acquisition.",
        explore_card_diploma_title: "Professional Diplomas",
        explore_card_diploma_desc: "Comprehensive 5-month career tracks with guaranteed co-op internships.",
        explore_back_btn: "Back to Home","""

# Arabic translation keys insertion
ar_target = 'index_hero_cta_primary: "استكشف البرامج",'
ar_replacement = """index_hero_cta_primary: "استكشف البرامج",
        explore_modal_title: "استكشف برامجنا التعليمية",
        explore_modal_sub: "اختر المسار الذي يناسب أهدافك المهنية وطريقتك في التعلم.",
        explore_card_intern_title: "التدريب العملي (Internships)",
        explore_card_intern_desc: "تدريب عملي لمدة شهر بالتعاون مع شركات تكنولوجيا وتحت إشراف مهندسين خبراء.",
        explore_card_boot_title: "المعسكرات الصيفية (Bootcamps)",
        explore_card_boot_desc: "معسكرات برمجية وعملية مكثفة مدتها شهرين لاكتساب المهارات المطلوبة في سوق العمل بسرعة.",
        explore_card_diploma_title: "الدبلومات المهنية (Diplomas)",
        explore_card_diploma_desc: "مسارات تأهيل وظيفي متكاملة مدتها ٥ أشهر مع تدريب عملي مضمون ومكفول بعد التخرج.",
        explore_back_btn: "العودة للرئيسية","""

js = js.replace(en_target, en_replacement)
js = js.replace(ar_target, ar_replacement)

with open("lang.js", "w", encoding="utf-8") as f:
    f.write(js)

print("lang.js updated with explore modal translation keys!")


# 2. Update styles.css with explore modal card and layout rules
with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

css = css.replace("\r\n", "\n")

explore_css = """
/* --- EXPLORE MODAL SPECIAL CARDS --- */
.explore-modal-content {
    max-width: 600px !important;
    padding: 40px 32px !important;
}

.explore-modal-header {
    text-align: center;
    margin-bottom: 28px;
}

.explore-modal-title {
    font-size: 1.7rem;
    font-weight: 700;
    margin-bottom: 8px;
    letter-spacing: -0.01em;
}

.explore-modal-sub {
    font-size: 0.95rem;
    color: var(--text-muted);
}

.explore-grid {
    display: flex;
    flex-direction: column;
    gap: 16px;
}

.explore-option-card {
    display: flex;
    align-items: center;
    padding: 16px 20px;
    background: var(--bg-secondary);
    border: 1px solid var(--glass-border);
    border-radius: var(--radius-md);
    text-decoration: none !important;
    transition: all 0.3s cubic-bezier(0.25, 1, 0.5, 1);
    color: var(--text-main) !important;
}

.explore-option-card:hover {
    background: var(--bg-tertiary);
    border-color: var(--accent-blue);
    transform: translateY(-2px);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.03);
}

body.dark-theme .explore-option-card:hover {
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.25);
    border-color: var(--accent-cyan);
}

.explore-option-icon {
    width: 44px;
    height: 44px;
    border-radius: var(--radius-sm);
    background: rgba(14, 165, 233, 0.08);
    color: var(--accent-blue);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    margin-right: 16px;
    transition: var(--transition-smooth);
}

body.rtl .explore-option-icon {
    margin-right: 0;
    margin-left: 16px;
}

.explore-option-icon svg {
    width: 22px;
    height: 22px;
}

.explore-option-card:hover .explore-option-icon {
    background: var(--accent-blue);
    color: #FFFFFF;
}

body.dark-theme .explore-option-icon {
    background: rgba(96, 165, 250, 0.1);
    color: var(--accent-cyan);
}

body.dark-theme .explore-option-card:hover .explore-option-icon {
    background: var(--accent-cyan);
    color: #0A0A0C !important;
}

.explore-option-info {
    flex-grow: 1;
}

.explore-option-title {
    font-size: 1.1rem;
    font-weight: 600;
    margin-bottom: 2px;
}

.explore-option-desc {
    font-size: 0.85rem;
    color: var(--text-muted);
    line-height: 1.35;
}

.explore-option-arrow {
    color: var(--text-muted);
    opacity: 0;
    transform: translateX(-10px);
    transition: all 0.3s ease;
}

body.rtl .explore-option-arrow {
    transform: translateX(10px);
}

.explore-option-card:hover .explore-option-arrow {
    opacity: 1;
    color: var(--accent-blue);
    transform: translateX(0);
}

body.dark-theme .explore-option-card:hover .explore-option-arrow {
    color: var(--accent-cyan);
}
"""

if explore_css not in css:
    css += explore_css
    with open("styles.css", "w", encoding="utf-8") as f:
        f.write(css)
    print("styles.css updated with explore modal styles!")


# 3. Update index.html to add the explore modal markup
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("\r\n", "\n")

modal_html = """    <!-- Explore Programs Modal -->
    <div class="modal-overlay" id="exploreModal">
        <div class="modal-content explore-modal-content">
            <button class="modal-close" id="closeExploreModal">&times;</button>
            <div class="explore-modal-header">
                <h2 class="explore-modal-title" data-i18n="explore_modal_title">Explore Our Programs</h2>
                <p class="explore-modal-sub" data-i18n="explore_modal_sub">Choose the path that matches your learning style and career goals.</p>
            </div>
            <div class="explore-grid">
                <!-- Option 1: Internships -->
                <a href="internships.html" class="explore-option-card">
                    <div class="explore-option-icon">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <rect x="2" y="7" width="20" height="14" rx="2" ry="2"/>
                            <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>
                        </svg>
                    </div>
                    <div class="explore-option-info">
                        <h3 class="explore-option-title" data-i18n="explore_card_intern_title">Internships</h3>
                        <p class="explore-option-desc" data-i18n="explore_card_intern_desc">1-month corporate training with direct engineering mentorship.</p>
                    </div>
                    <div class="explore-option-arrow">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                            <line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/>
                        </svg>
                    </div>
                </a>
                
                <!-- Option 2: Bootcamps -->
                <a href="bootcamps.html" class="explore-option-card">
                    <div class="explore-option-icon">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M18 3a3 3 0 0 0-3 3v12a3 3 0 0 0 3 3 3 3 0 0 0 3-3V6a3 3 0 0 0-3-3z"/>
                            <path d="M6 3a3 3 0 0 0-3 3v12a3 3 0 0 0 3 3 3 3 0 0 0 3-3V6a3 3 0 0 0-3-3z"/>
                            <path d="M12 9v12"/>
                            <path d="M9 12h6"/>
                        </svg>
                    </div>
                    <div class="explore-option-info">
                        <h3 class="explore-option-title" data-i18n="explore_card_boot_title">Summer Bootcamps</h3>
                        <p class="explore-option-desc" data-i18n="explore_card_boot_desc">Intensive 2-month practical coding bootcamps for fast skill acquisition.</p>
                    </div>
                    <div class="explore-option-arrow">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                            <line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/>
                        </svg>
                    </div>
                </a>
                
                <!-- Option 3: Diplomas -->
                <a href="diplomas.html" class="explore-option-card">
                    <div class="explore-option-icon">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M22 10v6M2 10l10-5 10 5-10 5z"/>
                            <path d="M6 12v5c0 2 2 3 6 3s6-1 6-3v-5"/>
                        </svg>
                    </div>
                    <div class="explore-option-info">
                        <h3 class="explore-option-title" data-i18n="explore_card_diploma_title">Professional Diplomas</h3>
                        <p class="explore-option-desc" data-i18n="explore_card_diploma_desc">Comprehensive 5-month career tracks with guaranteed co-op internships.</p>
                    </div>
                    <div class="explore-option-arrow">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                            <line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/>
                        </svg>
                    </div>
                </a>
            </div>
        </div>
    </div>

</body>"""

html = html.replace("</body>", modal_html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html updated with explore modal markup!")


# 4. Update main.js to add the controller script
with open("main.js", "r", encoding="utf-8") as f:
    js_code = f.read()

js_code = js_code.replace("\r\n", "\n")

controller_js = """
    // --- Explore Programs Modal Controller ---
    const exploreCta = document.getElementById('heroCtaPrimary');
    const exploreModal = document.getElementById('exploreModal');
    const closeExploreModal = document.getElementById('closeExploreModal');
    
    if (exploreCta && exploreModal) {
        exploreCta.addEventListener('click', (e) => {
            e.preventDefault(); // Stop normal redirection
            exploreModal.classList.add('active');
            document.body.style.overflow = 'hidden'; // Disable background scrolling
        });
        
        const closeModal = () => {
            exploreModal.classList.remove('active');
            document.body.style.overflow = ''; // Re-enable background scrolling
        };
        
        if (closeExploreModal) {
            closeExploreModal.addEventListener('click', closeModal);
        }
        
        // Close on clicking outside the modal content
        exploreModal.addEventListener('click', (e) => {
            if (e.target === exploreModal) {
                closeModal();
            }
        });
        
        // Close on clicking any card link to avoid locked scrolling on navigation
        const exploreCards = exploreModal.querySelectorAll('.explore-option-card');
        exploreCards.forEach(card => {
            card.addEventListener('click', () => {
                closeModal();
            });
        });
    }
"""

# Append the controller to DOMContentLoaded block in main.js
# We can find the DOMContentLoaded closing bracket
dom_content_loaded_end = """    // --- Dark Mode Switcher ---"""
js_code = js_code.replace(dom_content_loaded_end, controller_js + "\n" + dom_content_loaded_end)

with open("main.js", "w", encoding="utf-8") as f:
    f.write(js_code)

print("main.js updated with explore modal controller!")
