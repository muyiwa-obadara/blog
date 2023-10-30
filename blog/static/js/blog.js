/**
 * JavaScript File for the Blog Application
 * MIT Licence
 * Developer: Muyiwa J. Obadara
 * Email: muyiwa.j.obadara@gmail.com4
 */

const navToggleBtn = document.querySelector('#nav-toggle-btn');

function toggleNow() {
    navToggleBtn.classList.toggle('fa-close');
}




navToggleBtn.addEventListener('click', toggleNow);