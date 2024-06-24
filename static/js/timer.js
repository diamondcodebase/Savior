const remainTime = document.getElementById('remainTime');
const timerContainer = document.getElementById('timer-container');

let countdownInterval;
let allowTimeMins = sessionStorage.getItem("allowTimeMins");
let countdownTime =  sessionStorage.getItem('countdownTime') || allowTimeMins * 60;