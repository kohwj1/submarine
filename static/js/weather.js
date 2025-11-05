let spoilerFilter = false;

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