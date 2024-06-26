const remainTime = document.getElementById('remainTime');
const timerContainer = document.getElementById('timer-container');

let countdownInterval;
let allow_time_mins = sessionStorage.getItem("allow_time_mins");
let countdownTime =  sessionStorage.getItem('countdownTime') || allow_time_mins * 60;