const topNavSearchBar = document.getElementById('search-bar')
const topNavSearchBarLabel = document.getElementById('search-bar-label');
const topNavSearchButton = document.getElementById('am-search-bar-button');
const searchInput = document.getElementById('search');
const burgerMenu = document.getElementById('am-burger-icon');
const mainNav = document.getElementById('am-main-nav');
const subNavToggle = document.getElementById('am-sub-nav-toggle');
const subNav = document.getElementById('am-sub-nav');
const closeMenuButton = document.getElementById('am-close-menu');
const menuBlocker = document.getElementById('am-main-nav-blocker');
const body = document.getElementsByTagName('body')[0];
const catalogueFilters = document.getElementById('am-catalogue-filters');
const catalogueFiltersTitle = document.getElementById('am-catalogue-filters-title');

topNavSearchBarLabel.classList.remove('search-bar__label--label-style');

const manageScroll = function() {
    let header = document.getElementById('am-main-bar');
    let topNav = document.getElementById('am-top-nav');
    let scrollTop = window.scrollY;

    let width = window.screen.width;

    if (width <= 750) {
        if(scrollTop >= 70) {
            topNav.classList.add('top-nav--sticky');
        } else {
            topNav.classList.remove('top-nav--sticky');
        }
    } else {
        if(scrollTop >= 75) {
            header.classList.add('main-bar--sticky');
        } else {
            header.classList.remove('main-bar--sticky');
        }
    }
}

const moveLabelUp = function() {
    topNavSearchBarLabel.classList.add('search-bar__label--label-style');
}

const moveLabelDown = function() {
    if(search.value) return;
    topNavSearchBarLabel.classList.remove('search-bar__label--label-style');
    topNavSearchBarLabel.classList.add('search-bar__label--placeholder-style');
}

const deploySearchBar = function() {
    topNavSearchBar.classList.add('search-bar--focus');
    searchInput.focus();
}

const minimizeSearchBar = function() {
    if(search.value) return;
    topNavSearchBar.classList.remove('search-bar--focus');
}

const openMenu = function() {
    mainNav.classList.add('main-nav--opened');
    body.classList.add('body-with-opened-menu');
}

const closeMenu = function() {
    mainNav.classList.remove('main-nav--opened');
    body.classList.remove('body-with-opened-menu');
}

const toggleSubNav = function(event) {
    event.preventDefault();
    subNav.classList.toggle('main-nav__sub-nav--opened');
}

const toggleCatalogueFilters = function() {
    catalogueFilters.classList.toggle('catalogue-filters--closed');
}

// events listeners

window.addEventListener('scroll', manageScroll);
topNavSearchBar.addEventListener('focusin', function () {
    moveLabelUp();
    deploySearchBar();
});

topNavSearchBar.addEventListener('focusout', function () {
    moveLabelDown();
    minimizeSearchBar();
});

topNavSearchButton.addEventListener('click', deploySearchBar);

burgerMenu.addEventListener('click', openMenu);
closeMenuButton.addEventListener('click', closeMenu);
subNavToggle.addEventListener('click', toggleSubNav);
menuBlocker.addEventListener('click', closeMenu);
catalogueFiltersTitle.addEventListener('click', toggleCatalogueFilters)