document.addEventListener('DOMContentLoaded', function() {
    // Make sure carousel navigation is working properly
    const carousel = document.getElementById('heroCarousel');
    if (carousel) {
        const carouselInstance = new bootstrap.Carousel(carousel, {
            interval: 2000,
            wrap: true,
            touch: true
        });
        
        // Ensure navigation buttons work correctly
        const prevButton = document.querySelector('.carousel-control-prev');
        const nextButton = document.querySelector('.carousel-control-next');
        
        if (prevButton && nextButton) {
            prevButton.addEventListener('click', function(e) {
                e.preventDefault();
                carouselInstance.prev();
            });
            
            nextButton.addEventListener('click', function(e) {
                e.preventDefault();
                carouselInstance.next();
            });
        }
    }
    
    // Product quantity buttons
    const quantityInputs = document.querySelectorAll('.quantity-input');
    if (quantityInputs) {
        quantityInputs.forEach(input => {
            const minusBtn = input.previousElementSibling;
            const plusBtn = input.nextElementSibling;
            
            if (minusBtn && plusBtn) {
                minusBtn.addEventListener('click', () => {
                    if (input.value > 1) {
                        input.value = parseInt(input.value) - 1;
                        // Trigger change event for form updates
                        const event = new Event('change');
                        input.dispatchEvent(event);
                    }
                });
                
                plusBtn.addEventListener('click', () => {
                    input.value = parseInt(input.value) + 1;
                    // Trigger change event for form updates
                    const event = new Event('change');
                    input.dispatchEvent(event);
                });
            }
        });
    }
    
    // Product image gallery
    const mainImage = document.getElementById('product-main-image');
    const thumbnails = document.querySelectorAll('.product-thumbnail');
    
    if (mainImage && thumbnails.length > 0) {
        thumbnails.forEach(thumb => {
            thumb.addEventListener('click', () => {
                // Update main image
                mainImage.src = thumb.src;
                
                // Update active thumbnail
                thumbnails.forEach(t => t.classList.remove('active'));
                thumb.classList.add('active');
            });
        });
    }
    
    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    if (alerts) {
        alerts.forEach(alert => {
            setTimeout(() => {
                const bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            }, 5000);
        });
    }
    
    // Tooltip initialization
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Animate elements when they come into view
    const animatedElements = document.querySelectorAll('.animate-on-scroll');
    if (animatedElements.length > 0) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-fade-in');
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.1
        });
        
        animatedElements.forEach(el => {
            observer.observe(el);
        });
    }
    
    // Add to cart button animation - prevent event bubbling to card link
    const addToCartButtons = document.querySelectorAll('.product-card .btn-primary');
    if (addToCartButtons) {
        addToCartButtons.forEach(button => {
            button.addEventListener('click', function(e) {
                // Stop event propagation to prevent triggering the card link
                e.stopPropagation();
                
                // Prevent immediate redirect if it's a link
                if (this.tagName === 'A') {
                    e.preventDefault();
                }
                
                // Add animation class
                this.classList.add('added-to-cart');
                
                // Change icon to checkmark
                const icon = this.querySelector('i');
                if (icon) {
                    icon.classList.remove('fa-cart-plus');
                    icon.classList.add('fa-check');
                }
                
                // Change text if there's space
                if (this.textContent.includes('Add')) {
                    this.innerHTML = '<i class="fas fa-check"></i> Added';
                }
                
                // Wait and redirect if it's a link
                if (this.tagName === 'A') {
                    const href = this.getAttribute('href');
                    setTimeout(() => {
                        window.location.href = href;
                    }, 800);
                }
            });
        });
    }
    
    // Prevent the footer buttons from triggering the card click
    document.querySelectorAll('.product-card .card-footer').forEach(footer => {
        footer.addEventListener('click', e => {
            e.stopPropagation();
        });
    });
    
    // Make the whole product card clickable
    document.querySelectorAll('.product-card').forEach(card => {
        card.addEventListener('click', e => {
            const link = card.querySelector('.product-card-link');
            if (link && link.href) {
                window.location.href = link.href;
            }
        });
    });
    
    // Category cards hover animations
    const categoryCards = document.querySelectorAll('.category-card');
    if (categoryCards) {
        categoryCards.forEach(card => {
            // Create an animated icon for each category
            const cardBody = card.querySelector('.card-body');
            const cardTitle = card.querySelector('.card-title');
            
            if (cardBody && cardTitle) {
                const categoryName = cardTitle.textContent.trim().toLowerCase();
                let iconClass = 'fa-leaf'; // Default icon
                
                // Select appropriate icon based on category name
                if (categoryName.includes('protein')) {
                    iconClass = 'fa-dumbbell';
                } else if (categoryName.includes('vitamin')) {
                    iconClass = 'fa-pills';
                } else if (categoryName.includes('pre-workout')) {
                    iconClass = 'fa-bolt';
                } else if (categoryName.includes('weight') || categoryName.includes('management')) {
                    iconClass = 'fa-weight-scale';
                }
                
                // Create and append icon element
                const iconElement = document.createElement('div');
                iconElement.className = 'category-icon';
                iconElement.innerHTML = `<i class="fas ${iconClass}"></i>`;
                iconElement.style.cssText = `
                    position: absolute;
                    top: -30px;
                    right: 20px;
                    width: 50px;
                    height: 50px;
                    background: linear-gradient(135deg, #2196F3, #4CAF50);
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    color: white;
                    opacity: 0;
                    transform: translateY(20px);
                    transition: all 0.3s ease;
                    z-index: 1;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.15);
                `;
                
                cardBody.style.position = 'relative';
                cardBody.prepend(iconElement);
                
                // Show icon on hover
                card.addEventListener('mouseenter', () => {
                    iconElement.style.opacity = '1';
                    iconElement.style.transform = 'translateY(0)';
                });
                
                card.addEventListener('mouseleave', () => {
                    iconElement.style.opacity = '0';
                    iconElement.style.transform = 'translateY(20px)';
                });
            }
        });
    }
    
    // Add rating stars to products
    const productCards = document.querySelectorAll('.product-card-link');
    if (productCards) {
        productCards.forEach(cardLink => {
            const cardBody = cardLink.querySelector('.card-body');
            if (cardBody) {
                const ratingContainer = document.createElement('div');
                ratingContainer.className = 'star-rating';
                
                // Generate random rating between 4 and 5 stars
                const rating = (4 + Math.random()).toFixed(1);
                const fullStars = Math.floor(rating);
                const hasHalfStar = rating % 1 >= 0.5;
                
                // Create star HTML
                let starsHtml = '';
                for (let i = 0; i < 5; i++) {
                    if (i < fullStars) {
                        starsHtml += '<i class="fas fa-star"></i>';
                    } else if (i === fullStars && hasHalfStar) {
                        starsHtml += '<i class="fas fa-star-half-alt"></i>';
                    } else {
                        starsHtml += '<i class="far fa-star"></i>';
                    }
                }
                starsHtml += ` <small class="text-muted">(${(Math.floor(Math.random() * 100) + 10)})</small>`;
                
                ratingContainer.innerHTML = starsHtml;
                
                // Insert after product description
                const description = cardBody.querySelector('.card-text:not(.small):not(.text-muted)');
                if (description) {
                    description.after(ratingContainer);
                }
            }
        });
    }
    
    // Add trust message to newsletter
    const newsletterForm = document.querySelector('.newsletter-section form');
    if (newsletterForm) {
        const trustMessage = document.createElement('div');
        trustMessage.className = 'trust-message';
        trustMessage.innerHTML = '<i class="fas fa-shield-alt me-1"></i> No spam. Only tips & deals you\'ll love.';
        newsletterForm.appendChild(trustMessage);
    }
    
    // Add smooth scroll effect
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if (targetId !== '#' && document.querySelector(targetId)) {
                e.preventDefault();
                document.querySelector(targetId).scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Add subtle parallax effect to hero image on scroll
    const heroSection = document.querySelector('.hero-section');
    if (heroSection) {
        window.addEventListener('scroll', () => {
            const scrollY = window.scrollY;
            const heroImages = heroSection.querySelectorAll('.carousel-item img');
            
            heroImages.forEach(img => {
                // Move the background slightly based on scroll position
                img.style.transform = `translateY(${scrollY * 0.2}px)`;
            });
        });
    }
    
    // Add subtle animation to benefit icons
    const benefitIcons = document.querySelectorAll('.benefit-icon');
    if (benefitIcons.length > 0) {
        benefitIcons.forEach((icon, index) => {
            // Add slight delay to each icon for staggered animation
            setTimeout(() => {
                icon.style.animation = 'fadeInUp 0.6s ease-out forwards';
            }, index * 150);
        });
    }
}); 