const startButton = document.getElementById('startButton');

startButton.addEventListener('click', () => {
    location.replace("register");
    sessionStorage.setItem('allowTimeMins',allowTimeMins);
});
