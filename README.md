# Day12-Number-guessing-game

On Day 12, we built a **Number Guessing Game**.  
The computer picks a number between 1 and 100, and you have to guess it.  
Choose a difficulty level: **easy** gives you more guesses (10 to be exact), **hard** gives you fewer (5 tries).  Your job is to guess the number before your chances run out!

This project was a great way to **practice understanding scope**, manage **global and local variables**, and strengthen **function design** while building a simple interactive game.  

## What We Learned

- **Global vs Local scope** – knowing where a variable lives and who can access it
- **Modifying global variables** inside functions
- **Python constants** – using all-caps variables to signal “don’t change me”
- **Understanding that Python does NOT have block scope** (if/for/while blocks don’t create a new scope)
- How to **pass variables between functions** and maintain state
- Writing **functions** to organize code (`check_answer()`, `set_difficulty()`, `game()`)
- Using **loops** to repeat guesses until the game ends
- Handling **user input** and validating it against the computer’s number


## How the Code Works

- The computer picks a random number between 1 and 100.
- You choose a difficulty level, which sets the number of attempts.
- Each turn, you guess a number:
  - If your guess is too high or too low, the program tells you and decreases your attempts.
  - If you guess correctly, the program congratulates you.
- The game ends when you guess the number or run out of turns.

