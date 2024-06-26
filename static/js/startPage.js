const startButton = document.getElementById('startButton');

startButton.addEventListener('click', () => {
    sessionStorage.setItem('allow_time_mins', 1);
});
