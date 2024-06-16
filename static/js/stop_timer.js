function resetTimer() {
  clearInterval(countdownInterval);
  countdownTime = 300;
  updateTimer();
  sessionStorage.removeItem('countdownTime');
  timerContainer.classList.add('hidden');
}

window.onload = (event) => {
    resetTimer();
};