const words = [];
//start logic
const startbutton = document.getElementById('start-btn');
const endbutton  = document.getElementById('end');
const start=document.querySelector(".start") 
const end=document.querySelector(".end") 
const game=document.querySelector(".game")
const word=document.querySelector("word");
let hearts= 3;
let currentWord=""
startbutton.addEventListener('click',() => {
    game.classList.remove("hidden")
    start.classList.add("hidden")
    
    word.textContent = words(Math.floor(Math.random()*10))
    word.textContent = currentWord.split('').sort(()=>Math.random()-0.5).join('')
});

endbutton.addEventListener('click',() => {
    game.classList.remove("hidden")
    end.classList.add("hidden")
    
    word.textContent = words(Math.floor(Math.random()*10))
    word.textContent = currentWord.split('').sort(()=>Math.random()-0.5).join('')
});

const guessbutton = document.getElementById('guess-btn');
guessbutton.addEventListener('click',() => {
    const guess = document.getElementById('guess').value;
    if(guess.value === currentWord){
        alert("Correct!");
         
    word.textContent = words(Math.floor(Math.random()*10))
    word.textContent = currentWord.split('').sort(()=>Math.random()-0.5).join('')
    }
    else if(hearts==0){
        alert("Game Over. You lost!");
        game.classList.add("hidden")
        end.classList.remove("hidden")
        hearts= 3;
        word.textContent = ""
        currentWord=""
    } 
    else {
        hearts-= 1;
          
    word.textContent = words(Math.floor(Math.random()*10))
    word.textContent = currentWord.split('').sort(()=>Math.random()-0.5).join('')
        alert("Incorrect!");

    }
});
