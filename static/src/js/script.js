const manageScroll = function() {
    let header = document.getElementById('am-main-bar');
    let scrollTop = window.scrollY;

    if(scrollTop >= 75) {
        header.classList.add('main-bar--sticky');
    } else {
        header.classList.remove('main-bar--sticky');
    }
}

window.addEventListener('scroll', manageScroll, false);