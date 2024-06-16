// Get the buttons container, the exit button and the score count
const btnContainer = document.getElementById('buttons-container');
const exitBtn = document.getElementById('exitBtn');
const scoreDisplay =  document.getElementById('scoreDisplay');
const scoreCount = document.getElementById('scoreCount');

// set checkpoints and victoryScore
const checkpoints = [0,40]; //[0, 7, 11, 15, 21, 23, 27, 30, 31, 35, 37, 40, 45];
const victoryScore = 50;

// Initialize the score count to 0
let score = 0;

// Set target Button
let tgtButton = null;

// Generate and display 4 buttons
for (let i = 1; i <= 4; i++) {
    const button = document.createElement('button');
    button.textContent = `${i}`;
    button.classList.add('button');
    button.addEventListener('click', handleButtonClick);
    btnContainer.appendChild(button);
}

// // Add event listener for exit button
// exitBtn.addEventListener('click', () => {
//     location.replace("san");
// });;

// Start the game
swapButtons();


// Function to handle button click
function handleButtonClick(event) {
    const button = event.target;
    if (button === tgtButton) {
        score++;
        scoreCount.innerHTML = `${score}`;  
        scoreDisplay.style.fontSize = adjustFontSize(score) + "px";    
    }
    else {
        // randomize the deduction
        const deduct = Math.floor(Math.random() * 3);
        score -= deduct;
        scoreCount.innerHTML = `${score}`;  
    }
    swapButtons();
}

// Function to change score font size
function adjustFontSize(score){
    if(score < 5){
        return 20;
    }
    else if(score < 10){
        return 24;
    }
    else if(score < 15){
        return 28;
    }
    else if(score < 20){
        return 32;
    }
    else if(score < 25){
        return 36;
    }
    else if(score < 30){
        return 40;
    }
    else if(score < 35){
        return 44;
    }
    else if(score < 40){
        return 48;
    }
    else if(score < 45){
        return 52;
    }
    else{
        return 56;
    }
}

// Function to swap button positions
function swapButtons() {
    // if score reach the victory score, hidden buttons and show exit
    if(score >= victoryScore){
        btnContainer.style.display = 'none';
        exitBtn.style.display = 'block';
    }

    if(!checkpoints.includes(score)){
        return;
    }

    // Get all the buttons
    const buttons = Array.from(btnContainer.children);
    for(let i = 0; i <= 3; i++){
        if(buttons[i].classList.contains('highlight')){
            buttons[i].classList.remove('highlight');
        }        
    }

    // Randomly select two buttons to swap
    const index1 = Math.floor(Math.random() * buttons.length);

    // Set the new current button
    tgtButton = buttons[index1];
    tgtButton.classList.add('highlight');
  }

 