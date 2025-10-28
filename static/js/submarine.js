const areaLabels = document.querySelectorAll('.card.h-100');
let calculateList = []

function tabUIrefresh() {
    const url = new URL(window.location.href);
    const urlParams = url.searchParams;
    const tabs = document.querySelectorAll('.submarine-tab');
    for (tab of tabs) {
        if (urlParams.get('region') == tab.getAttribute('data-value')) {
            tab.classList.add('active');
            tab.setAttribute('aria-current', 'page');
        }
    }
}

function registerEventHandlers() {
    const CalculatorIcon = document.getElementById('CalculatorIcon');
    const CalculatorWindow = document.getElementById('CalculatorWindow');
    const closeCalculator = document.getElementById('closeCalculator');

    CalculatorIcon.addEventListener('click', () => {
        CalculatorIcon.style.display = 'none';
        CalculatorWindow.style.display = 'flex';
    })
    closeCalculator.addEventListener('click', () => {
        CalculatorIcon.style.display = 'flex';
        CalculatorWindow.style.display = 'none';
    })

    for (label of areaLabels) {
        label.addEventListener('click', function() {
            toggleSelector(this);
            console.log(calculateList);
        })
    }
}

function toggleSelector(targetElement) {
    targetElement.classList.toggle('text-bg-primary');
    if (targetElement.classList.contains('text-bg-primary')) {
        calculateList.push(targetElement.getAttribute('data-value'))
    } else {
        calculateList.splice(calculateList.indexOf(targetElement.getAttribute('data-value')), 1)
    }
}

function calculateArriveTime(minutesToAdd) {
    const now = new Date();
    const futureTimeMs = now.getTime() + (minutesToAdd * 60000);
    const futureDate = new Date(futureTimeMs);
    const year = futureDate.getFullYear();
    const month = String(futureDate.getMonth() + 1).padStart(2, '0');
    const day = String(futureDate.getDate()).padStart(2, '0');
    const hours = String(futureDate.getHours()).padStart(2, '0');
    const minutes = String(futureDate.getMinutes()).padStart(2, '0');
    return `${year}-${month}-${day} ${hours}:${minutes}`;
}

document.addEventListener('DOMContentLoaded', function() {
    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
    const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))
    registerEventHandlers();
    tabUIrefresh();
})

document.querySelector('.btn-reset').addEventListener('click', function() {
    for (label of areaLabels) {
        label.classList.remove('text-bg-primary');
    };
    calculateList = [];
    document.querySelector('.alert-primary').innerHTML = "잠수함 해역을 선택해주세요";
})

document.querySelector('.btn-calculate').addEventListener('click', async function() {
    if (calculateList.length == 0) {
        alert("해역을 1개 이상 선택해주세요");
    } else {
        const estimateArea = document.querySelector('.alert-primary');
        estimateArea.innerHTML = `<div class="spinner-border" role="status">`
        const res = await fetch('/api/submarine/navigate', {
            method: "POST",
            headers: {"Content-Type":"application/json"},
            body: JSON.stringify({navigate_path: calculateList}),
        });
        const bestRoute = await res.json();
        const submarineSpeed = document.getElementById('speed-input').value;
        const duration = Math.ceil(bestRoute.time / submarineSpeed) + 720;
        const durationDay = Math.floor(duration / 1440);
        const durationHour = Math.floor((duration % 1440) / 60);
        const durationMinute = duration % 60;
        estimateArea.innerHTML = `
            <ul class="m-0">
                <li>최적 경로: ${bestRoute.path}</li>
                <li>탐사 소요 시간: ${durationDay}일 ${durationHour}시간 ${durationMinute}분 (${calculateArriveTime(duration)} 도착 예정)</li>
            </ul>`
    }
})