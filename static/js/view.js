const enterButton = document.getElementById('enterBtn');
const mins = document.getElementById('mins');

enterButton.addEventListener('click', () => {
    location.replace("0");
    sessionStorage["allow_time_mins"] = mins.innerHTML;
});
