function updateTimer() {
    const minutes = Math.floor(countdownTime / 60);
    const seconds = countdownTime % 60;
    remainTime.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
  }

function startTimer() {    
    timerContainer.classList.remove('hidden');
    clearInterval(countdownInterval);
    countdownTime = sessionStorage.getItem("allow_time_mins") * 60;
    updateTimer();
    sessionStorage.removeItem('countdownTime');
}

window.onload = (event) => {
    startTimer();
    countdown();
};