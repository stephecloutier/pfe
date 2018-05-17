
const topNavSearchBar = document.getElementById('search-bar')
const topNavSearchBarLabel = document.getElementById('search-bar-label');
const topNavSearchButton = document.getElementById('am-search-bar-button');
const searchInput = document.getElementById('search');

topNavSearchBarLabel.classList.remove('search-bar__label--label-style');

const manageScroll = function() {
    let header = document.getElementById('am-main-bar');
    let topNav = document.getElementById('am-top-nav');
    let scrollTop = window.scrollY;

    let width = window.screen.width;

    if (width <= 720) {
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