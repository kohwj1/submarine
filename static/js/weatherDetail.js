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
            currentListItem.style.background = `linear-gradient(to right, #d9e8ff ${barPercent}%, transparent ${barPercent}%)`;

            currentListItem.setAttribute('aria-valuenow', barPercent);
        }
    }, 100);
}

document.addEventListener('DOMContentLoaded', () => {
    getProgressBar();
});