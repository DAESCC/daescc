document.addEventListener('DOMContentLoaded', () => {
    // Example: Toggle mobile navigation
    const navToggle = document.querySelector('#nav-toggle');
    const navLinks = document.querySelector('nav');

    if (navToggle) {
        navToggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
    }

    // Example: Simple contact form submission handler
    const contactForm = document.querySelector('#contactForm');

    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault(); // Prevent the default form submission

            // Simulate form data handling
            const formData = new FormData(contactForm);
            console.log('Form data:', Object.fromEntries(formData.entries()));

            // Here, you would typically send the form data to a server
            // For demonstration, we'll just show a message
            alert('Thank you for your message. We will get back to you soon.');

            // Reset the form after submission
            contactForm.reset();
        });
    }

    // Add any additional JavaScript functionality needed for your site below
});
