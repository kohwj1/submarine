let spoilerFilter = false;

document.addEventListener('DOMContentLoaded', function() {
    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
    const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))
})

document.getElementById('switchCheck').addEventListener('click', function() {
    spoilerFilter = !spoilerFilter;
    if (spoilerFilter) {
        targetPlace = document.querySelectorAll('.spoiler')
        for (place of targetPlace) {
            place.classList.remove('spoiler');
            place.classList.add('spoiler-free');
        }
    } else {
        targetPlace = document.querySelectorAll('.spoiler-free')
        for (place of targetPlace) {
            place.classList.remove('spoiler-free');
            place.classList.add('spoiler');
        }
    }
})