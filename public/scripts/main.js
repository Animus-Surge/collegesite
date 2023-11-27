// Small screen navbar logic
// --------------------------------------------------------

const nav = document.querySelector('.nav');
const navToggle = document.querySelector('.nav__toggle');

navToggle.addEventListener('click', () => {
    nav.classList.toggle('nav--visible');
    }
);
