// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Intersection Observer for fade-in animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Add fade-in animation to elements
document.addEventListener('DOMContentLoaded', () => {
    // Elements to animate
    const animatedElements = document.querySelectorAll(
        '.feature-card, .tech-item, .screenshot-item, .floating-card'
    );
    
    animatedElements.forEach((el, index) => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = `all 0.6s ease ${index * 0.1}s`;
        observer.observe(el);
    });
});

// QR Code interaction
document.addEventListener('DOMContentLoaded', () => {
    const qrCodes = document.querySelectorAll('.qr-code, .qr-code-large');
    
    qrCodes.forEach(qr => {
        qr.addEventListener('click', () => {
            // Add a pulse animation
            qr.style.transform = 'scale(1.05)';
            setTimeout(() => {
                qr.style.transform = 'scale(1)';
            }, 200);
            
            // Show tooltip
            showTooltip(qr, 'Point your camera at the QR code to download!');
        });
    });
});

// Tooltip function
function showTooltip(element, message) {
    const tooltip = document.createElement('div');
    tooltip.className = 'tooltip';
    tooltip.textContent = message;
    tooltip.style.cssText = `
        position: absolute;
        bottom: 100%;
        left: 50%;
        transform: translateX(-50%);
        background: #1a1a1a;
        color: white;
        padding: 8px 12px;
        border-radius: 8px;
        font-size: 0.9rem;
        white-space: nowrap;
        z-index: 1000;
        margin-bottom: 10px;
        opacity: 0;
        transition: opacity 0.3s ease;
    `;
    
    element.style.position = 'relative';
    element.appendChild(tooltip);
    
    // Trigger fade in
    setTimeout(() => tooltip.style.opacity = '1', 10);
    
    // Remove tooltip after 3 seconds
    setTimeout(() => {
        tooltip.style.opacity = '0';
        setTimeout(() => {
            if (tooltip.parentNode) {
                tooltip.parentNode.removeChild(tooltip);
            }
        }, 300);
    }, 3000);
}

// Download button analytics (placeholder)
document.addEventListener('DOMContentLoaded', () => {
    const downloadButtons = document.querySelectorAll('a[href="/download"]');
    
    downloadButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            // Track download attempt
            console.log('Download initiated:', new Date().toISOString());
            
            // Add visual feedback
            const originalText = button.innerHTML;
            button.innerHTML = '<span class="btn-icon">⬇️</span>Downloading...';
            button.style.opacity = '0.7';
            
            setTimeout(() => {
                button.innerHTML = originalText;
                button.style.opacity = '1';
            }, 2000);
        });
    });
});

// Parallax effect for hero section
document.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    const hero = document.querySelector('.hero');
    const heroHeight = hero.offsetHeight;
    
    if (scrolled < heroHeight) {
        const rate = scrolled * -0.5;
        hero.style.transform = `translate3d(0, ${rate}px, 0)`;
    }
});

// Mobile menu toggle (if needed in future)
function toggleMobileMenu() {
    const menu = document.querySelector('.mobile-menu');
    if (menu) {
        menu.classList.toggle('active');
    }
}

// Performance optimization: Throttle scroll events
function throttle(func, wait, immediate) {
    let timeout;
    return function executedFunction() {
        const context = this;
        const args = arguments;
        const later = function() {
            timeout = null;
            if (!immediate) func.apply(context, args);
        };
        const callNow = immediate && !timeout;
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
        if (callNow) func.apply(context, args);
    };
}

// Optimized scroll handler
const optimizedScrollHandler = throttle(() => {
    const scrolled = window.pageYOffset;
    const hero = document.querySelector('.hero');
    const heroHeight = hero.offsetHeight;
    
    if (scrolled < heroHeight) {
        const rate = scrolled * -0.5;
        hero.style.transform = `translate3d(0, ${rate}px, 0)`;
    }
}, 16); // ~60fps

document.addEventListener('scroll', optimizedScrollHandler);

// Add loading animation for images
document.addEventListener('DOMContentLoaded', () => {
    const images = document.querySelectorAll('img');
    
    images.forEach(img => {
        img.addEventListener('load', function() {
            this.style.opacity = '1';
            this.style.transition = 'opacity 0.3s ease';
        });
        
        // Set initial state
        img.style.opacity = '0';
        
        // If image is already loaded (cached)
        if (img.complete) {
            img.style.opacity = '1';
        }
    });
});
