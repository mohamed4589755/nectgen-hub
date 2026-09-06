# 1. Update styles.css
with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

dropdown_css = """
/* Sprints-style Language Dropdown */
.lang-dropdown-container {
    position: relative;
    display: flex;
    align-items: center;
}

.lang-dropdown-btn {
    display: flex;
    align-items: center;
    gap: 6px;
    background: var(--bg-secondary);
    border: 1px solid var(--glass-border);
    border-radius: var(--radius-pill);
    padding: 6px 12px;
    font-size: 0.78rem;
    font-weight: 600;
    color: var(--text-main);
    cursor: pointer;
    transition: var(--transition-smooth);
    margin-left: 12px;
}

.lang-dropdown-btn:hover, .lang-dropdown-btn.active {
    background: var(--accent-blue);
    color: var(--text-dark);
    border-color: transparent;
}

.lang-dropdown-btn.active .chevron-icon {
    transform: rotate(180deg);
}

body.rtl .lang-dropdown-btn {
    margin-left: 0;
    margin-right: 12px;
}

.lang-dropdown-menu {
    position: absolute;
    top: calc(100% + 8px);
    right: 0;
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);
    border-radius: var(--radius-sm);
    padding: 6px 0;
    list-style: none;
    min-width: 120px;
    box-shadow: var(--shadow-hover);
    z-index: 1001;
    opacity: 0;
    visibility: hidden;
    transform: translateY(-10px);
    transition: opacity 0.3s ease, transform 0.3s ease, visibility 0.3s ease;
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
}

body.rtl .lang-dropdown-menu {
    right: auto;
    left: 0;
}

.lang-dropdown-menu.show {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
}

.lang-dropdown-item {
    padding: 8px 16px;
    font-size: 0.8rem;
    font-weight: 500;
    color: var(--text-main);
    cursor: pointer;
    transition: var(--transition-smooth);
    text-align: left;
}

body.rtl .lang-dropdown-item {
    text-align: right;
}

.lang-dropdown-item:hover {
    background: var(--bg-secondary);
    color: var(--accent-blue);
}

.lang-dropdown-item.active {
    color: var(--accent-blue);
    font-weight: 700;
    background: rgba(46, 125, 255, 0.05);
}

/* Adjustments for dark theme buttons and dropdown hover states */
body.dark-theme .lang-dropdown-item:hover {
    background: rgba(255, 255, 255, 0.05);
}
body.dark-theme .lang-dropdown-item.active {
    background: rgba(59, 130, 246, 0.15);
}
"""

if ".lang-dropdown-container" not in css:
    css += dropdown_css

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("styles.css updated with dropdown styles!")


# 2. Update lang.js
with open("lang.js", "r", encoding="utf-8") as f:
    js = f.read()

# Replace insertLangButton implementation
old_insert_fn = """    // Create/Insert Language switch button dynamically into navbar if not present
    const insertLangButton = () => {
        const navMenu = document.getElementById('navMenu');
        if (navMenu && !document.getElementById('langToggle')) {
            const li = document.createElement('li');
            li.style.display = 'flex';
            li.style.alignItems = 'center';
            
            const btn = document.createElement('button');
            btn.id = 'langToggle';
            btn.className = 'btn';
            btn.style.width = '32px';
            btn.style.height = '32px';
            btn.style.padding = '0';
            btn.style.background = 'var(--bg-secondary)';
            btn.style.border = '1px solid var(--glass-border)';
            btn.style.borderRadius = '50%';
            btn.style.cursor = 'pointer';
            btn.style.color = 'var(--text-main)';
            btn.style.display = 'flex';
            btn.style.alignItems = 'center';
            btn.style.justifyContent = 'center';
            btn.style.marginLeft = '12px';
            btn.style.transition = 'var(--transition-smooth)';
            
            // Inject Feather Globe SVG
            btn.innerHTML = `<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="display: block; flex-shrink: 0;"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>`;
            
            // Hover effect
            btn.onmouseover = () => {
                btn.style.background = 'var(--accent-blue)';
                btn.style.color = 'var(--text-dark)';
                btn.style.borderColor = 'transparent';
            };
            btn.onmouseout = () => {
                btn.style.background = 'var(--bg-secondary)';
                btn.style.color = 'var(--text-main)';
                btn.style.borderColor = 'var(--glass-border)';
            };
            
            li.appendChild(btn);
            navMenu.appendChild(li);
            
            btn.addEventListener('click', () => {
                currentLang = currentLang === 'en' ? 'ar' : 'en';
                localStorage.setItem('selectedLang', currentLang);
                applyLanguage(currentLang);
            });
        }
    };"""

new_insert_fn = """    // Create/Insert Language switch dropdown dynamically into navbar if not present
    const insertLangButton = () => {
        const navMenu = document.getElementById('navMenu');
        if (navMenu && !document.getElementById('langDropdownContainer')) {
            const li = document.createElement('li');
            li.id = 'langDropdownContainer';
            li.className = 'lang-dropdown-container';
            
            // Create main button
            const btn = document.createElement('button');
            btn.id = 'langToggleBtn';
            btn.className = 'lang-dropdown-btn';
            
            // Globe icon SVG
            const globeSvg = `<svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0;"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>`;
            
            // Chevron down SVG
            const chevronSvg = `<svg class="chevron-icon" viewBox="0 0 24 24" width="10" height="10" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0; margin-left: 2px; transition: transform 0.3s ease;"><polyline points="6 9 12 15 18 9"/></svg>`;
            
            btn.innerHTML = `${globeSvg} <span class="active-lang-text">EN</span> ${chevronSvg}`;
            
            // Create dropdown menu
            const menu = document.createElement('ul');
            menu.id = 'langDropdownMenu';
            menu.className = 'lang-dropdown-menu';
            
            // English option
            const optEn = document.createElement('li');
            optEn.className = 'lang-dropdown-item';
            optEn.textContent = 'English';
            optEn.setAttribute('data-lang', 'en');
            
            // Arabic option
            const optAr = document.createElement('li');
            optAr.className = 'lang-dropdown-item';
            optAr.textContent = 'العربية';
            optAr.setAttribute('data-lang', 'ar');
            
            menu.appendChild(optEn);
            menu.appendChild(optAr);
            
            li.appendChild(btn);
            li.appendChild(menu);
            
            // Append to navMenu
            navMenu.appendChild(li);
            
            // Click listener for button (toggle menu)
            btn.addEventListener('click', (e) => {
                e.stopPropagation();
                menu.classList.toggle('show');
                btn.classList.toggle('active');
            });
            
            // Click listeners for options
            optEn.addEventListener('click', () => {
                if (currentLang !== 'en') {
                    currentLang = 'en';
                    localStorage.setItem('selectedLang', currentLang);
                    applyLanguage(currentLang);
                }
                menu.classList.remove('show');
                btn.classList.remove('active');
            });
            
            optAr.addEventListener('click', () => {
                if (currentLang !== 'ar') {
                    currentLang = 'ar';
                    localStorage.setItem('selectedLang', currentLang);
                    applyLanguage(currentLang);
                }
                menu.classList.remove('show');
                btn.classList.remove('active');
            });
            
            // Close dropdown when clicking anywhere else
            document.addEventListener('click', () => {
                menu.classList.remove('show');
                btn.classList.remove('active');
            });
        }
    };"""

js = js.replace(old_insert_fn, new_insert_fn)

# Replace placeholders block in applyLanguage to include updating dropdown labels
old_placeholders = """        // Translate placeholders
        document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
            const key = el.getAttribute('data-i18n-placeholder');
            if (translations[lang] && translations[lang][key]) {
                el.setAttribute('placeholder', translations[lang][key]);
            }
        });"""

new_placeholders = """        // Translate placeholders
        document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
            const key = el.getAttribute('data-i18n-placeholder');
            if (translations[lang] && translations[lang][key]) {
                el.setAttribute('placeholder', translations[lang][key]);
            }
        });
        
        // Update active language label in dropdown button
        const activeLangText = document.querySelector('.active-lang-text');
        if (activeLangText) {
            activeLangText.textContent = lang === 'en' ? 'EN' : 'العربية';
        }
        
        // Highlight active dropdown item
        document.querySelectorAll('.lang-dropdown-item').forEach(item => {
            const itemLang = item.getAttribute('data-lang');
            if (itemLang === lang) {
                item.classList.add('active');
            } else {
                item.classList.remove('active');
            }
        });"""

js = js.replace(old_placeholders, new_placeholders)

with open("lang.js", "w", encoding="utf-8") as f:
    f.write(js)

print("lang.js successfully updated with dropdown components!")
