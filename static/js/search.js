const keywordInput = document.getElementById('filter')
const itemList = document.querySelectorAll('.item-name')


keywordInput.addEventListener('input', function() {
    const searchKeyword = keywordInput.value;
    // console.log(searchKeyword);
    if (searchKeyword == "") {
        for (item of itemList) {
            let tableRow = item.parentElement.parentElement;
            tableRow.style.display = "table-row";
        }
    } else {
        for (item of itemList) {
            let tableRow = item.parentElement.parentElement;
            if (item.textContent.includes(searchKeyword)) {
                tableRow.style.display = "table-row";
            } else {
                tableRow.style.display = "none";
            }
        }
    }
})