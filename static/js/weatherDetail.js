const currentListItem = document.querySelectorAll('.remain-time')[0]
const nextWeatherTimeUi = document.querySelector('.next-weather-time')

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
            nextWeatherTimeUi.textContent = `${Math.floor(timeDiff / 60)}분 ${Math.floor(timeDiff % 60)}초 후 날씨 변경`
        }
    }, 100);
}

document.addEventListener('DOMContentLoaded', () => {
    getProgressBar();
});