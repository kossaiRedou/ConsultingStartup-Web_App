/**
 * GABITHEX - Script d'Optimisation de Conversion
 * Fonctionnalités d'amélioration de l'expérience utilisateur et de la conversion
 */

document.addEventListener('DOMContentLoaded', function() {
    
    // 1. Tracking des interactions pour analytics
    function trackConversionEvent(action, label) {
        if (typeof gtag !== 'undefined') {
            gtag('event', action, {
                'event_category': 'Conversion',
                'event_label': label,
                'value': 1
            });
        }
        console.log(`Conversion Event: ${action} - ${label}`);
    }

    // 2. Animation des statistiques au scroll
    function animateStats() {
        const stats = document.querySelectorAll('.stat-item h3');
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const target = entry.target;
                    const text = target.textContent;
                    const number = parseInt(text);
                    if (!isNaN(number)) {
                        animateNumber(target, number, text);
                        observer.unobserve(target);
                    }
                }
            });
        });
        
        stats.forEach(stat => observer.observe(stat));
    }

    function animateNumber(element, finalValue, originalText) {
        let currentValue = 0;
        const increment = finalValue / 30;
        const suffix = originalText.replace(finalValue.toString(), '');
        
        const timer = setInterval(() => {
            currentValue += increment;
            if (currentValue >= finalValue) {
                element.textContent = finalValue + suffix;
                clearInterval(timer);
            } else {
                element.textContent = Math.floor(currentValue) + suffix;
            }
        }, 50);
    }

    // 3. Optimisation du formulaire de contact
    function optimizeContactForm() {
        const form = document.querySelector('.php-email-form');
        const submitBtn = document.querySelector('button[type="submit"]');
        const urgentCheckbox = document.getElementById('urgentCheck');
        
        if (form) {
            // Validation en temps réel
            const inputs = form.querySelectorAll('input, textarea, select');
            inputs.forEach(input => {
                input.addEventListener('blur', function() {
                    validateField(this);
                });
                
                input.addEventListener('input', function() {
                    if (this.classList.contains('is-invalid')) {
                        validateField(this);
                    }
                });
            });
            
            // Gestion de l'urgence
            if (urgentCheckbox && submitBtn) {
                urgentCheckbox.addEventListener('change', function() {
                    if (this.checked) {
                        submitBtn.classList.add('pulse');
                        submitBtn.innerHTML = '<i class="bi bi-send"></i> 🚨 Envoyer en Priorité';
                        trackConversionEvent('urgent_project_selected', 'contact_form');
                    } else {
                        submitBtn.classList.remove('pulse');
                        submitBtn.innerHTML = '<i class="bi bi-send"></i> Envoyer & Recevoir Mon Devis Gratuit';
                    }
                });
            }
            
            // Soumission du formulaire avec analytics
            form.addEventListener('submit', function(e) {
                const projectType = document.getElementById('subject-field').value;
                trackConversionEvent('form_submitted', projectType || 'unknown');
                
                // Animation de soumission
                if (submitBtn) {
                    submitBtn.innerHTML = '<span class="loading-spinner"></span> Envoi en cours...';
                    submitBtn.disabled = true;
                }
            });
        }
    }

    // 4. Fonction de validation des champs
    function validateField(field) {
        const value = field.value.trim();
        let isValid = true;
        let errorMessage = '';
        
        // Validation par type de champ
        switch (field.type) {
            case 'email':
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                isValid = emailRegex.test(value);
                errorMessage = 'Veuillez entrer une adresse email valide';
                break;
                
            case 'text':
                isValid = value.length >= 2;
                errorMessage = 'Ce champ doit contenir au moins 2 caractères';
                break;
                
            default:
                if (field.hasAttribute('required')) {
                    isValid = value.length > 0;
                    errorMessage = 'Ce champ est obligatoire';
                }
        }
        
        // Application de la validation visuelle
        if (isValid) {
            field.classList.remove('is-invalid');
            field.classList.add('is-valid');
            removeErrorMessage(field);
        } else {
            field.classList.remove('is-valid');
            field.classList.add('is-invalid');
            showErrorMessage(field, errorMessage);
        }
        
        return isValid;
    }

    // 5. Gestion des messages d'erreur
    function showErrorMessage(field, message) {
        removeErrorMessage(field);
        const errorDiv = document.createElement('div');
        errorDiv.className = 'invalid-feedback';
        errorDiv.textContent = message;
        field.parentNode.appendChild(errorDiv);
    }
    
    function removeErrorMessage(field) {
        const existing = field.parentNode.querySelector('.invalid-feedback');
        if (existing) {
            existing.remove();
        }
    }

    // 6. Popup de sortie d'intention (Exit Intent)
    function setupExitIntent() {
        let exitIntentShown = false;
        
        document.addEventListener('mouseleave', function(e) {
            if (e.clientY <= 0 && !exitIntentShown && window.scrollY > 500) {
                exitIntentShown = true;
                showExitIntentPopup();
            }
        });
    }
    
    function showExitIntentPopup() {
        // Créer le popup d'exit intent
        const popup = document.createElement('div');
        popup.className = 'exit-intent-popup';
        popup.innerHTML = `
            <div class="popup-content">
                <div class="popup-header">
                    <h3>⚡ Avant de partir...</h3>
                    <button class="close-popup">&times;</button>
                </div>
                <div class="popup-body">
                    <p><strong>Obtenez votre consultation gratuite de 30 minutes !</strong></p>
                    <ul>
                        <li>✅ Analyse de vos besoins</li>
                        <li>✅ Devis personnalisé</li>
                        <li>✅ Conseils d'experts</li>
                    </ul>
                    <a href="/contact/" class="btn btn-primary btn-lg">
                        📞 Réserver Ma Consultation Gratuite
                    </a>
                </div>
            </div>
        `;
        
        document.body.appendChild(popup);
        
        // Fermer le popup
        popup.querySelector('.close-popup').addEventListener('click', function() {
            popup.remove();
        });
        
        popup.addEventListener('click', function(e) {
            if (e.target === popup) {
                popup.remove();
            }
        });
        
        trackConversionEvent('exit_intent_popup_shown', 'exit_intent');
    }

    // 7. Boutons CTA flottants intelligents
    function setupFloatingCTA() {
        if (window.innerWidth > 768) {
            const floatingCTA = document.createElement('div');
            floatingCTA.className = 'floating-cta';
            floatingCTA.innerHTML = `
                <a href="/contact/" class="btn btn-primary pulse">
                    <i class="bi bi-telephone"></i> Devis Gratuit
                </a>
            `;
            
            floatingCTA.style.cssText = `
                position: fixed;
                bottom: 20px;
                right: 20px;
                z-index: 1000;
                transition: transform 0.3s ease;
            `;
            
            document.body.appendChild(floatingCTA);
            
            // Afficher après scroll
            window.addEventListener('scroll', function() {
                if (window.scrollY > 800) {
                    floatingCTA.style.transform = 'translateY(0)';
                } else {
                    floatingCTA.style.transform = 'translateY(100px)';
                }
            });
        }
    }

    // 8. Amélioration des témoignages avec rotation automatique
    function enhanceTestimonials() {
        const testimonials = document.querySelectorAll('.testimonial-card');
        if (testimonials.length > 0) {
            let currentIndex = 0;
            
            setInterval(() => {
                testimonials.forEach((card, index) => {
                    if (index === currentIndex) {
                        card.style.transform = 'scale(1.02)';
                        card.style.transition = 'all 0.3s ease';
                    } else {
                        card.style.transform = 'scale(1)';
                    }
                });
                
                currentIndex = (currentIndex + 1) % testimonials.length;
            }, 4000);
        }
    }

    // 9. Tracking des interactions CTA
    function trackCTAClicks() {
        document.querySelectorAll('a[href*="/contact/"]').forEach(cta => {
            cta.addEventListener('click', function() {
                const ctaText = this.textContent.trim();
                trackConversionEvent('cta_clicked', ctaText);
            });
        });
        
        document.querySelectorAll('a[href*="/services/"]').forEach(cta => {
            cta.addEventListener('click', function() {
                trackConversionEvent('services_viewed', 'navigation');
            });
        });
    }

    // 10. Personnalisation basée sur le comportement
    function personalizeExperience() {
        // Détecter si l'utilisateur revient
        const isReturningVisitor = localStorage.getItem('gabithex_visited');
        
        if (isReturningVisitor) {
            // Personnaliser pour les visiteurs récurrents
            const heroTitle = document.querySelector('.hero h2');
            if (heroTitle && heroTitle.textContent.includes('Transformez')) {
                heroTitle.textContent = 'De retour ? Concrétisons votre projet !';
            }
        } else {
            // Marquer comme visiteur
            localStorage.setItem('gabithex_visited', 'true');
        }
        
        // Personnalisation selon l'heure
        const hour = new Date().getHours();
        const timeBasedCTA = document.querySelector('.time-based-cta');
        if (timeBasedCTA) {
            if (hour >= 9 && hour <= 17) {
                timeBasedCTA.textContent = '📞 Appelez-nous maintenant !';
                timeBasedCTA.href = 'tel:+33182882030';
            } else {
                timeBasedCTA.textContent = '📧 Laissez-nous un message';
                timeBasedCTA.href = '/contact/';
            }
        }
    }

    // Initialisation de tous les modules
    function init() {
        animateStats();
        optimizeContactForm();
        setupExitIntent();
        setupFloatingCTA();
        enhanceTestimonials();
        trackCTAClicks();
        personalizeExperience();
        
        console.log('GABITHEX Conversion Optimization: Initialized ✓');
    }

    // Lancer l'initialisation
    init();
});

// CSS pour les éléments créés dynamiquement
const conversionCSS = `
<style>
.exit-intent-popup {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.8);
    z-index: 10000;
    display: flex;
    align-items: center;
    justify-content: center;
    animation: fadeIn 0.3s ease;
}

.popup-content {
    background: white;
    border-radius: 20px;
    padding: 2rem;
    max-width: 500px;
    width: 90%;
    position: relative;
    animation: slideInUp 0.3s ease;
}

.popup-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.5rem;
}

.close-popup {
    background: none;
    border: none;
    font-size: 2rem;
    cursor: pointer;
    color: #999;
}

.popup-body ul {
    list-style: none;
    padding: 0;
    margin: 1rem 0;
}

.popup-body li {
    padding: 0.5rem 0;
    color: #28a745;
}

.floating-cta {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 1000;
    transition: transform 0.3s ease;
}

.floating-cta .btn {
    box-shadow: 0 4px 20px rgba(0, 123, 255, 0.4);
    border-radius: 30px;
    padding: 12px 20px;
}

.is-invalid {
    border-color: #dc3545 !important;
}

.is-valid {
    border-color: #28a745 !important;
}

.invalid-feedback {
    color: #dc3545;
    font-size: 0.875rem;
    margin-top: 0.25rem;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

@keyframes slideInUp {
    from { transform: translateY(30px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
}

@media (max-width: 768px) {
    .floating-cta {
        bottom: 10px;
        right: 10px;
    }
    
    .popup-content {
        margin: 1rem;
        padding: 1.5rem;
    }
}
</style>
`;

// Injecter le CSS
document.head.insertAdjacentHTML('beforeend', conversionCSS); 