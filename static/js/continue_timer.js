function updateTimer() {
  const minutes = Math.floor(countdownTime / 60);
  const seconds = countdownTime % 60;
  remainTime.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
}

function countdown() {
  timerContainer.classList.remove('hidden');
  countdownInterval = setInterval(() => {
    if (countdownTime > 0) {
      countdownTime--;
      updateTimer();
      sessionStorage.setItem('countdownTime', countdownTime);
    } else {
      clearInterval(countdownInterval);
    }
  }, 1000);

};

window.onload = (event) => {
  countdown();
};

