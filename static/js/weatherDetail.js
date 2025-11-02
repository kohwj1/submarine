const currentListItem = document.querySelectorAll('.remain-time')[0]

function getProgressBar() {
    const strNextWeatherTime = document.querySelectorAll('.unix-time')[1].textContent.replace(' ','T');
    const nextWeatherTime = new Date(strNextWeatherTime);
    
    let timer = setInterval(() => {
        let nowTime = new Date();
        let timeDiff = (nextWeatherTime.getTime() - nowTime.getTime())/1000;
        let barPercent = (timeDiff/1400)*100;
        if (barPercent < 0) {
            clearInterval(timer);
            location.reload();
        } else {
            currentListItem.style.background = `linear-gradient(to right, #d9e8ff ${barPercent}%, transparent ${100 - barPercent}%)`;
            // currentListItem.setAttribute('data-bs-title', `${Math.floor(timeDiff / 60)}분 ${Math.floor(timeDiff % 60)}초 후에 날씨가 변경됩니다.`)

            currentListItem.setAttribute('aria-valuenow', barPercent);
        }
    }, 1000);
}

document.addEventListener('DOMContentLoaded', () => {
    // currentListItem.setAttribute('data-bs-toggle', 'tooltip');
    // currentListItem.setAttribute('data-bs-placement', 'bottom');
    // currentListItem.setAttribute('data-bs-title', '-');
    // const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    // const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));
    getProgressBar();
});