const canvas = document.getElementById('converted');
const ctx = canvas.getContext('2d');
const textArea = document.getElementById('userInput');
const fontSizeSelector = 21;
const fontFaceSelector = document.querySelectorAll('input[name="font-face"]');

const btnDownload = document.getElementById('btn-download');

function textConvert() {
    const originText = textArea.value;
    // const fontSize = fontSizeSelector.value;
    const fontSize = fontSizeSelector;
    const fontFace = document.querySelector('input[name="font-face"]:checked').value;
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.font = `${fontSize}px ${fontFace}`;
    ctx.fillStyle = 'black';
    ctx.textAlign = 'left';
    const lines = originText.split('\n');
    let yPos = 30;
    const lineHeight = parseInt(fontSize/2 + 10);
    
    for (const line of lines) {
        ctx.fillText(line, 10, yPos);
        yPos += lineHeight;
    }
}

document.addEventListener('DOMContentLoaded', () => {
    textArea.value = 
`Thy Life is a riddle, to bear rapture and sorrow
To listen, to suffer, to entrust unto tomorrow
In one fleeting moment, from the Land doth life flow
Yet in one fleeting moment, for anew it doth grow
In the same fleeting moment
Thou must live, die, and know

このたびのおわりは、あしたへのいっぽなのだから

1234567890
１２３４５６７８９０`;
    textConvert();
});
textArea.addEventListener('input', textConvert);

for (radio of fontFaceSelector) {
    radio.addEventListener('click', textConvert)
}

btnDownload.addEventListener('click', () => {
    if (textArea.value.trim() == '') {
        alert('한 글자 이상 입력해주세요.')
    } else {
        const dataURL = canvas.toDataURL('image/png');
        const img = document.createElement('img');
        img.src = dataURL;
        const link = document.createElement('a');
        link.download = 'image.png';
        link.href = dataURL.replace('image/png', 'image/octet-stream');
        link.click();
    }
})