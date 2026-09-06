# 1. Modify index.html to remove the hero slider and center the text
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Normalize line endings
html = html.replace("\r\n", "\n")

old_hero_section = """        <div class="container hero-grid">
            <div class="hero-content">
                <span class="section-tag" data-i18n="index_hero_tag">Empower the Future</span>
                <h1 class="hero-title" data-i18n="index_hero_title">Empowering the Next Generation of <span class="gradient-text">Tech Creators</span></h1>
                <p class="hero-subtitle" data-i18n="index_hero_sub">
                    At NextGen Institute, we bridge the gap between academic theory and practical innovation. Join our immersive programs in AI, Machine Learning, and Data Analytics to shape the future of technology.
                </p>
                <div class="hero-actions">
                    <a href="bootcamps.html" class="btn btn-primary" id="heroCtaPrimary" data-i18n="index_hero_cta_primary">Explore Programs</a>
                </div>
            </div>
            <div class="hero-visual">
                <div class="hero-slider-container">
                    <div class="hero-slides-wrapper" id="heroSlidesWrapper">
                        <div class="hero-slide active">
                            <div class="hero-img-container">
                                <img src="assets/hero_bg.jpg?v=21" alt="AI & Data Science" class="hero-slide-img">
                            </div>
                        </div>
                        <div class="hero-slide">
                            <div class="hero-img-container">
                                <img src="assets/hero_slide2.jpg" alt="Data Analytics Dashboard" class="hero-slide-img">
                            </div>
                        </div>
                        <div class="hero-slide">
                            <div class="hero-img-container">
                                <img src="assets/hero_slide3.jpg" alt="Machine Learning Workflows" class="hero-slide-img">
                            </div>
                        </div>
                    </div>
                    <!-- Dots indicator for hero slider -->
                    <div class="hero-slider-dots" id="heroSliderDots">
                        <span class="hero-dot active" data-slide="0"></span>
                        <span class="hero-dot" data-slide="1"></span>
                        <span class="hero-dot" data-slide="2"></span>
                    </div>
                </div>
            </div>
        </div>"""

new_hero_section = """        <div class="container hero-grid-centered">
            <div class="hero-content-centered">
                <span class="section-tag" data-i18n="index_hero_tag">Empower the Future</span>
                <h1 class="hero-title" data-i18n="index_hero_title">Empowering the Next Generation of <span class="gradient-text">Tech Creators</span></h1>
                <p class="hero-subtitle" data-i18n="index_hero_sub">
                    At NextGen Institute, we bridge the gap between academic theory and practical innovation. Join our immersive programs in AI, Machine Learning, and Data Analytics to shape the future of technology.
                </p>
                <div class="hero-actions">
                    <a href="bootcamps.html" class="btn btn-primary" id="heroCtaPrimary" data-i18n="index_hero_cta_primary">Explore Programs</a>
                </div>
            </div>
        </div>"""

if old_hero_section in html:
    html = html.replace(old_hero_section, new_hero_section)
    print("index.html hero slider removed and centered successfully!")
else:
    # Fallback to general replace if any v number changed
    import re
    # We match up to class="hero-visual" block
    pattern = r'<div class="container hero-grid">.*?</div>\s*</div>\s*</div>'
    # Since regex matching can be tricky with recursive divs, let's write a simple slice-based replacement
    start_idx = html.find('<div class="container hero-grid">')
    if start_idx != -1:
        # find the end of hero-visual container before the closing </section>
        end_idx = html.find('</section>', start_idx)
        if end_idx != -1:
            slice_to_replace = html[start_idx:end_idx]
            # Replace the whole container slice
            html = html.replace(slice_to_replace, new_hero_section + "\n    ")
            print("index.html hero slider removed and centered successfully (via section slice)!")
        else:
            print("Error: Could not locate end of section in index.html")
    else:
        print("Error: Could not locate container hero-grid in index.html")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)


# 2. Modify styles.css to add the centered layout classes
with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

css = css.replace("\r\n", "\n")

centered_css = """
/* --- CENTERED HERO REDESIGN --- */
.hero-grid-centered {
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    width: 100%;
    padding: 40px 0;
}

.hero-content-centered {
    display: flex;
    flex-direction: column;
    align-items: center;
    max-width: 800px;
}

.hero-content-centered .hero-title {
    font-size: 4.2rem;
    line-height: 1.1;
    font-weight: 800;
    margin-bottom: 24px;
    letter-spacing: -0.02em;
}

.hero-content-centered .hero-subtitle {
    font-size: 1.35rem;
    line-height: 1.5;
    color: var(--text-muted);
    margin-bottom: 36px;
    max-width: 680px;
}

.hero-content-centered .hero-actions {
    display: flex;
    gap: 16px;
    justify-content: center;
    align-items: center;
}

@media (max-width: 768px) {
    .hero-content-centered .hero-title {
        font-size: 2.5rem !important;
        line-height: 1.15;
    }
    .hero-content-centered .hero-subtitle {
        font-size: 1.1rem !important;
        line-height: 1.4;
        margin-bottom: 28px;
    }
}
"""

if centered_css not in css:
    css += centered_css
    with open("styles.css", "w", encoding="utf-8") as f:
        f.write(css)
    print("styles.css updated with centered hero styles!")
else:
    print("styles.css already contains centered hero styles.")
