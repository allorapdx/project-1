"""
--------------------------------
Python Web Development Techdegree
Project 1 - Number Guessing Game
Version 1.0
--------------------------------
"""

import random

high_score = []

def start_game():
    #Display a welcome message to the player.
    #TODO: Make the bottom row of stars shift left 1 place
    print('* '*20, '\n  Welcome to the Number Guessing Game!','\n       Can you guess the number?\n','* '*20)

def end_game():
    #Let the player know the game is ending.
    print("\nThanks for playing! Come back soon!\n")

#Start function.
start_game()

#Store a random number from range as the solution and attempts.
random_number = random.randint(1, 10)
number_of_attempts = 0


while True:
    try:
        #Continuously prompt the player for a guess until correct.
        number_selection = int(input("Pick a number between 1 and 10:  "))
        #Add each attempt
        number_of_attempts = number_of_attempts+1
    #Non-number guesses should be handled with an exception.
    except (ValueError,RuntimeError, TypeError, NameError):
        print("This was not a valid guess. Try again!")
    else:
        #Guess is outside the guessing range I should be told to try again.
        if number_selection not in range(1,11):
            print("This guess was not in the game's range. Try again!")
        #If the guess greater than the solution, display to the player "It's higher".
        elif random_number > number_selection:
            print("It's higher")
        # If the guess is less than the solution, display to the player "It's lower". 
        elif random_number < number_selection:
            print("It's lower")
        #Show how many attempts it took them to get the correct number.
        elif random_number == number_selection:
            print("Congratulations! You completed the game in {} attempts!!!".format(number_of_attempts))     
            #Add high score to list
            high_score.append(number_of_attempts)
            #Display high score
            print("\nCurrent HIGH SCORE: {} ".format(min(high_score)))
            play_again = input("Play again and beat the high score?! (Yes/No):")
            #When the player chooses to play the game again, a new random number within the range is chosen each time.
            random_number = random.randint(1, 10)
            number_of_attempts = 0
            if play_again.lower() != "yes":
                break
#When the game ends, an ending message is shown to the player.
end_game()
