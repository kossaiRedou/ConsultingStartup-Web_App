/**
* Template Name: Company
* Template URL: https://bootstrapmade.com/company-free-html-bootstrap-template/
* Updated: Aug 07 2024 with Bootstrap v5.3.3
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/

(function() {
  "use strict";

  /**
   * Apply .scrolled class to the body as the page is scrolled down
   */
  function toggleScrolled() {
    const selectBody = document.querySelector('body');
    const selectHeader = document.querySelector('#header');
    if (!selectHeader.classList.contains('scroll-up-sticky') && !selectHeader.classList.contains('sticky-top') && !selectHeader.classList.contains('fixed-top')) return;
    window.scrollY > 100 ? selectBody.classList.add('scrolled') : selectBody.classList.remove('scrolled');
  }

  document.addEventListener('scroll', toggleScrolled);
  window.addEventListener('load', toggleScrolled);

  /**
   * Mobile nav toggle
   */
  const mobileNavToggleBtn = document.querySelector('.mobile-nav-toggle');

  function mobileNavToogle() {
    document.querySelector('body').classList.toggle('mobile-nav-active');
    mobileNavToggleBtn.classList.toggle('bi-list');
    mobileNavToggleBtn.classList.toggle('bi-x');
  }
  mobileNavToggleBtn.addEventListener('click', mobileNavToogle);

  /**
   * Hide mobile nav on same-page/hash links
   */
  document.querySelectorAll('#navmenu a').forEach(navmenu => {
    navmenu.addEventListener('click', () => {
      if (document.querySelector('.mobile-nav-active')) {
        mobileNavToogle();
      }
    });

  });

  /**
   * Toggle mobile nav dropdowns
   */
  document.querySelectorAll('.navmenu .toggle-dropdown').forEach(navmenu => {
    navmenu.addEventListener('click', function(e) {
      e.preventDefault();
      this.parentNode.classList.toggle('active');
      this.parentNode.nextElementSibling.classList.toggle('dropdown-active');
      e.stopImmediatePropagation();
    });
  });

  /**
   * Preloader
   */
  const preloader = document.querySelector('#preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      preloader.remove();
    });
  }

  /**
   * Scroll top button
   */
  let scrollTop = document.querySelector('.scroll-top');

  function toggleScrollTop() {
    if (scrollTop) {
      window.scrollY > 100 ? scrollTop.classList.add('active') : scrollTop.classList.remove('active');
    }
  }
  scrollTop.addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });

  window.addEventListener('load', toggleScrollTop);
  document.addEventListener('scroll', toggleScrollTop);

  /**
   * Animation on scroll function and init
   */
  function aosInit() {
    AOS.init({
      duration: 600,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    });
  }
  window.addEventListener('load', aosInit);

  /**
   * Auto generate the carousel indicators
   */
  document.querySelectorAll('.carousel-indicators').forEach((carouselIndicator) => {
    carouselIndicator.closest('.carousel').querySelectorAll('.carousel-item').forEach((carouselItem, index) => {
      if (index === 0) {
        carouselIndicator.innerHTML += `<li data-bs-target="#${carouselIndicator.closest('.carousel').id}" data-bs-slide-to="${index}" class="active"></li>`;
      } else {
        carouselIndicator.innerHTML += `<li data-bs-target="#${carouselIndicator.closest('.carousel').id}" data-bs-slide-to="${index}"></li>`;
      }
    });
  });

  /**
   * Initiate glightbox
   */
  const glightbox = GLightbox({
    selector: '.glightbox'
  });

  /**
   * Init isotope layout and filters
   */
  document.querySelectorAll('.isotope-layout').forEach(function(isotopeItem) {
    let layout = isotopeItem.getAttribute('data-layout') ?? 'masonry';
    let filter = isotopeItem.getAttribute('data-default-filter') ?? '*';
    let sort = isotopeItem.getAttribute('data-sort') ?? 'original-order';

    let initIsotope;
    imagesLoaded(isotopeItem.querySelector('.isotope-container'), function() {
      initIsotope = new Isotope(isotopeItem.querySelector('.isotope-container'), {
        itemSelector: '.isotope-item',
        layoutMode: layout,
        filter: filter,
        sortBy: sort
      });
    });

    isotopeItem.querySelectorAll('.isotope-filters li').forEach(function(filters) {
      filters.addEventListener('click', function() {
        isotopeItem.querySelector('.isotope-filters .filter-active').classList.remove('filter-active');
        this.classList.add('filter-active');
        initIsotope.arrange({
          filter: this.getAttribute('data-filter')
        });
        if (typeof aosInit === 'function') {
          aosInit();
        }
      }, false);
    });

  });

  /**
   * Animate the skills items on reveal
   */
  let skillsAnimation = document.querySelectorAll('.skills-animation');
  skillsAnimation.forEach((item) => {
    new Waypoint({
      element: item,
      offset: '80%',
      handler: function(direction) {
        let progress = item.querySelectorAll('.progress .progress-bar');
        progress.forEach(el => {
          el.style.width = el.getAttribute('aria-valuenow') + '%';
        });
      }
    });
  });

  /**
   * Init swiper sliders
   */
  function initSwiper() {
    document.querySelectorAll(".init-swiper").forEach(function(swiperElement) {
      let config = JSON.parse(
        swiperElement.querySelector(".swiper-config").innerHTML.trim()
      );

      if (swiperElement.classList.contains("swiper-tab")) {
        initSwiperWithCustomPagination(swiperElement, config);
      } else {
        new Swiper(swiperElement, config);
      }
    });
  }

  window.addEventListener("load", initSwiper);

  var swiper = new Swiper('.mySwiper', {
    slidesPerView: 3,
    spaceBetween: 30,
    loop: true,
    autoplay: { delay: 2000 },
    breakpoints: {
      640: { slidesPerView: 2 },
      1024: { slidesPerView: 3 }
    }
  });

  var testimonialSwiper = new Swiper('.testimonialSwiper', {
    slidesPerView: 1,
    loop: true,
    autoplay: { delay: 4000 },
    navigation: false,
    pagination: { el: '.swiper-pagination', clickable: true }
  });

})();

/**
 * Homepage Enhancements
 */
document.addEventListener('DOMContentLoaded', function() {
  // Animate stats on scroll
  const stats = document.querySelectorAll('.stat-card h3');
  if (stats.length) {
    const animateStats = () => {
      stats.forEach(stat => {
        const value = parseInt(stat.textContent);
        if (!stat.dataset.animated && isElementInViewport(stat)) {
          animateValue(stat, 0, value, 2000);
          stat.dataset.animated = true;
        }
      });
    };

    window.addEventListener('scroll', animateStats);
    animateStats(); // Initial check
  }

  // Parallax effect for hero section
  const hero = document.querySelector('.hero');
  if (hero) {
    window.addEventListener('scroll', () => {
      const scrolled = window.pageYOffset;
      hero.style.backgroundPositionY = -(scrolled * 0.5) + 'px';
    });
  }

  // Smooth scroll for navigation links
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
});

// Utility functions
function isElementInViewport(el) {
  const rect = el.getBoundingClientRect();
  return (
    rect.top >= 0 &&
    rect.left >= 0 &&
    rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
    rect.right <= (window.innerWidth || document.documentElement.clientWidth)
  );
}

function animateValue(obj, start, end, duration) {
  let startTimestamp = null;
  const step = (timestamp) => {
    if (!startTimestamp) startTimestamp = timestamp;
    const progress = Math.min((timestamp - startTimestamp) / duration, 1);
    obj.innerHTML = Math.floor(progress * (end - start) + start) + (obj.textContent.includes('%') ? '%' : '+');
    if (progress < 1) {
      window.requestAnimationFrame(step);
    }
  };
  window.requestAnimationFrame(step);
}

/**
 * Animate number counters
 */
function animateCounter(element, start = 0, end, duration = 2000) {
  let startTimestamp = null;
  const step = (timestamp) => {
    if (!startTimestamp) startTimestamp = timestamp;
    const progress = Math.min((timestamp - startTimestamp) / duration, 1);
    const value = Math.floor(progress * (end - start) + start);
    element.textContent = value + (element.textContent.includes('+') ? '+' : element.textContent.includes('%') ? '%' : 'h');
    if (progress < 1) {
      window.requestAnimationFrame(step);
    }
  };
  window.requestAnimationFrame(step);
}

// Initialize counter animations when they come into view
const counterObserver = new IntersectionObserver((entries, observer) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const counter = entry.target;
      const value = parseInt(counter.textContent);
      animateCounter(counter, 0, value);
      observer.unobserve(counter);
    }
  });
}, {
  threshold: 0.5
});

// Observe all counter elements
document.querySelectorAll('.counter').forEach(counter => {
  counterObserver.observe(counter);
});

// Reinitialize counters on carousel slide
document.querySelector('#hero-carousel').addEventListener('slid.bs.carousel', function () {
  document.querySelectorAll('.carousel-item.active .counter').forEach(counter => {
    const value = parseInt(counter.textContent);
    animateCounter(counter, 0, value, 1000);
  });
});

/**
 * GABITHEX Homepage Enhancements
 */
document.addEventListener('DOMContentLoaded', function() {
  // Smooth reveal of value items on scroll
  const valueItems = document.querySelectorAll('.value-item');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
      }
    });
  }, { threshold: 0.2 });

  valueItems.forEach(item => {
    item.style.opacity = '0';
    item.style.transform = 'translateY(20px)';
    item.style.transition = 'all 0.6s ease-out';
    observer.observe(item);
  });

  // Service card hover effects
  const serviceCards = document.querySelectorAll('.service-card');
  serviceCards.forEach(card => {
    card.addEventListener('mouseenter', function() {
      this.style.transform = 'translateY(-10px)';
      const icon = this.querySelector('.icon');
      if (icon) {
        icon.style.transform = 'scale(1.1)';
      }
    });

    card.addEventListener('mouseleave', function() {
      this.style.transform = 'translateY(0)';
      const icon = this.querySelector('.icon');
      if (icon) {
        icon.style.transform = 'scale(1)';
      }
    });
  });

  // Parallax effect for sections with bg-pattern
  const parallaxSections = document.querySelectorAll('.bg-pattern');
  window.addEventListener('scroll', () => {
    parallaxSections.forEach(section => {
      const scrolled = window.pageYOffset;
      const rate = scrolled * 0.15;
      section.style.backgroundPosition = `center ${rate}px`;
    });
  });

  // Animate numbers in stats
  function animateValue(obj, start, end, duration) {
    let startTimestamp = null;
    const step = (timestamp) => {
      if (!startTimestamp) startTimestamp = timestamp;
      const progress = Math.min((timestamp - startTimestamp) / duration, 1);
      obj.innerHTML = Math.floor(progress * (end - start) + start);
      if (progress < 1) {
        window.requestAnimationFrame(step);
      }
    };
    window.requestAnimationFrame(step);
  }

  // Initialize stats animation
  const stats = document.querySelectorAll('.stat-number');
  const statsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting && !entry.target.dataset.animated) {
        const endValue = parseInt(entry.target.dataset.value);
        animateValue(entry.target, 0, endValue, 2000);
        entry.target.dataset.animated = 'true';
      }
    });
  }, { threshold: 0.5 });

  stats.forEach(stat => statsObserver.observe(stat));

  // Floating CTA button
  const floatingCTA = document.createElement('div');
  floatingCTA.className = 'floating-cta';
  floatingCTA.innerHTML = `
    <a href="/contact" class="btn btn-primary btn-lg btn-pulse">
      <i class="bi bi-chat-dots-fill"></i>
      <span>Parlons de votre projet</span>
    </a>
  `;
  document.body.appendChild(floatingCTA);

  // Show/hide floating CTA based on scroll position
  let lastScrollTop = 0;
  window.addEventListener('scroll', () => {
    const st = window.pageYOffset || document.documentElement.scrollTop;
    if (st > lastScrollTop && st > 300) {
      floatingCTA.style.transform = 'translateY(0)';
    } else {
      floatingCTA.style.transform = 'translateY(100%)';
    }
    lastScrollTop = st <= 0 ? 0 : st;
  });

  // Add loading animation to buttons
  const buttons = document.querySelectorAll('.btn');
  buttons.forEach(button => {
    button.addEventListener('click', function(e) {
      if (!this.classList.contains('btn-loading')) {
        this.classList.add('btn-loading');
        const originalText = this.innerHTML;
        this.innerHTML = '<i class="bi bi-arrow-repeat spin"></i> Chargement...';
        
        setTimeout(() => {
          this.classList.remove('btn-loading');
          this.innerHTML = originalText;
        }, 1000);
      }
    });
  });
});

// Add these styles to your CSS
const style = document.createElement('style');
style.textContent = `
  .floating-cta {
    position: fixed;
    bottom: 30px;
    right: 30px;
    z-index: 1000;
    transform: translateY(100%);
    transition: transform 0.3s ease;
  }

  .floating-cta .btn {
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  }

  .floating-cta .btn span {
    margin-left: 8px;
  }

  @keyframes spin {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
  }

  .spin {
    display: inline-block;
    animation: spin 1s linear infinite;
  }

  .btn-loading {
    pointer-events: none;
    opacity: 0.8;
  }
`;
document.head.appendChild(style);

/**
 * Initialize Testimonials Slider
 */
document.addEventListener('DOMContentLoaded', function() {
  const testimonialsSlider = new Swiper('.testimonials-slider .swiper-container', {
    slidesPerView: 1,
    spaceBetween: 30,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false,
    },
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
    navigation: {
      nextEl: '.nav-next',
      prevEl: '.nav-prev',
    },
    breakpoints: {
      768: {
        slidesPerView: 2,
      },
      1024: {
        slidesPerView: 3,
      },
    },
    effect: 'coverflow',
    coverflowEffect: {
      rotate: 0,
      stretch: 0,
      depth: 100,
      modifier: 1,
      slideShadows: false,
    },
  });

  // Animate trust badges on scroll
  const trustBadges = document.querySelectorAll('.trust-badge');
  const trustBadgesObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.transform = 'translateY(0)';
        entry.target.style.opacity = '1';
      }
    });
  }, { threshold: 0.2 });

  trustBadges.forEach(badge => {
    badge.style.transform = 'translateY(20px)';
    badge.style.opacity = '0';
    badge.style.transition = 'all 0.6s ease-out';
    trustBadgesObserver.observe(badge);
  });

  // Animate testimonial items on scroll
  const testimonialItems = document.querySelectorAll('.testimonial-item');
  const testimonialObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animate__animated', 'animate__fadeIn');
        entry.target.style.opacity = '1';
      }
    });
  }, { threshold: 0.2 });

  testimonialItems.forEach(item => {
    item.style.opacity = '0';
    testimonialObserver.observe(item);
  });

  // Add hover effect to testimonial items
  testimonialItems.forEach(item => {
    item.addEventListener('mouseenter', () => {
      item.style.transform = 'translateY(-10px)';
    });
    item.addEventListener('mouseleave', () => {
      item.style.transform = 'translateY(0)';
    });
  });
});

/**
 * Initialize Testimonials Carousel
 */
document.addEventListener('DOMContentLoaded', function() {
  // Initialize Bootstrap Carousel
  const testimonialCarousel = new bootstrap.Carousel(document.getElementById('testimonialCarousel'), {
    interval: 5000,
    touch: true,
    pause: 'hover'
  });

  // Animate testimonial items on slide
  const carousel = document.getElementById('testimonialCarousel');
  carousel.addEventListener('slide.bs.carousel', function (e) {
    const activeItem = e.relatedTarget;
    const testimonialContent = activeItem.querySelector('.testimonial-content');
    const testimonialAuthor = activeItem.querySelector('.testimonial-author');
    
    // Reset animations
    testimonialContent.style.opacity = '0';
    testimonialContent.style.transform = 'translateY(20px)';
    testimonialAuthor.style.opacity = '0';
    testimonialAuthor.style.transform = 'translateY(20px)';
    
    // Trigger animations after a short delay
    setTimeout(() => {
      testimonialContent.style.transition = 'all 0.5s ease-out';
      testimonialContent.style.opacity = '1';
      testimonialContent.style.transform = 'translateY(0)';
      
      setTimeout(() => {
        testimonialAuthor.style.transition = 'all 0.5s ease-out';
        testimonialAuthor.style.opacity = '1';
        testimonialAuthor.style.transform = 'translateY(0)';
      }, 200);
    }, 300);
  });

  // Add hover effects to carousel controls
  const carouselControls = document.querySelectorAll('.carousel-control-prev, .carousel-control-next');
  carouselControls.forEach(control => {
    control.addEventListener('mouseenter', function() {
      this.style.transform = 'translateY(-50%) scale(1.1)';
    });
    control.addEventListener('mouseleave', function() {
      this.style.transform = 'translateY(-50%) scale(1)';
    });
  });
});