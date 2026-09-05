// Force light theme and clean up old theme settings
localStorage.setItem('selectedTheme', 'light');
document.documentElement.classList.remove('dark-theme');
document.body.classList.remove('dark-theme');
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
            
            const submitBtn = document.getElementById('submitBtn');
            const name = document.getElementById('name') ? document.getElementById('name').value.trim() : '';
            const email = document.getElementById('email') ? document.getElementById('email').value.trim() : '';
            const subject = document.getElementById('subject') ? document.getElementById('subject').value.trim() : '';
            const message = document.getElementById('message') ? document.getElementById('message').value.trim() : '';
            const currentLang = localStorage.getItem('selectedLang') || 'en';

            if (!name || !email || !subject || !message) {
                showToast(currentLang === 'ar' ? 'يرجى ملء جميع الحقول المطلوبة.' : 'Please fill out all fields before submitting.', 'error');
                return;
            }

            const origText = submitBtn ? submitBtn.innerText : '';
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerText = currentLang === 'ar' ? 'جاري الإرسال...' : 'Sending...';
            }

            fetch('https://formsubmit.co/ajax/nextgeninstitute.careers@gmail.com', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({
                    name: name,
                    email: email,
                    subject: subject,
                    message: message,
                    _subject: `New Inquiry from ${name}: ${subject}`,
                    _template: 'table',
                    _captcha: 'false'
                })
            })
            .then(res => res.json())
            .then(data => {
                if (submitBtn) {
                    submitBtn.disabled = false;
                    submitBtn.innerText = origText;
                }
                if (data.success === "true" || data.success === true) {
                    const successMsg = currentLang === 'ar' 
                        ? `شكراً لك يا ${name}! تم إرسال رسالتك بنجاح وسنتواصل معك قريباً.`
                        : `Thank you, ${name}! Your inquiry has been sent successfully.`;
                    showToast(successMsg, 'success');
                    contactForm.reset();
                } else if (data.message && data.message.includes('Activation')) {
                    const warnMsg = currentLang === 'ar'
                        ? 'تنبيه: يرجى فتح الإيميل nextgeninstitute.careers@gmail.com والضغط على رابط التفعيل (Activate Form) لمرة واحدة.'
                        : 'Form needs activation! Please check nextgeninstitute.careers@gmail.com inbox to activate.';
                    showToast(warnMsg, 'error');
                } else {
                    const errorMsg = currentLang === 'ar'
                        ? 'حدث خطأ أثناء الإرسال، يرجى المحاولة لاحقاً.'
                        : 'An error occurred while sending. Please try again.';
                    showToast(errorMsg, 'error');
                }
            })
            .catch(() => {
                if (submitBtn) {
                    submitBtn.disabled = false;
                    submitBtn.innerText = origText;
                }
                const errorMsg = currentLang === 'ar' 
                    ? 'حدث خطأ أثناء الإرسال، يرجى المحاولة لاحقاً.'
                    : 'An error occurred while sending. Please try again.';
                showToast(errorMsg, 'error');
            });
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



    // --- Explore Programs Modal Controller ---
    const exploreCta = document.getElementById('heroCtaPrimary');
    const ctaFooter = document.getElementById('ctaFooter');
    const exploreModal = document.getElementById('exploreModal');
    const closeExploreModal = document.getElementById('closeExploreModal');
    
    if (exploreModal) {
        const openModal = (e) => {
            e.preventDefault(); // Stop normal redirection
            exploreModal.classList.add('show');
            document.body.style.overflow = 'hidden'; // Disable background scrolling
        };

        if (exploreCta) {
            exploreCta.addEventListener('click', openModal);
        }

        if (ctaFooter) {
            ctaFooter.addEventListener('click', openModal);
        }
        
        const closeModal = () => {
            exploreModal.classList.remove('show');
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
