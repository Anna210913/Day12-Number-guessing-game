from random import randint
from myart import logo

#create global constants for setting difficulty level
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


#Create a function to guess user's guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess and returns the number of turns remaining"""
    if user_guess > actual_answer:
        print("Too high, guess again")
        return turns -1
    elif user_guess < actual_answer:
        print("Too low, guess again")
        return turns -1
    elif user_guess == actual_answer:
        print(f"You got it right, good job! The answer was {actual_answer}")
"""you could also use else:print('you got it right') since there is no other choice."""

# We need to make a function that sets difficulty level and chooses number of attempts
def set_difficulty():
    level = input("Choose a difficulty level. Type 'easy' or 'hard':")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    #Choose a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    answer = randint(1,100)
    #print(f"Hint: The correct answer is {answer}")

    turns = set_difficulty()

    guess =0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        #Input to let the number guess that number
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("Oops you've run out of guesses. You lose!")
            print(f"The correct answer is {answer}")
            return
        """since this is all a function we use return to exit the function thereby ending the game"""


game()
#How to track number of turns user takes and reduce by 1 if they get something wrong


