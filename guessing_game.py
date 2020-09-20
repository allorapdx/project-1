"""
--------------------------------
Python Web Development
Project 1 - Number Guessing Game
Version 2.0
--------------------------------
"""

import random

high_score = []
number_of_attempts = 0
level = 'easy'
random_number = 0
number_range = '1 and 10'


#Display a welcome message to the player.
def menu():
    print('* '*20)
    print('  Welcome to the Number Guessing Game!')
    print('       Can you guess the number?')
    print('* '*20)


#Player selected difficulty.  
def difficulty():
    global level
    while True:
        try:
            level = input('\nEasy / Medium / Hard \n\nSelect Difficulty: ')
        except (ValueError,RuntimeError, TypeError, NameError):    
            print('The selection was not a valid option.')
        else:
            if (level.lower() == 'easy' or level.lower() == 'medium' or level.lower() == 'hard' ):
                number()
                break
            else:
                print('The selection was not a valid option.')


#Select random number for player.
def number():
    global random_number
    global number_range
    random_number = 0
    if level == 'easy':
        random_number = random.randint(1, 10)
        number_range = '1 and 10'
    elif level == 'medium':
        random_number = random.randint(1, 100)
        number_range = '1 and 100'
    elif level == 'hard':
        random_number = random.randint(1, 1000)
        number_range = '1 and 1000'
    start_game()    


#The guessing game!
def start_game():
    global number_of_attempts
    global random_number
    number_of_attempts = 0
    while True:
        try:
            number_selection = int(input("Pick a number between {}:  ".format(number_range)))
            number_of_attempts = number_of_attempts+1
        except (ValueError,RuntimeError, TypeError, NameError):    
            print("This was not a valid guess. Try again!")
        else:
            if number_selection not in range(1,1001):
                print("This guess was not in the game's range. Try again!")
            elif random_number > number_selection:
                print("It's higher")
            elif random_number < number_selection:
                print("It's lower")
            elif random_number == number_selection:
                print("Congratulations! You completed the game in {} attempts!!!".format(number_of_attempts))
                score()
                end_game()
                break

                
#Updates and displays players high score.
def score():
    global number_of_attempts
    high_score.append(number_of_attempts)
    print("\n* * * Current {} HIGH SCORE: {} * * * \n".format(level.capitalize(), min(high_score)))


#Display a continue message or goodbye message to the player.
def end_game():
    play_again = input("Play again and beat the high score?! (Yes/No):")
    if play_again.lower() == "yes":
        number()
    else:
        print("\nThanks for playing! Come back soon!\n")


menu()
difficulty()
