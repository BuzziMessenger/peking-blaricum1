/* =============================================
   Peking Blaricum - JavaScript
   ============================================= */
(function() {
    'use strict';

    // Mobile Nav Toggle
    var navToggle = document.getElementById('navToggle');
    var nav = document.getElementById('nav');
    if (navToggle && nav) {
        navToggle.addEventListener('click', function() {
            var open = nav.classList.toggle('open');
            navToggle.classList.toggle('open', open);
            navToggle.setAttribute('aria-expanded', open);
            document.body.style.overflow = open ? 'hidden' : '';
        });
        nav.querySelectorAll('a').forEach(function(link) {
            link.addEventListener('click', function() {
                nav.classList.remove('open');
                navToggle.classList.remove('open');
                navToggle.setAttribute('aria-expanded', 'false');
                document.body.style.overflow = '';
            });
        });
    }

    // Header scroll effect
    var header = document.getElementById('header');
    if (header) {
        var onScroll = function() {
            if (window.scrollY > 30) header.classList.add('scrolled');
            else header.classList.remove('scrolled');
        };
        window.addEventListener('scroll', onScroll, { passive: true });
        onScroll();
    }

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
        anchor.addEventListener('click', function(e) {
            var target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                var offset = 80;
                var top = target.getBoundingClientRect().top + window.scrollY - offset;
                window.scrollTo({ top: top, behavior: 'smooth' });
            }
        });
    });

    // Opening status badge
    var hoursStatus = document.getElementById('hoursStatus');
    if (hoursStatus) {
        var updateStatus = function() {
            var now = new Date();
            var day = now.getDay();
            var hour = now.getHours();
            var min = now.getMinutes();
            var time = hour + min / 60;
            if (day === 2) {
                hoursStatus.textContent = 'Momenteel gesloten - dinsdag zijn wij gesloten';
                hoursStatus.className = 'hours-status closed';
            } else if (time >= 16 && time < 20.75) {
                hoursStatus.textContent = 'Nu geopend - keuken tot 20:45';
                hoursStatus.className = 'hours-status open';
            } else if (time >= 20.75 && time < 21) {
                hoursStatus.textContent = 'Bijna sluitingstijd - nog even snel langskomen!';
                hoursStatus.className = 'hours-status open';
            } else {
                hoursStatus.textContent = 'Momenteel gesloten - open van 16:00 tot 21:00';
                hoursStatus.className = 'hours-status closed';
            }
        };
        updateStatus();
        setInterval(updateStatus, 60000);
    }

    // Highlight today in hours
    var days = ['Zondag','Maandag','Dinsdag','Woensdag','Donderdag','Vrijdag','Zaterdag'];
    var todayName = days[new Date().getDay()];
    document.querySelectorAll('.hours-row').forEach(function(row) {
        var dayEl = row.querySelector('.hours-day');
        if (dayEl && dayEl.textContent === todayName) row.classList.add('today');
    });

    // Year in footer
    var yearEl = document.getElementById('year');
    if (yearEl) yearEl.textContent = new Date().getFullYear();

    // Reveal on scroll
    if ('IntersectionObserver' in window) {
        var observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });
        document.querySelectorAll('.section, .stat-card, .contact-block').forEach(function(el) {
            el.classList.add('reveal');
            observer.observe(el);
        });
    }
})();