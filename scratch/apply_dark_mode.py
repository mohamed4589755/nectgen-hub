# 1. Update styles.css
with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

dark_mode_css = """
/* Dark Theme Variables */
body.dark-theme, html.dark-theme {
    --bg-primary: #0A0A0C;
    --bg-secondary: #121215;
    --bg-tertiary: #16161A;
    --accent-blue: #3b82f6;
    --accent-violet: #F5F5F7;
    --accent-cyan: #60a5fa;
    --text-main: #ECECEF;
    --text-muted: #8E919A;
    --text-dark: #FFFFFF;
    --glass-bg: rgba(18, 18, 22, 0.85);
    --glass-border: rgba(255, 255, 255, 0.08);
    --gradient-primary: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
    --gradient-glow: 0 0 30px rgba(59, 130, 246, 0.2);
    --shadow-soft: 0 12px 40px rgba(0, 0, 0, 0.3);
    --shadow-hover: 0 24px 60px rgba(0, 0, 0, 0.5);
}

/* Adjustments for logo in dark theme */
body.dark-theme .logo-text-top {
    color: #FFFFFF !important;
}
body.dark-theme .logo-text-bottom {
    color: #9CA3AF !important;
}

/* Form input styling for dark theme */
body.dark-theme .form-group input,
body.dark-theme .form-group textarea,
body.dark-theme .form-group select {
    background: rgba(255, 255, 255, 0.03) !important;
    border-color: rgba(255, 255, 255, 0.1) !important;
    color: #FFFFFF !important;
}

body.dark-theme .form-group input:focus,
body.dark-theme .form-group textarea:focus,
body.dark-theme .form-group select:focus {
    border-color: var(--accent-blue) !important;
    box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.15) !important;
}

/* Custom dark theme adjustments to prevent white backgrounds */
body.dark-theme .card {
    background: var(--glass-bg);
    border-color: var(--glass-border);
}

body.dark-theme .btn-secondary {
    background: rgba(255, 255, 255, 0.06);
    border-color: rgba(255, 255, 255, 0.15);
    color: #FFFFFF;
}

body.dark-theme .btn-secondary:hover {
    background: var(--accent-blue);
    color: #FFFFFF;
    border-color: transparent;
}

/* Ensure the hero slider handles dark backgrounds beautifully */
body.dark-theme .hero-dot {
    background: rgba(255, 255, 255, 0.2);
}
body.dark-theme .hero-dot.active {
    background: var(--accent-blue);
}

/* Smooth transition for theme switching */
body {
    transition: background-color 0.4s ease, color 0.4s ease, border-color 0.4s ease, box-shadow 0.4s ease;
}
.card, .glass-panel, header, footer, a, span, p, h1, h2, h3, h4, h5, h6, input, textarea, select, button {
    transition: background-color 0.4s ease, color 0.4s ease, border-color 0.4s ease, box-shadow 0.4s ease, transform 0.3s ease, opacity 0.3s ease;
}
"""

if "body.dark-theme" not in css:
    css += dark_mode_css

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("styles.css updated with dark mode styles!")


# 2. Update lang.js translations
with open("lang.js", "r", encoding="utf-8") as f:
    lang_content = f.read()

# English keys replacement
old_en_key = 'contact_form_btn: "Send Inquiry"'
new_en_key = 'contact_form_btn: "Send Inquiry",\n        theme_dark: "Dark Mode",\n        theme_light: "Light Mode"'

# Arabic keys replacement
old_ar_key = 'contact_form_btn: "إرسال الاستفسار"'
new_ar_key = 'contact_form_btn: "إرسال الاستفسار",\n        theme_dark: "الوضع الداكن",\n        theme_light: "الوضع المضيء"'

lang_content = lang_content.replace(old_en_key, new_en_key).replace(old_ar_key, new_ar_key)

with open("lang.js", "w", encoding="utf-8") as f:
    f.write(lang_content)

print("lang.js updated with dark mode translations!")


# 3. Update main.js script
with open("main.js", "r", encoding="utf-8") as f:
    js = f.read()

# Add instant theme check at the very top of main.js
instant_theme_check = """// Instant theme application to prevent light-theme flash
if (localStorage.getItem('selectedTheme') === 'dark') {
    document.documentElement.classList.add('dark-theme');
    document.body.classList.add('dark-theme');
}
"""

if "Instant theme application" not in js:
    js = instant_theme_check + js

# Inject the dynamic theme button loader inside DOMContentLoaded listener
dom_loaded_inject = """    // --- Dark Mode Switcher ---
    const initTheme = () => {
        const navMenu = document.getElementById('navMenu');
        if (!navMenu || document.getElementById('themeToggle')) return;
        
        let currentTheme = localStorage.getItem('selectedTheme') || 'light';
        
        // Create button list item
        const li = document.createElement('li');
        li.style.display = 'flex';
        li.style.alignItems = 'center';
        li.style.marginLeft = '12px';
        
        const btn = document.createElement('button');
        btn.id = 'themeToggle';
        btn.className = 'btn';
        btn.style.padding = '6px 12px';
        btn.style.fontSize = '0.78rem';
        btn.style.background = 'var(--bg-secondary)';
        btn.style.border = '1px solid var(--glass-border)';
        btn.style.borderRadius = 'var(--radius-pill)';
        btn.style.cursor = 'pointer';
        btn.style.color = 'var(--text-main)';
        btn.style.fontWeight = '600';
        btn.style.display = 'flex';
        btn.style.alignItems = 'center';
        btn.style.gap = '6px';
        btn.style.transition = 'var(--transition-smooth)';
        
        // Sun SVG
        const sunSvg = `<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0;"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>`;
        
        // Moon SVG
        const moonSvg = `<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0;"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>`;
        
        const updateButtonUI = (theme) => {
            const translationsDict = typeof translations !== 'undefined' ? translations : {};
            const currentLang = localStorage.getItem('selectedLang') || 'en';
            
            if (theme === 'dark') {
                const label = (translationsDict[currentLang] && translationsDict[currentLang]['theme_light']) || 'Light Mode';
                btn.innerHTML = `${sunSvg} <span data-i18n="theme_light">${label}</span>`;
            } else {
                const label = (translationsDict[currentLang] && translationsDict[currentLang]['theme_dark']) || 'Dark Mode';
                btn.innerHTML = `${moonSvg} <span data-i18n="theme_dark">${label}</span>`;
            }
        };
        
        updateButtonUI(currentTheme);
        
        btn.addEventListener('click', () => {
            const isDark = document.body.classList.toggle('dark-theme');
            document.documentElement.classList.toggle('dark-theme', isDark);
            const newTheme = isDark ? 'dark' : 'light';
            localStorage.setItem('selectedTheme', newTheme);
            updateButtonUI(newTheme);
        });
        
        li.appendChild(btn);
        
        // Append next to language button or at end
        navMenu.appendChild(li);
    };
    
    initTheme();
    setTimeout(initTheme, 100);
"""

# Append this logic right inside the DOMContentLoaded listener block (near the end of main.js)
dom_content_loaded_end = "    document.body.appendChild(waBtn);\n});"
js = js.replace(dom_content_loaded_end, dom_content_loaded_end.replace("});", dom_loaded_inject + "\n});"))

with open("main.js", "w", encoding="utf-8") as f:
    f.write(js)

print("main.js updated with theme toggle logic!")
