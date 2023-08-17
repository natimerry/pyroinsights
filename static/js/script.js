'use strict';

const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting){
            entry.target.classList.add('cta-content-shown');
        }
    });
});
const hiddenElement = document.querySelectorAll(".cta-content-hidden");



/**
 * navbar toggle
 */

const navOpenBtn = document.querySelector("[data-nav-open-btn]");
const navbar = document.querySelector("[data-navbar]");
const navCloseBtn = document.querySelector("[data-nav-close-btn]");

const navElemArr = [navOpenBtn, navCloseBtn];

for (let i = 0; i < navElemArr.length; i++) {
  navElemArr[i].addEventListener("click", function () {
    navbar.classList.toggle("active");
  });
}

/**
 * toggle navbar when click any navbar link
 */

const navbarLinks = document.querySelectorAll("[data-nav-link]");

for (let i = 0; i < navbarLinks.length; i++) {
  navbarLinks[i].addEventListener("click", function () {
    navbar.classList.remove("active");
  });
}





/**
 * header active when window scrolled down
 */

const header = document.querySelector("[data-header]");

window.addEventListener("scroll", function () {
  window.scrollY >= 50 ? header.classList.add("active")
    : header.classList.remove("active");
});


const openbutton = document.querySelectorAll("[data-open-modal]");
const closebutton = document.querySelector("[data-close-modal]"); 
const modal = document.querySelector("[data-modal]");
// const overlay = document.querySelector("[data-overlay]"); 


openbutton.forEach(x => {
    console.log(x);
    x.addEventListener("click",() =>{
        modal.classList.add("open");
        // overlay.classList.add("open");
        modal.showModal();
      })
})


closebutton.addEventListener("click",() =>{
  modal.classList.remove("open");
  // overlay.classList.remove("open");
  modal.close();
})
