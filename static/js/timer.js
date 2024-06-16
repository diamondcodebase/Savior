const remainTime = document.getElementById('remainTime');
const timerContainer = document.getElementById('timer-container');

let countdownInterval;
let allowTimeMinutes = 3;
let countdownTime =  sessionStorage.getItem('countdownTime') || allowTimeMinutes * 60;