function resetTimer() {
  clearInterval(countdownInterval);
  countdownTime = 120;
  updateTimer();
  sessionStorage.removeItem('countdownTime');
  timerContainer.classList.add('hidden');
}

window.onload = (event) => {
    resetTimer();
};