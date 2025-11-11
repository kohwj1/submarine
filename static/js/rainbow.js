function etConvert(timeStr) {
    const strTime = timeStr.replace(' ','T')
    const unixTime = new Date(strTime);
    const etUnix = (unixTime.getTime() * 3600 / 175);
    const minutes = String(parseInt((etUnix / (1000 * 60)) % 60)).padStart(2,'0');
    const hours = String(parseInt((etUnix / (1000 * 60 * 60)) % 24)).padStart(2, '0');
    return `${hours}:${minutes}`
}

document.addEventListener('DOMContentLoaded', () => {
    const timeList = document.querySelectorAll('.rainbow-time');
    for (t of timeList) {
        t.innerHTML += `<small class='et-convert'>ET ${etConvert(t.innerText)}</small>`;
    }
})