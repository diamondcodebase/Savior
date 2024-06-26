const startButton = document.getElementById('startButton');

startButton.addEventListener('click', () => {
    location.replace("register");
    sessionStorage.setItem('allow_time_mins',allow_time_mins);
});
