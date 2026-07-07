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
        <svg viewBox="0 0 24 24" width="32" height="32" fill="none">
            <path fill="white" d="M12.03 2c-5.52 0-10 4.48-10 10 0 1.78.47 3.5 1.35 5L2 22l5.12-1.34c1.46.8 3.12 1.22 4.82 1.22 5.52 0 10-4.48 10-10 0-5.52-4.48-10-10-10z"/>
            <path fill="var(--wa-bg)" d="M17.98 16.18c-.27-.13-1.58-.78-1.82-.87-.24-.09-.42-.13-.6.13-.18.27-.7 1.13-.86 1.3-.16.18-.33.2-.6.07-.27-.13-1.15-.43-2.2-1.36-.81-.72-1.36-1.62-1.52-1.9-.16-.27-.02-.42.12-.55.12-.13.27-.3.4-.46.13-.16.18-.28.27-.46.09-.18.04-.34-.02-.47-.07-.13-.6-1.44-.82-1.97-.22-.53-.48-.46-.6-.46-.12 0-.27-.02-.42-.02-.15 0-.39.06-.6.28-.21.22-.8.78-.8 1.9s.82 2.2 1.04 2.5c.22.3 1.62 2.48 3.93 3.48.55.24.98.38 1.32.49.56.18 1.07.15 1.47.09.45-.07 1.38-.56 1.57-1.1.2-.55.2-1.02.14-1.13-.06-.11-.24-.17-.51-.3z"/>
        </svg>
    `;
    document.body.appendChild(waBtn);
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
