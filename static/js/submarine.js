const tabs = document.querySelectorAll('.submarine-tab');
let navigate_time_list = new Array;

for (tab of tabs) {
    tab.addEventListener('click', function() {
        const currentActiveTab = document.querySelector('.submarine-tab.active');
        if (currentActiveTab) {
            currentActiveTab.classList.remove('active');
            currentActiveTab.removeAttribute('aria-current');
        }
        this.classList.add('active');
        this.setAttribute('aria-current', 'page');

        const dataValue = this.getAttribute('data-value');
        if (dataValue) {
            getAreaList(dataValue);
        }
    })
}

async function getAreaList(region) {
    const tbody = document.getElementById('submarine-tbody');
    tbody.innerHTML = '';
    const res = await fetch(`/api/submarine/area?id=${region}`);
    const resdata = await res.json();
    const response_data = await resdata.data;
    
    for (row of response_data) {
        const tableRow = document.createElement('tr');
        const areaCheckbox = document.createElement('td');
        const areaName = document.createElement('td');
        const areaExp = document.createElement('td');
        const areaSpec = document.createElement('td');
        const areaRewardsTier0 = document.createElement('td');
        const areaRewardsTier1 = document.createElement('td');
        const areaRewardsTier2 = document.createElement('td');

        areaRewardsTier0.classList.add('reward-col');
        areaRewardsTier1.classList.add('reward-col');
        areaRewardsTier2.classList.add('reward-col');

        const areaUnlock = document.createElement('td');
        areaCheckbox.innerHTML = `<div class="form-check form-switch"><input class="form-check-input" name=${row.areaId} value=${row.areaId} type="checkbox"></div>`
        areaCheckbox.classList.add('checkcol');
        areaName.innerHTML = `${row.name}<br><small>Lv.${row.reqRank} 이상</small>`;
        areaExp.textContent = `${row.exp.toLocaleString()}`;
        areaSpec.textContent = row.minSpec;
        areaUnlock.innerHTML = `${row.unlock.join("<br>")}`;
        const tier0 = row.rewards.tier0;
        const tier1 = row.rewards.tier1;
        const tier2 = row.rewards.tier2;
        for (row of tier0) {
            areaRewardsTier0.innerHTML += `<a class="official-guide" href="https://guide.ff14.co.kr/lodestone/db/item/${row.itemId}" target="_blank">${row.name}</a><br>`
        };
        for (row of tier1) {
            areaRewardsTier1.innerHTML += `<a class="official-guide" href="https://guide.ff14.co.kr/lodestone/db/item/${row.itemId}" target="_blank">${row.name}</a><br>`
        };
        for (row of tier2) {
            areaRewardsTier2.innerHTML += `<a class="official-guide" href="https://guide.ff14.co.kr/lodestone/db/item/${row.itemId}" target="_blank">${row.name}</a><br>`
        };
        tableRow.appendChild(areaCheckbox);
        tableRow.appendChild(areaName);
        tableRow.appendChild(areaExp);
        tableRow.appendChild(areaSpec);
        tableRow.appendChild(areaRewardsTier0);
        tableRow.appendChild(areaRewardsTier1);
        tableRow.appendChild(areaRewardsTier2);
        tableRow.appendChild(areaUnlock);
        tbody.appendChild(tableRow);
    }
}

document.addEventListener('DOMContentLoaded', async () => {
    const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
    const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))
    getAreaList('6')
})