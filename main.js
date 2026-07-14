// Instant theme application to prevent light-theme flash
if (localStorage.getItem('selectedTheme') === 'dark') {
    document.documentElement.classList.add('dark-theme');
    document.body.classList.add('dark-theme');
}
document.addEventListener('DOMContentLoaded', () => {
    // --- Header Scroll Effect ---
    const header = document.querySelector('header');
    const handleScroll = () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    };
    window.addEventListener('scroll', handleScroll);
    handleScroll(); // Initial check in case of page refresh on scrolled position

    // --- Mobile Menu Toggle ---
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', () => {
            navToggle.classList.toggle('active');
            navMenu.classList.toggle('active');
        });

        // Close menu when clicking a link
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                navToggle.classList.remove('active');
                navMenu.classList.remove('active');
            });
        });
    }

    // --- Contact Form Submission Handler & Toast ---
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            // Get values
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const subject = document.getElementById('subject').value;
            const message = document.getElementById('message').value;

            if (name && email && subject && message) {
                showToast(`Thank you, ${name}! Your inquiry has been sent successfully.`, 'success');
                contactForm.reset();
            } else {
                showToast('Please fill out all fields before submitting.', 'error');
            }
        });
    }

    // Toast Functionality
    function showToast(message, type = 'success') {
        // Remove existing toast if any
        const existingToast = document.querySelector('.toast');
        if (existingToast) {
            existingToast.remove();
        }

        // Create toast element
        const toast = document.createElement('div');
        toast.className = `toast ${type === 'success' ? 'toast-success' : ''}`;
        
        // Add content
        toast.innerHTML = `
            <div class="toast-icon">${type === 'success' ? '✓' : '✗'}</div>
            <div class="toast-message">${message}</div>
        `;

        document.body.appendChild(toast);

        // Animate in
        setTimeout(() => {
            toast.classList.add('show');
        }, 100);

        // Animate out and remove
        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => {
                toast.remove();
            }, 400);
        }, 4000);
    }

    // --- Slideshow / Carousel Functionality ---
    const slideTrack = document.getElementById('slideTrack');
    const slides = document.querySelectorAll('.slide');
    const prevBtn = document.getElementById('prevSlide');
    const nextBtn = document.getElementById('nextSlide');
    const dots = document.querySelectorAll('.dot');
    
    if (slideTrack && slides.length > 0) {
        let currentSlide = 0;
        const totalSlides = slides.length;
        let autoSlideInterval;
        
        const updateSlidePosition = () => {
            slideTrack.style.transform = `translateX(-${currentSlide * 100}%)`;
            
            // Update active dot
            dots.forEach((dot, index) => {
                if (index === currentSlide) {
                    dot.classList.add('active');
                } else {
                    dot.classList.remove('active');
                }
            });
        };
        
        const nextSlide = () => {
            currentSlide = (currentSlide + 1) % totalSlides;
            updateSlidePosition();
        };
        
        const prevSlide = () => {
            currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
            updateSlidePosition();
        };
        
        // Event Listeners
        if (nextBtn) {
            nextBtn.addEventListener('click', () => {
                nextSlide();
                resetAutoSlide();
            });
        }
        
        if (prevBtn) {
            prevBtn.addEventListener('click', () => {
                prevSlide();
                resetAutoSlide();
            });
        }
        
        dots.forEach(dot => {
            dot.addEventListener('click', (e) => {
                currentSlide = parseInt(e.target.getAttribute('data-index'));
                updateSlidePosition();
                resetAutoSlide();
            });
        });
        
        // Auto Slide
        const startAutoSlide = () => {
            autoSlideInterval = setInterval(nextSlide, 5000); // Change slide every 5 seconds
        };
        
        const resetAutoSlide = () => {
            clearInterval(autoSlideInterval);
            startAutoSlide();
        };
        
        startAutoSlide();
    }

    // --- Hero Image Slider ---
    const heroSlidesWrapper = document.getElementById('heroSlidesWrapper');
    const heroDots = document.querySelectorAll('.hero-dot');
    if (heroSlidesWrapper && heroDots.length > 0) {
        let currentHeroSlide = 0;
        let heroSlideInterval;
        
        const updateHeroSlidePosition = () => {
            const isRtl = document.body.classList.contains('rtl');
            const shiftPercent = currentHeroSlide * 33.333;
            // In LTR we translate left (negative), in RTL we translate right (positive)
            const directionMultiplier = isRtl ? 1 : -1;
            heroSlidesWrapper.style.transform = `translateX(${directionMultiplier * shiftPercent}%)`;
            
            // Update active dot indicator
            heroDots.forEach((dot, index) => {
                if (index === currentHeroSlide) {
                    dot.classList.add('active');
                } else {
                    dot.classList.remove('active');
                }
            });
        };
        
        const nextHeroSlide = () => {
            currentHeroSlide = (currentHeroSlide + 1) % heroDots.length;
            updateHeroSlidePosition();
        };
        
        const startHeroAutoSlide = () => {
            heroSlideInterval = setInterval(nextHeroSlide, 4000); // Change slide every 4 seconds
        };
        
        const resetHeroAutoSlide = () => {
            clearInterval(heroSlideInterval);
            startHeroAutoSlide();
        };
        
        heroDots.forEach(dot => {
            dot.addEventListener('click', (e) => {
                currentHeroSlide = parseInt(e.target.getAttribute('data-slide'));
                updateHeroSlidePosition();
                resetHeroAutoSlide();
            });
        });
        
        startHeroAutoSlide();
    }


    // --- WhatsApp Floating Button Injection ---
    const whatsappNumber = "201206751361";
    const whatsappText = "Hello NextGen Institute, I am interested in your programs!";
    
    const waBtn = document.createElement('a');
    waBtn.href = `https://wa.me/${whatsappNumber}?text=${encodeURIComponent(whatsappText)}`;
    waBtn.target = "_blank";
    waBtn.className = "whatsapp-float";
    waBtn.setAttribute('aria-label', 'Chat on WhatsApp');
    waBtn.innerHTML = `
        <svg viewBox="0 0 24 24" width="34" height="34" fill="currentColor">
            <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946C.06 5.348 5.397.01 12.008.01c3.202.001 6.212 1.246 8.477 3.513 2.262 2.268 3.507 5.28 3.505 8.484-.004 6.657-5.34 11.997-11.953 11.997-2.005-.001-3.973-.502-5.724-1.455L0 24zm6.59-4.846c1.66.986 3.284 1.489 4.936 1.49h.005c5.378 0 9.75-4.37 9.755-9.755a9.66 9.66 0 0 0-2.845-6.894 9.66 9.66 0 0 0-6.893-2.847c-5.383 0-9.754 4.373-9.759 9.756-.002 2.222.746 4.337 2.16 6.07l-.962 3.514 3.608-.944zm8.002-1.438c-.3-.15-1.78-.877-2.056-.977-.276-.1-.478-.15-.678.15-.2.3-.778.977-.954 1.177-.176.2-.351.226-.651.076-.3-.15-1.265-.467-2.41-1.485-.89-.794-1.492-1.775-1.667-2.076-.175-.3-.019-.462.13-.611.135-.135.3-.35.45-.525.15-.175.2-.3.3-.5.1-.2.05-.375-.025-.525-.075-.15-.678-1.635-.93-2.244-.244-.589-.493-.509-.678-.509-.176 0-.376-.02-.577-.02-.2 0-.527.075-.803.376-.276.3-1.053 1.026-1.053 2.503 0 1.477 1.078 2.902 1.228 3.102.15.2 2.122 3.24 5.143 4.545.718.311 1.277.496 1.714.635.722.23 1.38.197 1.9.12.577-.087 1.78-.727 2.03-1.43.25-.701.25-1.302.176-1.43-.076-.127-.276-.202-.577-.352z"/>
        </svg>
    `;
    document.body.appendChild(waBtn);
    // --- Dark Mode Switcher ---
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

});


// --- UI Redesign Logic ---

document.addEventListener('DOMContentLoaded', () => {
    // 1. Intersection Observer for fade-up elements
    const fadeElements = document.querySelectorAll('.fade-up');
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };
    
    const fadeObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    fadeElements.forEach(el => fadeObserver.observe(el));
    
    // 2. Scroll Progress and Back to Top
    const scrollProgress = document.getElementById('scrollProgress');
    const backToTop = document.getElementById('backToTop');
    
    window.addEventListener('scroll', () => {
        // Progress bar
        const totalHeight = document.body.scrollHeight - window.innerHeight;
        const progress = (window.scrollY / totalHeight) * 100;
        if (scrollProgress) {
            scrollProgress.style.width = progress + '%';
        }
        
        // Back to top visibility
        if (window.scrollY > 400) {
            if (backToTop) backToTop.classList.add('visible');
        } else {
            if (backToTop) backToTop.classList.remove('visible');
        }
    });
    
    if (backToTop) {
        backToTop.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }
});
