const remainTime = document.getElementById('remainTime');
const timerContainer = document.getElementById('timer-container');

let countdownInterval;
let allow_time_mins = sessionStorage.getItem("allow_time_mins");
let countdownTime =  sessionStorage.getItem('countdownTime') || allow_time_mins * 60;

function countdown() {
    timerContainer.classList.remove('hidden');
    countdownInterval = setInterval(() => {
      if (countdownTime > 0) {
        countdownTime--;
        updateTimer();
        sessionStorage.setItem('countdownTime', countdownTime);
      } else {     
        clearInterval(countdownInterval); 
        window.location.replace("timesup");
      }
    }, 1000);
  };