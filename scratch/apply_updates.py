import glob
import re

# 1. Update all HTML files (LinkedIn, Facebook, Instagram, GitHub real SVG icons in the footer)
social_html_old = """                <div class="social-links" style="margin-top: 16px;">
                    <a href="https://www.linkedin.com/company/nextgen-institute/" class="social-icon" aria-label="LinkedIn" target="_blank">in</a>
                    <a href="#" class="social-icon" aria-label="Facebook" target="_blank">fb</a>
                    <a href="#" class="social-icon" aria-label="Instagram" target="_blank">ig</a>
                    <a href="#" class="social-icon" aria-label="GitHub">git</a>
                </div>"""

social_html_new = """                <div class="social-links" style="margin-top: 16px;">
                    <a href="https://www.linkedin.com/company/nextgen-institute/" class="social-icon" aria-label="LinkedIn" target="_blank">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/>
                            <rect x="2" y="9" width="4" height="12"/>
                            <circle cx="4" cy="4" r="2"/>
                        </svg>
                    </a>
                    <a href="#" class="social-icon" aria-label="Facebook" target="_blank">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>
                        </svg>
                    </a>
                    <a href="#" class="social-icon" aria-label="Instagram" target="_blank">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <rect x="2" y="2" width="20" height="20" rx="5" ry="5"/>
                            <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/>
                            <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/>
                        </svg>
                    </a>
                    <a href="#" class="social-icon" aria-label="GitHub" target="_blank">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/>
                        </svg>
                    </a>
                </div>"""

# Loop and replace social links in all HTML files
for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Normalize newlines for strict matching
    html_normalized = html.replace("\r\n", "\n")
    old_normalized = social_html_old.replace("\r\n", "\n")
    new_normalized = social_html_new.replace("\r\n", "\n")
    
    if old_normalized in html_normalized:
        html_normalized = html_normalized.replace(old_normalized, new_normalized)
        print(f"Replaced footer social links in {filepath} successfully!")
    else:
        # Fallback regex replace for any variance
        import re
        pattern = r'<div class="social-links".*?</div>'
        html_normalized, count = re.subn(pattern, new_normalized, html_normalized, flags=re.DOTALL)
        if count > 0:
            print(f"Replaced footer social links (regex) in {filepath} successfully!")
        else:
            print(f"Warning: Could not find social links in {filepath}!")
            
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_normalized)


# 2. Update styles.css
with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Normalize styles.css newlines
css = css.replace("\r\n", "\n")

# A. Update navbar link styles (Task 1)
old_nav_link_css = """.nav-link {
    font-size: 0.85rem;
    font-weight: 400;
    color: #515154; /* Apple gray navigation link */
    letter-spacing: -0.01em;
}

.nav-link:hover, .nav-link.active {
    color: var(--text-main);
    text-decoration: none;
}

.nav-link::after {
    display: none; /* Remove bottom underline animation for clean Apple look */
}"""

new_nav_link_css = """.nav-link {
    position: relative;
    font-size: 0.88rem;
    font-weight: 500;
    color: #374151; /* High contrast gray */
    letter-spacing: -0.01em;
    padding: 6px 0;
    transition: color 0.3s ease;
}

.nav-link:hover {
    color: var(--accent-blue);
    text-decoration: none;
}

.nav-link.active {
    color: var(--accent-blue);
    font-weight: 600;
}

.nav-link::after {
    content: '';
    position: absolute;
    bottom: -2px;
    left: 0;
    width: 100%;
    height: 2px;
    background-color: var(--accent-blue);
    transform: scaleX(0);
    transform-origin: right;
    transition: transform 0.3s cubic-bezier(0.25, 1, 0.5, 1);
}

.nav-link:hover::after, .nav-link.active::after {
    transform: scaleX(1);
    transform-origin: left;
}"""

css = css.replace(old_nav_link_css, new_nav_link_css)


# B. Update dark theme overrides for nav-links & gradient text & why choose us icons (Tasks 1, 3, 5)
old_dark_nav_link_css = """body.dark-theme .nav-link {
    color: #D1D5DB !important;
}
body.dark-theme .nav-link:hover, body.dark-theme .nav-link.active {
    color: #FFFFFF !important;
}"""

new_dark_nav_link_css = """body.dark-theme .nav-link {
    color: #D1D5DB !important;
}
body.dark-theme .nav-link:hover {
    color: var(--accent-cyan) !important;
}
body.dark-theme .nav-link.active {
    color: var(--accent-cyan) !important;
}
body.dark-theme .gradient-text {
    color: var(--accent-cyan) !important;
    background: none !important;
    -webkit-background-clip: initial !important;
    -webkit-text-fill-color: initial !important;
}
body.dark-theme .card-icon {
    background: rgba(255, 255, 255, 0.06) !important;
    color: var(--accent-cyan) !important;
}
body.dark-theme .card:hover .card-icon {
    background: var(--accent-blue) !important;
    color: #FFFFFF !important;
}"""

css = css.replace(old_dark_nav_link_css, new_dark_nav_link_css)


# C. Adjust gradient text in light theme (Task 3)
old_gradient_text_css = """.gradient-text {
    background: linear-gradient(135deg, #1D1D1F 30%, #86868B 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}"""

new_gradient_text_css = """.gradient-text {
    color: var(--accent-blue); /* Solid blue color instead of a low-contrast gradient */
    background: none;
    -webkit-background-clip: initial;
    -webkit-text-fill-color: initial;
}"""

css = css.replace(old_gradient_text_css, new_gradient_text_css)


# D. Adjust hero slider images to match margins (Task 4)
old_hero_img_css = """.hero-img-container {
    width: 100%;
    max-width: 480px;
    aspect-ratio: 1.25;
    border-radius: var(--radius-md);
    overflow: hidden;
    border: 1px solid rgba(0, 0, 0, 0.05);
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.05);
}"""

new_hero_img_css = """.hero-img-container {
    width: 100%;
    aspect-ratio: 1.35;
    border-radius: var(--radius-md);
    overflow: hidden;
    border: 1px solid rgba(0, 0, 0, 0.05);
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.05);
}"""

css = css.replace(old_hero_img_css, new_hero_img_css)


# E. Update social icon SVGs styles (Task 6)
old_social_icon_css = """.social-icon {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: var(--bg-secondary);
    border: none;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.1rem;
    transition: var(--transition-smooth);
}

.social-icon:hover {
    background: var(--accent-blue);
    color: var(--text-dark);
    transform: scale(1.05);
}"""

new_social_icon_css = """.social-icon {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: var(--bg-secondary);
    border: 1px solid var(--glass-border);
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--text-muted);
    transition: var(--transition-smooth);
}

.social-icon:hover {
    background: var(--accent-blue);
    color: #FFFFFF !important;
    transform: scale(1.05);
    border-color: transparent;
}

.social-icon svg {
    width: 20px;
    height: 20px;
    color: inherit;
    display: block;
    transition: var(--transition-smooth);
}"""

css = css.replace(old_social_icon_css, new_social_icon_css)


# F. Mobile view - Shift nav collapsing breakpoint from 768px to 1024px (Task 2)
# Currently, the nav elements collapse inside @media (max-width: 768px). We'll move lines 1016-1058 to a new @media (max-width: 1024px) media query.

old_collapsed_block = """    .nav-menu {
        position: fixed;
        top: 60px;
        left: -100%;
        width: 100%;
        height: calc(100vh - 60px);
        background: var(--bg-primary);
        flex-direction: column;
        align-items: center;
        padding: 40px 0;
        transition: var(--transition-smooth);
        border-top: 1px solid rgba(0, 0, 0, 0.05);
    }
    
    .nav-menu.active {
        left: 0;
    }
    
    .nav-wrapper {
        display: flex;
        justify-content: space-between;
        align-items: center;
        direction: ltr !important; /* Always keep logo on the left, hamburger toggle on the right */
    }
    
    .nav-toggle {
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    /* Toggle active animation */
    .nav-toggle.active span:nth-child(1) {
        transform: rotate(45deg) translate(6px, 6px);
    }
    
    .nav-toggle.active span:nth-child(2) {
        opacity: 0;
    }
    
    .nav-toggle.active span:nth-child(3) {
        transform: rotate(-45deg) translate(5px, -5px);
    }"""

# Remove the collapsed navigation logic from @media (max-width: 768px)
css = css.replace(old_collapsed_block, "")

# Append the new 1024px responsive navigation collapsing logic to the end of styles.css
new_1024_media_query = """

/* Tablet Collapse Breakpoint (Avoid nav-menu overlap on mid-screens) */
@media (max-width: 1024px) {
    .nav-menu {
        position: fixed;
        top: 60px;
        left: -100%;
        width: 100%;
        height: calc(100vh - 60px);
        background: var(--bg-primary);
        flex-direction: column;
        align-items: center;
        padding: 40px 0;
        transition: var(--transition-smooth);
        border-top: 1px solid rgba(0, 0, 0, 0.05);
    }
    
    .nav-menu.active {
        left: 0;
    }
    
    .nav-wrapper {
        display: flex;
        justify-content: space-between;
        align-items: center;
        direction: ltr !important; /* Always keep logo on the left, hamburger toggle on the right */
    }
    
    .nav-toggle {
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    /* Toggle active animation */
    .nav-toggle.active span:nth-child(1) {
        transform: rotate(45deg) translate(6px, 6px);
    }
    
    .nav-toggle.active span:nth-child(2) {
        opacity: 0;
    }
    
    .nav-toggle.active span:nth-child(3) {
        transform: rotate(-45deg) translate(5px, -5px);
    }
}
"""

css += new_1024_media_query

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)

print("styles.css updated with all responsive and visual styling fixes!")
