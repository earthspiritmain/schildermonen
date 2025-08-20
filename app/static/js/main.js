// Placeholder for future JS (e.g., mobile nav, accessibility) 

// Mobile Menu Toggle
document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const mobileNav = document.querySelector('.mobile-nav');
    
    if (mobileMenuToggle && mobileNav) {
        mobileMenuToggle.addEventListener('click', function() {
            // Toggle the active class for animation
            mobileMenuToggle.classList.toggle('active');
            mobileNav.classList.toggle('active');
            
            // Prevent body scroll when menu is open
            document.body.style.overflow = mobileNav.classList.contains('active') ? 'hidden' : '';
        });
        
        // Close mobile menu when clicking on links
        const mobileNavLinks = mobileNav.querySelectorAll('a');
        mobileNavLinks.forEach(link => {
            link.addEventListener('click', function() {
                mobileMenuToggle.classList.remove('active');
                mobileNav.classList.remove('active');
                document.body.style.overflow = '';
            });
        });
    }
    
    // Smooth scrolling for internal links
    const internalLinks = document.querySelectorAll('a[href^="#"]');
    internalLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                const headerHeight = document.querySelector('.hero-nav').offsetHeight;
                const targetPosition = targetElement.offsetTop - headerHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Add scroll effect to navigation
    let lastScrollTop = 0;
    const heroNav = document.querySelector('.hero-nav');
    
    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        // Add background opacity based on scroll
        if (scrollTop > 50) {
            heroNav.style.background = 'rgba(0, 0, 0, 0.9)';
        } else {
            heroNav.style.background = 'rgba(0, 0, 0, 0.7)';
        }
        
        lastScrollTop = scrollTop;
    });
    
    // Service Cards Animation
    const serviceObserverOptions = {
        threshold: 0.2,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const serviceCardsObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting && !entry.target.classList.contains('animate')) {
                entry.target.classList.add('animate');
            }
        });
    }, serviceObserverOptions);
    
    // Observe all service cards
    const serviceCards = document.querySelectorAll('.service-card');
    serviceCards.forEach(card => {
        // Initially hide cards for animation
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        serviceCardsObserver.observe(card);
    });
    
    // Animate metrics on scroll
    const observerOptions = {
        threshold: 0.5,
        rootMargin: '0px 0px -100px 0px'
    };
    
    const metricsObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const numbers = entry.target.querySelectorAll('.metric__number');
                numbers.forEach(number => {
                    const finalValue = number.textContent;
                    const numValue = parseInt(finalValue.replace(/\D/g, ''));
                    
                    if (numValue && !number.classList.contains('animated')) {
                        number.classList.add('animated');
                        animateNumber(number, numValue, finalValue.includes('+') ? '+' : '');
                    }
                });
            }
        });
    }, observerOptions);
    
    const metricsStrip = document.querySelector('.metrics-strip');
    if (metricsStrip) {
        metricsObserver.observe(metricsStrip);
    }
    
    // Number animation function
    function animateNumber(element, target, suffix = '') {
        let current = 0;
        const increment = target / 30;
        const timer = setInterval(() => {
            current += increment;
            element.textContent = Math.floor(current) + suffix;
            
            if (current >= target) {
                element.textContent = target + suffix;
                clearInterval(timer);
            }
        }, 50);
    }
    
    // Before/After Slider Functionality
    const beforeAfterSliders = document.querySelectorAll('.slider');
    
    beforeAfterSliders.forEach(slider => {
        const parentContainer = slider.closest('.comparison-container');
        if (!parentContainer) return;
        
        const afterImageContainer = parentContainer.querySelector('.after-image-container');
        const sliderButton = parentContainer.querySelector('.slider-button');
        
        function updateComparison(value) {
            const percentage = value;
            
            // Update the clip-path of the after image
            if (afterImageContainer) {
                afterImageContainer.style.clipPath = `polygon(${percentage}% 0%, 100% 0%, 100% 100%, ${percentage}% 100%)`;
            }
            
            // Update slider button position
            if (sliderButton) {
                sliderButton.style.left = `${percentage}%`;
            }
        }
        
        // Initialize the comparison at 50%
        updateComparison(50);
        
        // Handle slider input events
        slider.addEventListener('input', function() {
            updateComparison(this.value);
        });
        
        // Handle mouse events for better UX
        slider.addEventListener('mousedown', function() {
            if (sliderButton) {
                sliderButton.style.transform = 'translate(-50%, -50%) scale(1.1)';
            }
        });
        
        slider.addEventListener('mouseup', function() {
            if (sliderButton) {
                sliderButton.style.transform = 'translate(-50%, -50%) scale(1)';
            }
        });
        
        // Handle touch events for mobile
        slider.addEventListener('touchstart', function() {
            if (sliderButton) {
                sliderButton.style.transform = 'translate(-50%, -50%) scale(1.1)';
            }
        });
        
        slider.addEventListener('touchend', function() {
            if (sliderButton) {
                sliderButton.style.transform = 'translate(-50%, -50%) scale(1)';
            }
        });
    });
    
    // Animate before/after sections on scroll
    const beforeAfterObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting && !entry.target.classList.contains('animate')) {
                entry.target.classList.add('animate');
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, {
        threshold: 0.2,
        rootMargin: '0px 0px -50px 0px'
    });
    
    // Observe before/after items
    const beforeAfterItems = document.querySelectorAll('.before-after__item');
    beforeAfterItems.forEach(item => {
        // Initially hide items for animation
        item.style.opacity = '0';
        item.style.transform = 'translateY(30px)';
        item.style.transition = 'all 0.6s ease-out';
        beforeAfterObserver.observe(item);
    });
});

// Handle window resize for mobile menu
window.addEventListener('resize', function() {
    if (window.innerWidth > 768) {
        const mobileNav = document.querySelector('.mobile-nav');
        const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
        
        if (mobileNav && mobileMenuToggle) {
            mobileNav.classList.remove('active');
            mobileMenuToggle.classList.remove('active');
            document.body.style.overflow = '';
        }
    }
}); 