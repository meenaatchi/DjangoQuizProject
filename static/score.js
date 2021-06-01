let score= 0;

function checkAnswere(ques) {

    let options = document.getElementsByName(`q${ques}`);
    let selected = document.querySelector('input[type="radio"]:checked');
    let flag = 0;
    console.log (selected);
    options.forEach((opt) => {
        if (opt.classList.contains(`correct${ques}`)) {
            opt.value === selected.value ? flag = 1 : flag = 0;
        }
    } );
    if (flag) {
        document.querySelector(`.q${ques}explain1`).classList.remove('hide');
        score++;
    }
    else {
        document.querySelector(`.q${ques}explain2`).classList.remove('hide');
    }
    document.querySelector(`.options${ques}`).style.pointerEvents = 'none';
    selected.checked = false;
    selected.parentElement.classList.add('mark-this');
}

window.addEventListener('DOMContentLoaded', () => {
    startTimer();
});

let seconds = 0;
let minutes = 0;
let intId;
function startTimer() {
console.log ("afd");
let timer = document.querySelector('.timer');
intId = setInterval(() => {
    if (seconds === 61) {
        seconds = 0;
        minutes++;
    }
    timer.innerHTML = `${minutes} Mins : ${seconds} Secs`;
    seconds++;
}, 1000);
}

function endtest(){
clearInterval(intId);
document.querySelector('.result').style.display = 'block';
document.querySelector('.time').innerText = `${minutes} Minutes : ${seconds-1} Seconds`;
document.querySelector('.mark').innerText = `${score}`;
}


