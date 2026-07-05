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
    const whatsappText = "Hello NextGen Hub, I am interested in your programs!";
    
    const waBtn = document.createElement('a');
    waBtn.href = `https://wa.me/${whatsappNumber}?text=${encodeURIComponent(whatsappText)}`;
    waBtn.target = "_blank";
    waBtn.className = "whatsapp-float";
    waBtn.setAttribute('aria-label', 'Chat on WhatsApp');
    waBtn.innerHTML = `
        <svg viewBox="0 0 24 24" width="30" height="30" fill="currentColor">
            <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946C.003 5.372 5.378 0 12.026 0c3.221.001 6.248 1.254 8.527 3.535 2.279 2.281 3.53 5.309 3.53 8.532-.003 6.655-5.379 12.028-12.028 12.028-1.997-.001-3.957-.5-5.697-1.448L0 24zm6.59-4.846c1.6.95 3.188 1.449 4.825 1.451 5.436 0 9.86-4.42 9.863-9.864.001-2.63-1.023-5.101-2.884-6.963C16.58 1.916 14.105 1.01 11.5 1.01 6.064 1.01 1.642 5.432 1.639 10.876c-.001 1.706.469 3.313 1.36 4.754L1.932 20.3l4.715-1.146zm11.367-7.251c-.33-.164-1.951-.964-2.251-1.074-.3-.109-.518-.164-.718.136-.2.3-.771.964-.944 1.164-.173.199-.347.223-.677.059-.33-.164-1.393-.513-2.653-1.637-1.01-.901-1.691-2.013-1.889-2.342-.198-.33-.021-.508.143-.671.147-.146.33-.382.495-.573.164-.189.219-.327.327-.545.109-.219.055-.409-.027-.573-.082-.164-.718-1.727-.982-2.36-.258-.62-.519-.536-.718-.546-.188-.01-.403-.012-.618-.012-.215 0-.565.081-.861.409-.296.327-1.13 1.105-1.13 2.694 0 1.589 1.155 3.123 1.315 3.342.16.218 2.271 3.468 5.503 4.869.768.332 1.367.53 1.834.679.772.245 1.473.21 2.029.128.619-.092 1.951-.797 2.227-1.567.277-.769.277-1.43.196-1.567-.082-.136-.3-.218-.63-.382z"/>
        </svg>
    `;
    document.body.appendChild(waBtn);
});
