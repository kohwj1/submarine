const etText = document.getElementById('timer');
const etTextNormal = document.getElementById('normal-clock');

function getEorzeaTime() {
    let timer = setInterval(() => {
        const EORZEA_MULTIPLIER = 3600 / 175;
        const epoch = new Date(1970, 1, 1, 0, 0, 0, 0).getTime();
        let now = new Date().getTime();

        let elapsedEorzeaTime = (now - epoch) * EORZEA_MULTIPLIER;

        let eorzeaTime = new Date(epoch + elapsedEorzeaTime);
        let et_hour = String(eorzeaTime.getHours()).padStart(2, '0');
        let et_minute = String(eorzeaTime.getMinutes()).padStart(2, '0');
        etText.textContent = `${et_hour}:${et_minute}`;
        etTextNormal.textContent = `ET ${et_hour}:${et_minute}`;
    }, 1000);
}

document.addEventListener("DOMContentLoaded", getEorzeaTime)