import os

html_dir = r"C:\NextGen Hub Website"

# 1. index.html template
index_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NextGen Hub - Empowering Tech Creators in AI & Analytics</title>
    <meta name="description" content="NextGen Hub empowers the next generation of tech creators in AI, Machine Learning, and Data Analytics through hands-on bootcamps and premier internship opportunities.">
    <link rel="stylesheet" href="styles.css">
</head>
<body>

    <!-- Header Navigation -->
    <header>
        <div class="container nav-wrapper">
            <a href="index.html" class="logo" id="logoLink">
                <span class="logo-icon">⚡</span>NextGen<span class="gradient-text">Hub</span><span class="logo-dot">.</span>
            </a>
            <button class="nav-toggle" aria-label="Toggle Navigation" id="navToggleBtn">
                <span></span>
                <span></span>
                <span></span>
            </button>
            <ul class="nav-menu" id="navMenu">
                <li><a href="index.html" class="nav-link active" id="navIndex" data-i18n="nav_home">Home</a></li>
                <li><a href="internships.html" class="nav-link" id="navInternships" data-i18n="nav_internships">Internships</a></li>
                <li><a href="bootcamps.html" class="nav-link" id="navBootcamps" data-i18n="nav_bootcamps">Bootcamps</a></li>
                <li><a href="diplomas.html" class="nav-link" id="navDiplomas" data-i18n="nav_diplomas">Diplomas</a></li>
                <li><a href="about.html" class="nav-link" id="navAbout" data-i18n="nav_about">About Us</a></li>
                <li><a href="contact.html" class="nav-link" id="navContact" data-i18n="nav_contact">Contact</a></li>
            </ul>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="hero-glow"></div>
        <div class="container hero-grid">
            <div class="hero-content">
                <span class="section-tag" data-i18n="index_hero_tag">Empower the Future</span>
                <h1 class="hero-title" data-i18n="index_hero_title">Empowering the Next Generation of <span class="gradient-text">Tech Creators</span></h1>
                <p class="hero-subtitle" data-i18n="index_hero_sub">
                    At NextGen Hub, we bridge the gap between academic theory and practical innovation. Join our immersive programs in AI, Machine Learning, and Data Analytics to shape the future of technology.
                </p>
                <div class="hero-actions">
                    <a href="bootcamps.html" class="btn btn-primary" id="heroCtaPrimary" data-i18n="index_hero_cta_primary">Explore Bootcamps</a>
                    <a href="internships.html" class="btn btn-secondary" id="heroCtaSecondary" data-i18n="index_hero_cta_secondary">View Internships</a>
                </div>
            </div>
            <div class="hero-visual">
                <!-- Floating badge 1 -->
                <div class="floating-badge badge-1 glass-panel">
                    <div class="badge-icon">AI</div>
                    <div>
                        <h4 style="font-size: 0.9rem;" data-i18n="index_badge_ml">Machine Learning</h4>
                        <span style="font-size: 0.75rem; color: var(--text-muted);" data-i18n="index_badge_nn">Neural Networks</span>
                    </div>
                </div>
                <!-- Main hero image -->
                <div class="hero-img-container">
                    <img src="assets/hero_bg.jpg" alt="AI & Data Network Visualization" id="heroImg">
                </div>
                <!-- Floating badge 2 -->
                <div class="floating-badge badge-2 glass-panel">
                    <div class="badge-icon" style="background: var(--accent-blue);">📊</div>
                    <div>
                        <h4 style="font-size: 0.9rem;" data-i18n="index_badge_da">Analytics</h4>
                        <span style="font-size: 0.75rem; color: var(--text-muted);" data-i18n="index_badge_pm">Predictive Models</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Stats & Achievements -->
    <section class="container" style="margin-top: -60px; position: relative; z-index: 5;">
        <div class="stats-grid glass-panel">
            <div class="stat-card">
                <div class="stat-number gradient-text" id="statGrads" data-i18n="index_stat_grads">500+</div>
                <div class="stat-label" data-i18n="index_stat_grads_label">Graduates</div>
            </div>
            <div class="stat-card">
                <div class="stat-number gradient-text" id="statPartners" data-i18n="index_stat_partners">15+</div>
                <div class="stat-label" data-i18n="index_stat_partners_label">Industry Partners</div>
            </div>
            <div class="stat-card">
                <div class="stat-number gradient-text" id="statRate" data-i18n="index_stat_rate">94%</div>
                <div class="stat-label" data-i18n="index_stat_rate_label">Employment Rate</div>
            </div>
        </div>
    </section>

    <!-- Core Values Section -->
    <section class="section-padding">
        <div class="container">
            <div class="section-title-wrap">
                <span class="section-tag" data-i18n="index_values_tag">Why Choose Us</span>
                <h2 class="section-title" data-i18n="index_values_title">Designed for Fast-Paced Tech Careers</h2>
                <p class="section-subtitle" data-i18n="index_values_sub">We design our curriculum around modern industry workflows, ensuring you develop skills that are in high demand.</p>
            </div>
            
            <div class="cards-grid">
                <!-- Value Card 1 -->
                <div class="card glass-panel" id="valueCard1">
                    <div class="card-icon">🧠</div>
                    <h3 class="card-title" data-i18n="index_val1_title">Cutting-Edge AI Curriculums</h3>
                    <p class="card-desc" data-i18n="index_val1_desc">Master neural networks, large language models, and computer vision with tools used by world-class tech firms.</p>
                </div>
                <!-- Value Card 2 -->
                <div class="card glass-panel" id="valueCard2">
                    <div class="card-icon">📈</div>
                    <h3 class="card-title" data-i18n="index_val2_title">Real-world Data Analytics</h3>
                    <p class="card-desc" data-i18n="index_val2_desc">Translate complex unstructured datasets into actionable business intelligence using Python, SQL, and PowerBI.</p>
                </div>
                <!-- Value Card 3 -->
                <div class="card glass-panel" id="valueCard3">
                    <div class="card-icon">🚀</div>
                    <h3 class="card-title" data-i18n="index_val3_title">Mentorship & Internships</h3>
                    <p class="card-desc" data-i18n="index_val3_desc">Work directly under senior engineers and analysts during our seasonal industry-partnered internships.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Student Success Stories (Slideshow) -->
    <section class="section-padding" style="background: var(--bg-tertiary); border-top: 1px solid rgba(15, 23, 42, 0.05); border-bottom: 1px solid rgba(15, 23, 42, 0.05);">
        <div class="container">
            <div class="section-title-wrap">
                <span class="section-tag" data-i18n="slide_tag">Success Stories</span>
                <h2 class="section-title" data-i18n="slide_title">What Our Alumni Say</h2>
                <p class="section-subtitle" data-i18n="slide_sub">Real feedback from graduates who transitioned into tech careers through NextGen Hub.</p>
            </div>
            
            <div class="slideshow-container glass-panel" style="background: var(--bg-secondary);">
                <div class="slide-track" id="slideTrack">
                    <!-- Slide 1 -->
                    <div class="slide">
                        <div class="slide-content">
                            <div class="quote-icon">“</div>
                            <p class="slide-quote" data-i18n="slide1_quote">NextGen Hub completely changed my career path. The Advanced AI Diploma gave me the exact hands-on experience and production-ready portfolio to land a job as a Machine Learning Engineer. The 1-on-1 mentorship is outstanding!</p>
                            <h4 class="slide-author" data-i18n="slide1_author">Sarah K.</h4>
                            <span class="slide-role" data-i18n="slide1_role">ML Engineer at TechCorp</span>
                        </div>
                    </div>
                    <!-- Slide 2 -->
                    <div class="slide">
                        <div class="slide-content">
                            <div class="quote-icon">“</div>
                            <p class="slide-quote" data-i18n="slide2_quote">The Python and PowerBI projects I built during the Data Analytics track allowed me to transition from marketing into a lead analyst role. The curriculum is highly practical and aligned with real enterprise metrics.</p>
                            <h4 class="slide-author" data-i18n="slide2_author">David M.</h4>
                            <span class="slide-role" data-i18n="slide2_role">Senior Data Analyst</span>
                        </div>
                    </div>
                    <!-- Slide 3 -->
                    <div class="slide">
                        <div class="slide-content">
                            <div class="quote-icon">“</div>
                            <p class="slide-quote" data-i18n="slide3_quote">Working on production systems during my internship was a game-changer. I deployed containerized models using Docker and FastAPI. It gave me the confidence to apply to senior-level roles.</p>
                            <h4 class="slide-author" data-i18n="slide3_author">Yasmine L.</h4>
                            <span class="slide-role" data-i18n="slide3_role">AI Developer Intern</span>
                        </div>
                    </div>
                </div>
                
                <!-- Navigation controls -->
                <button class="slide-btn prev-btn" id="prevSlide" aria-label="Previous Slide">‹</button>
                <button class="slide-btn next-btn" id="nextSlide" aria-label="Next Slide">›</button>
                
                <!-- Indicators -->
                <div class="slideshow-dots" id="slideshowDots">
                    <span class="dot active" data-index="0"></span>
                    <span class="dot" data-index="1"></span>
                    <span class="dot" data-index="2"></span>
                </div>
            </div>
        </div>
    </section>

    <!-- Call to Action -->
    <section class="section-padding">
        <div class="container text-center">
            <h2 class="section-title" style="margin-bottom: 24px;" data-i18n="index_cta_title">Ready to Start Your Tech Journey?</h2>
            <p class="section-subtitle" style="margin-bottom: 40px;" data-i18n="index_cta_sub">Applications for our upcoming summer cohort are now open. Spaces are limited for high-touch mentorship.</p>
            <a href="contact.html" class="btn btn-primary" id="ctaFooter" data-i18n="index_cta_btn">Get in Touch</a>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="container footer-grid">
            <div class="footer-brand">
                <a href="index.html" class="logo" style="margin-bottom: 16px;">
                    <span class="logo-icon">⚡</span>NextGen<span class="gradient-text">Hub</span>
                </a>
                <p data-i18n="footer_desc">Empowering creators, students, and engineers in data analytics and artificial intelligence. Shaping tomorrow, today.</p>
            </div>
            <div class="footer-nav">
                <h4 class="footer-nav-title" data-i18n="footer_links_title">Quick Links</h4>
                <a href="index.html" id="footerNavHome" data-i18n="nav_home">Home</a>
                <a href="internships.html" id="footerNavInternships" data-i18n="nav_internships">Internship Listings</a>
                <a href="bootcamps.html" id="footerNavBootcamps" data-i18n="nav_bootcamps">Summer Bootcamps</a>
                <a href="diplomas.html" id="footerNavDiplomas" data-i18n="nav_diplomas">Professional Diplomas</a>
            </div>
            <div class="footer-nav">
                <h4 class="footer-nav-title" data-i18n="footer_connect_title">Connect</h4>
                <a href="about.html" id="footerNavAbout" data-i18n="nav_about">About Us</a>
                <a href="contact.html" id="footerNavContact" data-i18n="nav_contact">Contact Support</a>
                <div class="social-links" style="margin-top: 16px;">
                    <a href="https://www.linkedin.com/company/nextgen-datahub/" class="social-icon" aria-label="LinkedIn" target="_blank">in</a>
                    <a href="#" class="social-icon" aria-label="Facebook" target="_blank">fb</a>
                    <a href="#" class="social-icon" aria-label="Instagram" target="_blank">ig</a>
                    <a href="#" class="social-icon" aria-label="GitHub">git</a>
                </div>
            </div>
        </div>
        <div class="container footer-bottom">
            <p data-i18n="footer_copyright">&copy; 2026 NextGen Hub. All rights reserved.</p>
            <p data-i18n="footer_design">Designed for professional excellence in AI & Analytics.</p>
        </div>
    </footer>

    <script src="main.js"></script>
    <script src="lang.js"></script>
</body>
</html>
'''

# 2. internships.html template
internships_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Internship Opportunities - NextGen Hub</title>
    <meta name="description" content="Explore current internship opportunities in AI, Machine Learning, and Data Analytics at NextGen Hub. Gain real-world project experience.">
    <link rel="stylesheet" href="styles.css">
</head>
<body>

    <!-- Header Navigation -->
    <header>
        <div class="container nav-wrapper">
            <a href="index.html" class="logo" id="logoLink">
                <span class="logo-icon">⚡</span>NextGen<span class="gradient-text">Hub</span><span class="logo-dot">.</span>
            </a>
            <button class="nav-toggle" aria-label="Toggle Navigation" id="navToggleBtn">
                <span></span>
                <span></span>
                <span></span>
            </button>
            <ul class="nav-menu" id="navMenu">
                <li><a href="index.html" class="nav-link" id="navIndex" data-i18n="nav_home">Home</a></li>
                <li><a href="internships.html" class="nav-link active" id="navInternships" data-i18n="nav_internships">Internships</a></li>
                <li><a href="bootcamps.html" class="nav-link" id="navBootcamps" data-i18n="nav_bootcamps">Bootcamps</a></li>
                <li><a href="diplomas.html" class="nav-link" id="navDiplomas" data-i18n="nav_diplomas">Diplomas</a></li>
                <li><a href="about.html" class="nav-link" id="navAbout" data-i18n="nav_about">About Us</a></li>
                <li><a href="contact.html" class="nav-link" id="navContact" data-i18n="nav_contact">Contact</a></li>
            </ul>
        </div>
    </header>

    <!-- Subpage Hero Banner -->
    <section class="section-padding" style="padding-top: 150px; background: radial-gradient(circle at 10% 20%, rgba(14, 165, 233, 0.06) 0%, transparent 50%); border-bottom: 1px solid var(--glass-border);">
        <div class="container text-center">
            <span class="section-tag" data-i18n="intern_tag">Career Acceleration</span>
            <h1 class="hero-title" style="font-size: 3rem; margin-bottom: 16px;" data-i18n="intern_title">Internship <span class="gradient-text">Opportunities</span></h1>
            <p class="section-subtitle" data-i18n="intern_sub">Real tasks, real systems, and actual mentorship. Gain production-level experience that makes you stand out to global recruiters.</p>
        </div>
    </section>

    <!-- Internships Listings -->
    <section class="section-padding">
        <div class="container">
            <div class="section-title-wrap text-center">
                <h2 class="section-title" data-i18n="intern_list_title">Open Roles</h2>
                <p class="section-subtitle" data-i18n="intern_list_sub">Select a track matching your career aspirations. We accept candidates for our Summer and Autumn cohorts.</p>
            </div>

            <div class="cards-grid">
                <!-- Role 1 -->
                <div class="card glass-panel" id="roleCard1">
                    <div class="card-icon">🤖</div>
                    <div class="card-tags">
                        <span class="tag tag-highlight" data-i18n="intern_role1_tag1">AI Research</span>
                        <span class="tag" data-i18n="intern_role1_tag2">Remote</span>
                        <span class="tag" data-i18n="intern_role1_tag3">Paid</span>
                    </div>
                    <h3 class="card-title" data-i18n="intern_role1_title">AI Research Intern (NLP & LLMs)</h3>
                    <p class="card-desc" data-i18n="intern_role1_desc">
                        Work alongside our senior researchers to evaluate, fine-tune, and deploy transformer-based models. You will assist in customizing RAG systems for enterprise document retrieval workflows.
                    </p>
                    <div class="card-footer">
                        <span style="font-size: 0.85rem; color: var(--text-muted);"><span data-i18n="intern_duration_label">Duration:</span> <b data-i18n="intern_duration_3m">3 Months</b></span>
                        <a href="contact.html?role=AI_Research" class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem;" id="applyRole1" data-i18n="intern_apply_btn">Apply Now</a>
                    </div>
                </div>

                <!-- Role 2 -->
                <div class="card glass-panel" id="roleCard2">
                    <div class="card-icon">📈</div>
                    <div class="card-tags">
                        <span class="tag tag-highlight" data-i18n="intern_role2_tag1">Data Analytics</span>
                        <span class="tag" data-i18n="intern_role2_tag2">Hybrid</span>
                        <span class="tag" data-i18n="intern_role2_tag3">Paid</span>
                    </div>
                    <h3 class="card-title" data-i18n="intern_role2_title">Data Analytics Intern</h3>
                    <p class="card-desc" data-i18n="intern_role2_desc">
                        Help translate multi-channel operational and marketing metrics into executive dashboards. You will write efficient SQL queries, design beautiful dashboards, and run exploratory data analyses (EDA).
                    </p>
                    <div class="card-footer">
                        <span style="font-size: 0.85rem; color: var(--text-muted);"><span data-i18n="intern_duration_label">Duration:</span> <b data-i18n="intern_duration_3m">3 Months</b></span>
                        <a href="contact.html?role=Data_Analytics" class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem;" id="applyRole2" data-i18n="intern_apply_btn">Apply Now</a>
                    </div>
                </div>

                <!-- Role 3 -->
                <div class="card glass-panel" id="roleCard3">
                    <div class="card-icon">⚙️</div>
                    <div class="card-tags">
                        <span class="tag tag-highlight" data-i18n="intern_role3_tag1">Machine Learning</span>
                        <span class="tag" data-i18n="intern_role3_tag2">On-site</span>
                        <span class="tag" data-i18n="intern_role3_tag3">Paid</span>
                    </div>
                    <h3 class="card-title" data-i18n="intern_role3_title">Machine Learning Engineer Intern</h3>
                    <p class="card-desc" data-i18n="intern_role3_desc">
                        Support the deployment and containerization of deep learning models in production environments. You will optimize inference latency using tools like ONNX, Docker, and Kubernetes.
                    </p>
                    <div class="card-footer">
                        <span style="font-size: 0.85rem; color: var(--text-muted);"><span data-i18n="intern_duration_label">Duration:</span> <b data-i18n="intern_duration_6m">6 Months</b></span>
                        <a href="contact.html?role=ML_Engineer" class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem;" id="applyRole3" data-i18n="intern_apply_btn">Apply Now</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Program Highlights / Benefits -->
    <section class="section-padding" style="background: var(--bg-secondary); border-top: 1px solid var(--glass-border);">
        <div class="container">
            <div class="section-title-wrap text-center">
                <span class="section-tag" data-i18n="intern_benefits_tag">Benefits</span>
                <h2 class="section-title" data-i18n="intern_benefits_title">What We Offer</h2>
                <p class="section-subtitle" data-i18n="intern_benefits_sub">Our program is designed to launch your professional career with solid foundational support.</p>
            </div>

            <div class="cards-grid">
                <div class="card glass-panel" style="padding: 30px; border-color: transparent;" id="benefit1">
                    <h3 class="card-title" style="color: var(--accent-cyan);" data-i18n="intern_ben1_title">👥 Direct Mentorship</h3>
                    <p class="card-desc" style="font-size: 0.9rem;" data-i18n="intern_ben1_desc">You will be paired with an industry mentor who holds regular 1-on-1 feedback sessions to map out your career growth.</p>
                </div>
                <div class="card glass-panel" style="padding: 30px; border-color: transparent;" id="benefit2">
                    <h3 class="card-title" style="color: var(--accent-violet);" data-i18n="intern_ben2_title">💻 Real Production Code</h3>
                    <p class="card-desc" style="font-size: 0.9rem;" data-i18n="intern_ben2_desc">No coffee runs or meaningless tasks. You contribute directly to products, client assets, and open-source packages.</p>
                </div>
                <div class="card glass-panel" style="padding: 30px; border-color: transparent;" id="benefit3">
                    <h3 class="card-title" style="color: var(--accent-indigo);" data-i18n="intern_ben3_title">💼 Interview Prep & Referral</h3>
                    <p class="card-desc" style="font-size: 0.9rem;" data-i18n="intern_ben3_desc">Graduating interns receive referral recommendations and mock technical interview training with our leadership team.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="container footer-grid">
            <div class="footer-brand">
                <a href="index.html" class="logo" style="margin-bottom: 16px;">
                    <span class="logo-icon">⚡</span>NextGen<span class="gradient-text">Hub</span>
                </a>
                <p data-i18n="footer_desc">Empowering creators, students, and engineers in data analytics and artificial intelligence. Shaping tomorrow, today.</p>
            </div>
            <div class="footer-nav">
                <h4 class="footer-nav-title" data-i18n="footer_links_title">Quick Links</h4>
                <a href="index.html" id="footerNavHome" data-i18n="nav_home">Home</a>
                <a href="internships.html" id="footerNavInternships" data-i18n="nav_internships">Internship Listings</a>
                <a href="bootcamps.html" id="footerNavBootcamps" data-i18n="nav_bootcamps">Summer Bootcamps</a>
                <a href="diplomas.html" id="footerNavDiplomas" data-i18n="nav_diplomas">Professional Diplomas</a>
            </div>
            <div class="footer-nav">
                <h4 class="footer-nav-title" data-i18n="footer_connect_title">Connect</h4>
                <a href="about.html" id="footerNavAbout" data-i18n="nav_about">About Us</a>
                <a href="contact.html" id="footerNavContact" data-i18n="nav_contact">Contact Support</a>
                <div class="social-links" style="margin-top: 16px;">
                    <a href="https://www.linkedin.com/company/nextgen-datahub/" class="social-icon" aria-label="LinkedIn" target="_blank">in</a>
                    <a href="#" class="social-icon" aria-label="Facebook" target="_blank">fb</a>
                    <a href="#" class="social-icon" aria-label="Instagram" target="_blank">ig</a>
                    <a href="#" class="social-icon" aria-label="GitHub">git</a>
                </div>
            </div>
        </div>
        <div class="container footer-bottom">
            <p data-i18n="footer_copyright">&copy; 2026 NextGen Hub. All rights reserved.</p>
            <p data-i18n="footer_design">Designed for professional excellence in AI & Analytics.</p>
        </div>
    </footer>

    <script src="main.js"></script>
    <script src="lang.js"></script>
</body>
</html>
'''

# 3. bootcamps.html template
bootcamps_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Summer Bootcamps - NextGen Hub</title>
    <meta name="description" content="View upcoming summer bootcamps in Data Analytics and AI/ML at NextGen Hub. Complete course schedule from July 1, 2026 to October 1, 2026.">
    <link rel="stylesheet" href="styles.css">
</head>
<body>

    <!-- Header Navigation -->
    <header>
        <div class="container nav-wrapper">
            <a href="index.html" class="logo" id="logoLink">
                <span class="logo-icon">⚡</span>NextGen<span class="gradient-text">Hub</span><span class="logo-dot">.</span>
            </a>
            <button class="nav-toggle" aria-label="Toggle Navigation" id="navToggleBtn">
                <span></span>
                <span></span>
                <span></span>
            </button>
            <ul class="nav-menu" id="navMenu">
                <li><a href="index.html" class="nav-link" id="navIndex" data-i18n="nav_home">Home</a></li>
                <li><a href="internships.html" class="nav-link" id="navInternships" data-i18n="nav_internships">Internships</a></li>
                <li><a href="bootcamps.html" class="nav-link active" id="navBootcamps" data-i18n="nav_bootcamps">Bootcamps</a></li>
                <li><a href="diplomas.html" class="nav-link" id="navDiplomas" data-i18n="nav_diplomas">Diplomas</a></li>
                <li><a href="about.html" class="nav-link" id="navAbout" data-i18n="nav_about">About Us</a></li>
                <li><a href="contact.html" class="nav-link" id="navContact" data-i18n="nav_contact">Contact</a></li>
            </ul>
        </div>
    </header>

    <!-- Subpage Hero Banner -->
    <section class="section-padding" style="padding-top: 150px; background: radial-gradient(circle at 90% 10%, rgba(14, 165, 233, 0.06) 0%, transparent 50%); border-bottom: 1px solid var(--glass-border);">
        <div class="container text-center">
            <span class="section-tag" data-i18n="boot_tag">Rigorous Training</span>
            <h1 class="hero-title" style="font-size: 3rem; margin-bottom: 16px;" data-i18n="boot_title">Summer <span class="gradient-text">Bootcamps 2026</span></h1>
            <p class="section-subtitle" data-i18n="boot_sub">From foundation to production. Choose a path, roll up your sleeves, and master the technical frameworks defining our century.</p>
        </div>
    </section>

    <!-- Schedule Table Section -->
    <section class="section-padding">
        <div class="container">
            <div class="section-title-wrap text-center">
                <h2 class="section-title" data-i18n="boot_schedule_title">Program Schedule & Curriculum</h2>
                <p class="section-subtitle" data-i18n="boot_schedule_sub">Timeline: <b>July 1, 2026 to October 1, 2026</b>. Sessions are held live online with interactive laboratory hours.</p>
            </div>

            <!-- Schedule Table Wrapper -->
            <div class="table-responsive">
                <table class="schedule-table" id="scheduleTable">
                    <thead>
                        <tr>
                            <th data-i18n="boot_table_th_phase">Phase & Date</th>
                            <th data-i18n="boot_table_th_data">Data Analytics Track</th>
                            <th data-i18n="boot_table_th_ai">AI / Machine Learning Track</th>
                            <th data-i18n="boot_table_th_status">Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>
                                <b data-i18n="boot_table_w14">Weeks 1 - 4</b><br>
                                <span style="font-size: 0.85rem; color: var(--text-muted);" data-i18n="boot_table_w14_date">Jul 1 - Jul 28, 2026</span>
                            </td>
                            <td>
                                <b data-i18n="boot_table_w14_data_t">Foundations of Business Data</b><br>
                                <span data-i18n="boot_table_w14_data_d">Advanced SQL queries, schema structures, and data manipulation in PostgreSQL.</span>
                            </td>
                            <td>
                                <b data-i18n="boot_table_w14_ai_t">Mathematical Foundations & PyTorch</b><br>
                                <span data-i18n="boot_table_w14_ai_d">Linear algebra, calculus, probability, and basic neural network design in PyTorch.</span>
                            </td>
                            <td><span class="status-badge status-upcoming" data-i18n="boot_table_status_upcoming">Upcoming</span></td>
                        </tr>
                        <tr>
                            <td>
                                <b data-i18n="boot_table_w58">Weeks 5 - 8</b><br>
                                <span style="font-size: 0.85rem; color: var(--text-muted);" data-i18n="boot_table_w58_date">Jul 29 - Aug 25, 2026</span>
                            </td>
                            <td>
                                <b data-i18n="boot_table_w58_data_t">Data Visualizations & BI</b><br>
                                <span data-i18n="boot_table_w58_data_d">Transforming data into insights with PowerBI, Tableau, and custom Python plots (Seaborn).</span>
                            </td>
                            <td>
                                <b data-i18n="boot_table_w58_ai_t">Supervised & Unsupervised Learning</b><br>
                                <span data-i18n="boot_table_w58_ai_d">Regressions, classification models, decision trees, clustering (K-Means), and validation metrics.</span>
                            </td>
                            <td><span class="status-badge status-upcoming" data-i18n="boot_table_status_upcoming">Upcoming</span></td>
                        </tr>
                        <tr>
                            <td>
                                <b data-i18n="boot_table_w912">Weeks 9 - 12</b><br>
                                <span style="font-size: 0.85rem; color: var(--text-muted);" data-i18n="boot_table_w912_date">Aug 26 - Sep 22, 2026</span>
                            </td>
                            <td>
                                <b data-i18n="boot_table_w912_data_t">Exploratory Analysis & Wrangling</b><br>
                                <span data-i18n="boot_table_w912_data_d">NumPy, Pandas, missing value treatments, and advanced feature engineering methodologies.</span>
                            </td>
                            <td>
                                <b data-i18n="boot_table_w912_ai_t">Deep Learning & Large Models</b><br>
                                <span data-i18n="boot_table_w912_ai_d">CNNs for Computer Vision, Transformers for NLP, and fine-tuning Open-Source LLMs.</span>
                            </td>
                            <td><span class="status-badge status-open" data-i18n="boot_table_status_open">Open for Reg</span></td>
                        </tr>
                        <tr>
                            <td>
                                <b data-i18n="boot_table_wfinal">Final Cohort Week</b><br>
                                <span style="font-size: 0.85rem; color: var(--text-muted);" data-i18n="boot_table_wfinal_date">Sep 23 - Oct 1, 2026</span>
                            </td>
                            <td>
                                <b data-i18n="boot_table_wfinal_data_t">Capstone Business Analytics Project</b><br>
                                <span data-i18n="boot_table_wfinal_data_d">Interactive reporting dashboard deployed on cloud to solve a logistics optimization case study.</span>
                            </td>
                            <td>
                                <b data-i18n="boot_table_wfinal_ai_t">MLOps & Model Deployment</b><br>
                                <span data-i18n="boot_table_wfinal_ai_d">Wrapping algorithms inside FastAPI, containerizing with Docker, and cloud orchestration.</span>
                            </td>
                            <td><span class="status-badge status-open" data-i18n="boot_table_status_open">Open for Reg</span></td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- Enrollment CTA -->
            <div style="margin-top: 48px;" class="text-center">
                <a href="contact.html?inquiry=Bootcamp_Registration" class="btn btn-primary" id="registerCta" data-i18n="boot_register_cta">Reserve My Spot</a>
            </div>
        </div>
    </section>

    <!-- FAQ Section -->
    <section class="section-padding" style="background: var(--bg-secondary); border-top: 1px solid var(--glass-border);">
        <div class="container">
            <div class="section-title-wrap text-center">
                <span class="section-tag" data-i18n="boot_faq_tag">Common Queries</span>
                <h2 class="section-title" data-i18n="boot_faq_title">Frequently Asked Questions</h2>
                <p class="section-subtitle" data-i18n="boot_faq_sub">Need more details? Here are answers to common questions about our bootcamps.</p>
            </div>

            <div class="cards-grid" style="grid-template-columns: repeat(auto-fit, minmax(450px, 1fr));">
                <!-- FAQ 1 -->
                <div class="card glass-panel" style="padding: 30px;" id="faqCard1">
                    <h3 class="card-title" style="font-size: 1.15rem; color: var(--accent-cyan);" data-i18n="boot_faq1_q">What are the prerequisites for the AI/ML track?</h3>
                    <p class="card-desc" style="font-size: 0.9rem;" data-i18n="boot_faq1_a">Basic Python familiarity and high-school-level math are recommended. We provide pre-course self-study materials two weeks before July 1st to bring you up to speed.</p>
                </div>
                <!-- FAQ 2 -->
                <div class="card glass-panel" style="padding: 30px;" id="faqCard2">
                    <h3 class="card-title" style="font-size: 1.15rem; color: var(--accent-violet);" data-i18n="boot_faq2_q">Is there a certificate provided upon graduation?</h3>
                    <p class="card-desc" style="font-size: 0.9rem;" data-i18n="boot_faq2_a">Yes. All graduates who successfully complete their capstone project and pass the final review will receive an authenticated digital Certificate of Completion.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="container footer-grid">
            <div class="footer-brand">
                <a href="index.html" class="logo" style="margin-bottom: 16px;">
                    <span class="logo-icon">⚡</span>NextGen<span class="gradient-text">Hub</span>
                </a>
                <p data-i18n="footer_desc">Empowering creators, students, and engineers in data analytics and artificial intelligence. Shaping tomorrow, today.</p>
            </div>
            <div class="footer-nav">
                <h4 class="footer-nav-title" data-i18n="footer_links_title">Quick Links</h4>
                <a href="index.html" id="footerNavHome" data-i18n="nav_home">Home</a>
                <a href="internships.html" id="footerNavInternships" data-i18n="nav_internships">Internship Listings</a>
                <a href="bootcamps.html" id="footerNavBootcamps" data-i18n="nav_bootcamps">Summer Bootcamps</a>
                <a href="diplomas.html" id="footerNavDiplomas" data-i18n="nav_diplomas">Professional Diplomas</a>
            </div>
            <div class="footer-nav">
                <h4 class="footer-nav-title" data-i18n="footer_connect_title">Connect</h4>
                <a href="about.html" id="footerNavAbout" data-i18n="nav_about">About Us</a>
                <a href="contact.html" id="footerNavContact" data-i18n="nav_contact">Contact Support</a>
                <div class="social-links" style="margin-top: 16px;">
                    <a href="https://www.linkedin.com/company/nextgen-datahub/" class="social-icon" aria-label="LinkedIn" target="_blank">in</a>
                    <a href="#" class="social-icon" aria-label="Facebook" target="_blank">fb</a>
                    <a href="#" class="social-icon" aria-label="Instagram" target="_blank">ig</a>
                    <a href="#" class="social-icon" aria-label="GitHub">git</a>
                </div>
            </div>
        </div>
        <div class="container footer-bottom">
            <p data-i18n="footer_copyright">&copy; 2026 NextGen Hub. All rights reserved.</p>
            <p data-i18n="footer_design">Designed for professional excellence in AI & Analytics.</p>
        </div>
    </footer>

    <script src="main.js"></script>
    <script src="lang.js"></script>
</body>
</html>
'''

# 4. diplomas.html template
diplomas_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Professional Diplomas - NextGen Hub</title>
    <meta name="description" content="Enroll in NextGen Hub's professional diplomas in AI and Data Analytics. Comprehensive 6 to 9-month programs with industry certification and co-op placement.">
    <link rel="stylesheet" href="styles.css">
</head>
<body>

    <!-- Header Navigation -->
    <header>
        <div class="container nav-wrapper">
            <a href="index.html" class="logo" id="logoLink">
                <span class="logo-icon">⚡</span>NextGen<span class="gradient-text">Hub</span><span class="logo-dot">.</span>
            </a>
            <button class="nav-toggle" aria-label="Toggle Navigation" id="navToggleBtn">
                <span></span>
                <span></span>
                <span></span>
            </button>
            <ul class="nav-menu" id="navMenu">
                <li><a href="index.html" class="nav-link" id="navIndex" data-i18n="nav_home">Home</a></li>
                <li><a href="internships.html" class="nav-link" id="navInternships" data-i18n="nav_internships">Internships</a></li>
                <li><a href="bootcamps.html" class="nav-link" id="navBootcamps" data-i18n="nav_bootcamps">Bootcamps</a></li>
                <li><a href="diplomas.html" class="nav-link active" id="navDiplomas" data-i18n="nav_diplomas">Diplomas</a></li>
                <li><a href="about.html" class="nav-link" id="navAbout" data-i18n="nav_about">About Us</a></li>
                <li><a href="contact.html" class="nav-link" id="navContact" data-i18n="nav_contact">Contact</a></li>
            </ul>
        </div>
    </header>

    <!-- Subpage Hero Banner -->
    <section class="section-padding" style="padding-top: 150px; background: radial-gradient(circle at 50% 50%, rgba(14, 165, 233, 0.06) 0%, transparent 60%); border-bottom: 1px solid var(--glass-border);">
        <div class="container text-center">
            <span class="section-tag" data-i18n="diploma_tag">Long-Term Specialization</span>
            <h1 class="hero-title" style="font-size: 3rem; margin-bottom: 16px;" data-i18n="diploma_title">Professional <span class="gradient-text">Diplomas</span></h1>
            <p class="section-subtitle" data-i18n="diploma_sub">Comprehensive 6 to 9-month programs built to take you from absolute foundations to job-ready expertise with direct placement opportunities.</p>
        </div>
    </section>

    <!-- Diplomas List Section -->
    <section class="section-padding">
        <div class="container">
            <div class="section-title-wrap text-center">
                <h2 class="section-title" data-i18n="diploma_list_title">Available Specialization Tracks</h2>
                <p class="section-subtitle" data-i18n="diploma_list_sub">Choose a professional track. Each diploma includes weekly coding labs, live case studies, and a final capstone reviewed by industry experts.</p>
            </div>

            <div class="cards-grid">
                <!-- Diploma 1 -->
                <div class="card glass-panel" id="diplomaCard1">
                    <div class="card-icon">🎓</div>
                    <div class="card-tags">
                        <span class="tag tag-highlight" data-i18n="intern_role1_tag1">Artificial Intelligence</span>
                        <span class="tag" data-i18n="intern_role3_tag1">6 Months</span>
                        <span class="tag" data-i18n="diploma_d1_f4">Certification</span>
                    </div>
                    <h3 class="card-title" data-i18n="diploma_d1_title">Advanced AI & Deep Learning Diploma</h3>
                    <p class="card-desc" data-i18n="diploma_d1_desc">
                        A rigorous curriculum focusing on advanced neural networks, natural language processing, computer vision, and modern generative AI architectures. Built for aspiring AI specialists and software engineers.
                    </p>
                    <ul style="list-style: none; margin-bottom: 28px; font-size: 0.9rem; color: var(--text-muted); display: flex; flex-direction: column; gap: 8px; text-align: left;">
                        <li><span style="color: var(--accent-cyan); margin-right: 8px; font-weight: bold;">✓</span><span data-i18n="diploma_d1_f1">Deep Learning & Math Foundations</span></li>
                        <li><span style="color: var(--accent-cyan); margin-right: 8px; font-weight: bold;">✓</span><span data-i18n="diploma_d1_f2">Natural Language Processing & LLMs</span></li>
                        <li><span style="color: var(--accent-cyan); margin-right: 8px; font-weight: bold;">✓</span><span data-i18n="diploma_d1_f3">Computer Vision & Image Processing</span></li>
                        <li><span style="color: var(--accent-cyan); margin-right: 8px; font-weight: bold;">✓</span><span data-i18n="diploma_d1_f4">MLOps, Docker, and Cloud Deployment</span></li>
                    </ul>
                    <div class="card-footer">
                        <span style="font-size: 0.85rem; color: var(--text-muted);"><span data-i18n="diploma_format_label">Format:</span> <b data-i18n="diploma_format_val">Hybrid / Online</b></span>
                        <a href="contact.html?inquiry=AI_Diploma" class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem;" id="learnDiploma1" data-i18n="diploma_enroll_btn">Enroll Inquiry</a>
                    </div>
                </div>

                <!-- Diploma 2 -->
                <div class="card glass-panel" id="diplomaCard2">
                    <div class="card-icon">🏢</div>
                    <div class="card-tags">
                        <span class="tag tag-highlight" data-i18n="intern_role2_tag1">Data Analytics</span>
                        <span class="tag">9 Months</span>
                        <span class="tag" data-i18n="diploma_ben1_title">Co-op Placement</span>
                    </div>
                    <h3 class="card-title" data-i18n="diploma_d2_title">Enterprise Data Analytics & Engineering</h3>
                    <p class="card-desc" data-i18n="diploma_d2_desc">
                        Master the architectures of enterprise business intelligence. Learn SQL database modeling, big data wrangling with Python, and cloud-native dashboard automation.
                    </p>
                    <ul style="list-style: none; margin-bottom: 28px; font-size: 0.9rem; color: var(--text-muted); display: flex; flex-direction: column; gap: 8px; text-align: left;">
                        <li><span style="color: var(--accent-cyan); margin-right: 8px; font-weight: bold;">✓</span><span data-i18n="diploma_d2_f1">Advanced SQL & Relational Databases</span></li>
                        <li><span style="color: var(--accent-cyan); margin-right: 8px; font-weight: bold;">✓</span><span data-i18n="diploma_d2_f2">Python Data Analysis (Pandas, Numpy)</span></li>
                        <li><span style="color: var(--accent-cyan); margin-right: 8px; font-weight: bold;">✓</span><span data-i18n="diploma_d2_f3">BI Architectures (PowerBI, Tableau)</span></li>
                        <li><span style="color: var(--accent-cyan); margin-right: 8px; font-weight: bold;">✓</span><span data-i18n="diploma_d2_f4">Cloud Data Warehousing (Snowflake/AWS)</span></li>
                    </ul>
                    <div class="card-footer">
                        <span style="font-size: 0.85rem; color: var(--text-muted);"><span data-i18n="diploma_format_label">Format:</span> <b data-i18n="diploma_format_val">Hybrid / Online</b></span>
                        <a href="contact.html?inquiry=Data_Diploma" class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem;" id="learnDiploma2" data-i18n="diploma_enroll_btn">Enroll Inquiry</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Why Diplomas Section -->
    <section class="section-padding" style="background: var(--bg-secondary); border-top: 1px solid var(--glass-border);">
        <div class="container">
            <div class="section-title-wrap text-center">
                <span class="section-tag" data-i18n="diploma_benefits_tag">Career Placement</span>
                <h2 class="section-title" data-i18n="diploma_benefits_title">Diploma Benefits & Co-Op Support</h2>
                <p class="section-subtitle" data-i18n="diploma_benefits_sub">How our diploma tracks help you secure high-paying roles in regional and global tech companies.</p>
            </div>

            <div class="cards-grid" style="grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));">
                <div class="card glass-panel" style="padding: 30px; border-color: transparent;" id="benefit1">
                    <h3 class="card-title" style="color: var(--accent-cyan);" data-i18n="diploma_ben1_title">💼 Guaranteed Internship Placement</h3>
                    <p class="card-desc" style="font-size: 0.9rem;" data-i18n="diploma_ben1_desc">All diploma students who maintain a passing grade receive a guaranteed 3-month paid internship with our partner networks upon graduation.</p>
                </div>
                <div class="card glass-panel" style="padding: 30px; border-color: transparent;" id="benefit2">
                    <h3 class="card-title" style="color: var(--accent-violet);" data-i18n="diploma_ben2_title">📂 Portfolio Creation</h3>
                    <p class="card-desc" style="font-size: 0.9rem;" data-i18n="diploma_ben2_desc">Build 4 comprehensive production-ready projects in Git, showing prospective employers that you can design and deploy full industrial systems.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="container footer-grid">
            <div class="footer-brand">
                <a href="index.html" class="logo" style="margin-bottom: 16px;">
                    <span class="logo-icon">⚡</span>NextGen<span class="gradient-text">Hub</span>
                </a>
                <p data-i18n="footer_desc">Empowering creators, students, and engineers in data analytics and artificial intelligence. Shaping tomorrow, today.</p>
            </div>
            <div class="footer-nav">
                <h4 class="footer-nav-title" data-i18n="footer_links_title">Quick Links</h4>
                <a href="index.html" id="footerNavHome" data-i18n="nav_home">Home</a>
                <a href="internships.html" id="footerNavInternships" data-i18n="nav_internships">Internship Listings</a>
                <a href="bootcamps.html" id="footerNavBootcamps" data-i18n="nav_bootcamps">Summer Bootcamps</a>
                <a href="diplomas.html" id="footerNavDiplomas" data-i18n="nav_diplomas">Professional Diplomas</a>
            </div>
            <div class="footer-nav">
                <h4 class="footer-nav-title" data-i18n="footer_connect_title">Connect</h4>
                <a href="about.html" id="footerNavAbout" data-i18n="nav_about">About Us</a>
                <a href="contact.html" id="footerNavContact" data-i18n="nav_contact">Contact Support</a>
                <div class="social-links" style="margin-top: 16px;">
                    <a href="https://www.linkedin.com/company/nextgen-datahub/" class="social-icon" aria-label="LinkedIn" target="_blank">in</a>
                    <a href="#" class="social-icon" aria-label="Facebook" target="_blank">fb</a>
                    <a href="#" class="social-icon" aria-label="Instagram" target="_blank">ig</a>
                    <a href="#" class="social-icon" aria-label="GitHub">git</a>
                </div>
            </div>
        </div>
        <div class="container footer-bottom">
            <p data-i18n="footer_copyright">&copy; 2026 NextGen Hub. All rights reserved.</p>
            <p data-i18n="footer_design">Designed for professional excellence in AI & Analytics.</p>
        </div>
    </footer>

    <script src="main.js"></script>
    <script src="lang.js"></script>
</body>
</html>
'''

# 5. about.html template
about_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Us - NextGen Hub</title>
    <meta name="description" content="Discover the vision and mission of NextGen Hub, and meet our program leadership driving educational excellence in technology fields.">
    <link rel="stylesheet" href="styles.css">
</head>
<body>

    <!-- Header Navigation -->
    <header>
        <div class="container nav-wrapper">
            <a href="index.html" class="logo" id="logoLink">
                <span class="logo-icon">⚡</span>NextGen<span class="gradient-text">Hub</span><span class="logo-dot">.</span>
            </a>
            <button class="nav-toggle" aria-label="Toggle Navigation" id="navToggleBtn">
                <span></span>
                <span></span>
                <span></span>
            </button>
            <ul class="nav-menu" id="navMenu">
                <li><a href="index.html" class="nav-link" id="navIndex" data-i18n="nav_home">Home</a></li>
                <li><a href="internships.html" class="nav-link" id="navInternships" data-i18n="nav_internships">Internships</a></li>
                <li><a href="bootcamps.html" class="nav-link" id="navBootcamps" data-i18n="nav_bootcamps">Bootcamps</a></li>
                <li><a href="diplomas.html" class="nav-link" id="navDiplomas" data-i18n="nav_diplomas">Diplomas</a></li>
                <li><a href="about.html" class="nav-link active" id="navAbout" data-i18n="nav_about">About Us</a></li>
                <li><a href="contact.html" class="nav-link" id="navContact" data-i18n="nav_contact">Contact</a></li>
            </ul>
        </div>
    </header>

    <!-- Subpage Hero Banner -->
    <section class="section-padding" style="padding-top: 150px; background: radial-gradient(circle at 50% 50%, rgba(99, 102, 241, 0.06) 0%, transparent 60%); border-bottom: 1px solid var(--glass-border);">
        <div class="container text-center">
            <span class="section-tag" data-i18n="about_banner_tag">Our Story</span>
            <h1 class="hero-title" style="font-size: 3rem; margin-bottom: 16px;" data-i18n="about_banner_title">About <span class="gradient-text">NextGen Hub</span></h1>
            <p class="section-subtitle" data-i18n="about_banner_sub">A collective of developers, data modelers, and analytical professionals dedicated to cultivating regional technical competencies.</p>
        </div>
    </section>

    <!-- Vision & Mission Details -->
    <section class="section-padding">
        <div class="container about-grid">
            <div class="vision-text">
                <span class="section-tag" style="text-align: left;" data-i18n="about_vision_tag">Foundational Goal</span>
                <h2 class="section-title" style="font-size: 2.2rem; text-align: left; margin-bottom: 24px;" data-i18n="about_vision_title">Fostering Innovation, One Engineer at a Time</h2>
                <p style="color: var(--text-muted); margin-bottom: 20px;" data-i18n="about_vision_sub1">
                    NextGen Hub was conceived with a simple objective: to solve the tech talent shortage by establishing high-level training pathways. We believe traditional learning processes are too slow for today's AI transformation. By focusing strictly on hands-on deployment, we prepare candidates for actual tasks instantly.
                </p>
                <p style="color: var(--text-muted); margin-bottom: 20px;" data-i18n="about_vision_sub2">
                    Whether it's data visualization for corporate logistics or containerizing transformers for conversational AI chatbots, our members gain direct exposure to real technical challenges.
                </p>
                
                <!-- Core Values list -->
                <div style="margin-top: 32px; display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
                    <div style="display: flex; gap: 12px; align-items: flex-start;">
                        <span style="color: var(--accent-cyan); font-weight: bold; font-size: 1.2rem;">✓</span>
                        <div>
                            <h4 style="font-size: 0.95rem; margin-bottom: 4px;" data-i18n="about_val1_title">Industry Relevance</h4>
                            <p style="font-size: 0.85rem; color: var(--text-muted);" data-i18n="about_val1_desc">Curriculums adapt continuously to mirror actual market frameworks.</p>
                        </div>
                    </div>
                    <div style="display: flex; gap: 12px; align-items: flex-start;">
                        <span style="color: var(--accent-violet); font-weight: bold; font-size: 1.2rem;">✓</span>
                        <div>
                            <h4 style="font-size: 0.95rem; margin-bottom: 4px;" data-i18n="about_val2_title">Collaborative Spirit</h4>
                            <p style="font-size: 0.85rem; color: var(--text-muted);" data-i18n="about_val2_desc">Shared research labs encourage cooperative team-level problem solving.</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Leadership / Manager Profile -->
            <div class="manager-card glass-panel" id="managerCard">
                <div class="manager-avatar">
                    <img src="assets/manager_avatar.jpg" alt="Program Leadership Avatar" id="managerAvatarImg">
                </div>
                <h3 class="manager-title" data-i18n="about_mgr_title">Program Director</h3>
                <div class="manager-role" data-i18n="about_mgr_role">NextGen Hub Manager</div>
                <p class="manager-bio" data-i18n="about_mgr_bio">
                    Dedicated to designing educational modules and coordinating industry partnerships. Ensuring that every participant receives quality project guidance, state-of-the-art infrastructure, and continuous recruitment access.
                </p>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="container footer-grid">
            <div class="footer-brand">
                <a href="index.html" class="logo" style="margin-bottom: 16px;">
                    <span class="logo-icon">⚡</span>NextGen<span class="gradient-text">Hub</span>
                </a>
                <p data-i18n="footer_desc">Empowering creators, students, and engineers in data analytics and artificial intelligence. Shaping tomorrow, today.</p>
            </div>
            <div class="footer-nav">
                <h4 class="footer-nav-title" data-i18n="footer_links_title">Quick Links</h4>
                <a href="index.html" id="footerNavHome" data-i18n="nav_home">Home</a>
                <a href="internships.html" id="footerNavInternships" data-i18n="nav_internships">Internship Listings</a>
                <a href="bootcamps.html" id="footerNavBootcamps" data-i18n="nav_bootcamps">Summer Bootcamps</a>
                <a href="diplomas.html" id="footerNavDiplomas" data-i18n="nav_diplomas">Professional Diplomas</a>
            </div>
            <div class="footer-nav">
                <h4 class="footer-nav-title" data-i18n="footer_connect_title">Connect</h4>
                <a href="about.html" id="footerNavAbout" data-i18n="nav_about">About Us</a>
                <a href="contact.html" id="footerNavContact" data-i18n="nav_contact">Contact Support</a>
                <div class="social-links" style="margin-top: 16px;">
                    <a href="https://www.linkedin.com/company/nextgen-datahub/" class="social-icon" aria-label="LinkedIn" target="_blank">in</a>
                    <a href="#" class="social-icon" aria-label="Facebook" target="_blank">fb</a>
                    <a href="#" class="social-icon" aria-label="Instagram" target="_blank">ig</a>
                    <a href="#" class="social-icon" aria-label="GitHub">git</a>
                </div>
            </div>
        </div>
        <div class="container footer-bottom">
            <p data-i18n="footer_copyright">&copy; 2026 NextGen Hub. All rights reserved.</p>
            <p data-i18n="footer_design">Designed for professional excellence in AI & Analytics.</p>
        </div>
    </footer>

    <script src="main.js"></script>
    <script src="lang.js"></script>
</body>
</html>
'''

# 6. contact.html template
contact_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us - NextGen Hub</title>
    <meta name="description" content="Reach out to the NextGen Hub team for inquiries about internships, bootcamps, and business partnerships. We respond within 24 hours.">
    <link rel="stylesheet" href="styles.css">
</head>
<body>

    <!-- Header Navigation -->
    <header>
        <div class="container nav-wrapper">
            <a href="index.html" class="logo" id="logoLink">
                <span class="logo-icon">⚡</span>NextGen<span class="gradient-text">Hub</span><span class="logo-dot">.</span>
            </a>
            <button class="nav-toggle" aria-label="Toggle Navigation" id="navToggleBtn">
                <span></span>
                <span></span>
                <span></span>
            </button>
            <ul class="nav-menu" id="navMenu">
                <li><a href="index.html" class="nav-link" id="navIndex" data-i18n="nav_home">Home</a></li>
                <li><a href="internships.html" class="nav-link" id="navInternships" data-i18n="nav_internships">Internships</a></li>
                <li><a href="bootcamps.html" class="nav-link" id="navBootcamps" data-i18n="nav_bootcamps">Bootcamps</a></li>
                <li><a href="diplomas.html" class="nav-link" id="navDiplomas" data-i18n="nav_diplomas">Diplomas</a></li>
                <li><a href="about.html" class="nav-link" id="navAbout" data-i18n="nav_about">About Us</a></li>
                <li><a href="contact.html" class="nav-link active" id="navContact" data-i18n="nav_contact">Contact</a></li>
            </ul>
        </div>
    </header>

    <!-- Subpage Hero Banner -->
    <section class="section-padding" style="padding-top: 150px; background: radial-gradient(circle at 10% 80%, rgba(99, 102, 241, 0.08) 0%, transparent 60%); border-bottom: 1px solid var(--glass-border);">
        <div class="container text-center">
            <span class="section-tag" data-i18n="contact_banner_tag">Get in Touch</span>
            <h1 class="hero-title" style="font-size: 3rem; margin-bottom: 16px;" data-i18n="contact_banner_title">Contact <span class="gradient-text">Our Team</span></h1>
            <p class="section-subtitle" data-i18n="contact_banner_sub">Have questions about applications, bootcamps, or enterprise hiring programs? Let's start a conversation.</p>
        </div>
    </section>

    <!-- Contact Form & Info Details -->
    <section class="section-padding">
        <div class="container contact-grid">
            
            <!-- Contact Info -->
            <div class="contact-info">
                <div>
                    <span class="section-tag" style="text-align: left;" data-i18n="contact_info_tag">Details</span>
                    <h2 class="section-title" style="font-size: 2.2rem; text-align: left; margin-bottom: 12px;" data-i18n="contact_info_title">Contact Information</h2>
                    <p style="color: var(--text-muted); font-size: 0.95rem;" data-i18n="contact_info_sub">You can contact us via email or social media. We typically reply within 1 business day.</p>
                </div>

                <div class="contact-info-item">
                    <div class="contact-info-icon">✉</div>
                    <div class="contact-info-text">
                        <h4 data-i18n="contact_inquiry_title">General Inquiry</h4>
                        <p data-i18n="contact_inquiry_val">info@nextgenhub.placeholder</p>
                    </div>
                </div>

                <div class="contact-info-item">
                    <div class="contact-info-icon">🏛</div>
                    <div class="contact-info-text">
                        <h4 data-i18n="contact_hq_title">Headquarters</h4>
                        <p data-i18n="contact_hq_val">Remote / Digital Operations</p>
                    </div>
                </div>

                <div>
                    <h4 style="margin-bottom: 12px; font-size: 1.1rem;" data-i18n="contact_follow">Follow Us</h4>
                    <div class="social-links">
                        <a href="https://www.linkedin.com/company/nextgen-datahub/" class="social-icon" aria-label="LinkedIn" target="_blank">in</a>
                        <a href="#" class="social-icon" aria-label="Facebook" target="_blank">fb</a>
                        <a href="#" class="social-icon" aria-label="Instagram" target="_blank">ig</a>
                        <a href="#" class="social-icon" aria-label="GitHub">git</a>
                    </div>
                </div>
            </div>

            <!-- Contact Form -->
            <div class="contact-form glass-panel">
                <form id="contactForm">
                    <div class="form-group">
                        <label for="name" class="form-label" data-i18n="contact_form_name">Full Name</label>
                        <input type="text" id="name" class="form-control" data-i18n-placeholder="contact_form_name" placeholder="Jane Doe" required>
                    </div>
                    
                    <div class="form-group">
                        <label for="email" class="form-label" data-i18n="contact_form_email">Email Address</label>
                        <input type="email" id="email" class="form-control" data-i18n-placeholder="contact_form_email" placeholder="jane@example.com" required>
                    </div>

                    <div class="form-group">
                        <label for="subject" class="form-label" data-i18n="contact_form_subject">Subject / Purpose</label>
                        <input type="text" id="subject" class="form-control" data-i18n-placeholder="contact_form_subject" placeholder="How can we help?" required>
                    </div>

                    <div class="form-group">
                        <label for="message" class="form-label" data-i18n="contact_form_message">Message</label>
                        <textarea id="message" class="form-control" data-i18n-placeholder="contact_form_message" placeholder="Tell us about your background or inquiry details..."></textarea>
                    </div>

                    <button type="submit" class="btn btn-primary" style="width: 100%;" id="submitBtn" data-i18n="contact_form_btn">Send Inquiry</button>
                </form>
            </div>

        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="container footer-grid">
            <div class="footer-brand">
                <a href="index.html" class="logo" style="margin-bottom: 16px;">
                    <span class="logo-icon">⚡</span>NextGen<span class="gradient-text">Hub</span>
                </a>
                <p data-i18n="footer_desc">Empowering creators, students, and engineers in data analytics and artificial intelligence. Shaping tomorrow, today.</p>
            </div>
            <div class="footer-nav">
                <h4 class="footer-nav-title" data-i18n="footer_links_title">Quick Links</h4>
                <a href="index.html" id="footerNavHome" data-i18n="nav_home">Home</a>
                <a href="internships.html" id="footerNavInternships" data-i18n="nav_internships">Internship Listings</a>
                <a href="bootcamps.html" id="footerNavBootcamps" data-i18n="nav_bootcamps">Summer Bootcamps</a>
                <a href="diplomas.html" id="footerNavDiplomas" data-i18n="nav_diplomas">Professional Diplomas</a>
            </div>
            <div class="footer-nav">
                <h4 class="footer-nav-title" data-i18n="footer_connect_title">Connect</h4>
                <a href="about.html" id="footerNavAbout" data-i18n="nav_about">About Us</a>
                <a href="contact.html" id="footerNavContact" data-i18n="nav_contact">Contact Support</a>
                <div class="social-links" style="margin-top: 16px;">
                    <a href="https://www.linkedin.com/company/nextgen-datahub/" class="social-icon" aria-label="LinkedIn" target="_blank">in</a>
                    <a href="#" class="social-icon" aria-label="Facebook" target="_blank">fb</a>
                    <a href="#" class="social-icon" aria-label="Instagram" target="_blank">ig</a>
                    <a href="#" class="social-icon" aria-label="GitHub">git</a>
                </div>
            </div>
        </div>
        <div class="container footer-bottom">
            <p data-i18n="footer_copyright">&copy; 2026 NextGen Hub. All rights reserved.</p>
            <p data-i18n="footer_design">Designed for professional excellence in AI & Analytics.</p>
        </div>
    </footer>

    <script src="main.js"></script>
    <script src="lang.js"></script>
    <script>
        // Check URL parameters on load to auto-fill forms
        document.addEventListener('DOMContentLoaded', () => {
            const urlParams = new URLSearchParams(window.location.search);
            const role = urlParams.get('role');
            const inquiry = urlParams.get('inquiry');
            const subjectField = document.getElementById('subject');
            const messageField = document.getElementById('message');

            if (subjectField) {
                if (role === 'AI_Research') {
                    subjectField.value = 'Application: AI Research Intern';
                    messageField.placeholder = 'Please tell us about your experience in NLP, PyTorch, or large language models...';
                    messageField.focus();
                } else if (role === 'Data_Analytics') {
                    subjectField.value = 'Application: Data Analytics Intern';
                    messageField.placeholder = 'Please tell us about your experience in SQL, PowerBI, Python, or spreadsheet metrics...';
                    messageField.focus();
                } else if (role === 'ML_Engineer') {
                    subjectField.value = 'Application: Machine Learning Engineer Intern';
                    messageField.placeholder = 'Please tell us about your experience in Docker, FastAPI, deep learning, or ONNX...';
                    messageField.focus();
                } else if (inquiry === 'Bootcamp_Registration') {
                    subjectField.value = 'Bootcamp Registration Inquiry';
                    messageField.placeholder = 'State your preferred track (Data Analytics or AI/ML) and any questions about registration...';
                    messageField.focus();
                } else if (inquiry === 'AI_Diploma') {
                    subjectField.value = 'Enrollment: Advanced AI & Deep Learning Diploma';
                    messageField.placeholder = 'Please tell us about your technical background and why you want to enroll in the AI Diploma...';
                    messageField.focus();
                } else if (inquiry === 'Data_Diploma') {
                    subjectField.value = 'Enrollment: Enterprise Data Analytics & Engineering Diploma';
                    messageField.placeholder = 'Please tell us about your analytical background and why you want to enroll in the Data Analytics Diploma...';
                    messageField.focus();
                }
            }
        });
    </script>
</body>
</html>
'''

# Write each translation-ready HTML page to disk
with open(os.path.join(html_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)
print("Updated index.html to translation-ready format")

with open(os.path.join(html_dir, "internships.html"), "w", encoding="utf-8") as f:
    f.write(internships_html)
print("Updated internships.html to translation-ready format")

with open(os.path.join(html_dir, "bootcamps.html"), "w", encoding="utf-8") as f:
    f.write(bootcamps_html)
print("Updated bootcamps.html to translation-ready format")

with open(os.path.join(html_dir, "diplomas.html"), "w", encoding="utf-8") as f:
    f.write(diplomas_html)
print("Updated diplomas.html to translation-ready format")

with open(os.path.join(html_dir, "about.html"), "w", encoding="utf-8") as f:
    f.write(about_html)
print("Updated about.html to translation-ready format")

with open(os.path.join(html_dir, "contact.html"), "w", encoding="utf-8") as f:
    f.write(contact_html)
print("Updated contact.html to translation-ready format")
