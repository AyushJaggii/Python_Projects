## Guess The Number (User Version): In this game the user Thinks of a Secret number and the computer tries to guess it,
## using the hints provided by the user that whether the computer guess is higher, or lower than the secret number.

import random
def computer_guess(x):

    ## Initialize the low and high limits for the computer's guess
    low = 1
    high = x

    ## Initialize the feedback from the user
    feedback_to_computer = ''

    # Keep looping until the computer guesses the correct number
    while feedback_to_computer != 'c':
        if high != low:
            guess = random.randint(low, high)
        else:
            guess = low  ## or high because loww = high
            
        # Ask the user for feedback on the computer's guess
        feedback_to_computer = input(f'Is {guess} too high (H),too Low (L),too correct (C).').lower()

        # If the guess is too high, adjust the high limit for the next guess
        if feedback_to_computer == 'h':
            high = guess - 1
        # If the guess is too low, adjust the low limit for the next guess
        elif feedback_to_computer == 'l':
            low = guess + 1

    print(f'Congrats, The Computer Guessed your number,{guess} correctly.')
    
computer_guess(10000)