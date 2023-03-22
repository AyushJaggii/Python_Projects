## Guess The Number (Computer Version): In this game the computer generates a Secret number and the user tries to guess it,
## using the hints provided by the computer that whether the user guess is higher, or lower than the secret number.

import random
def guess(x):

    ## Generating a random number between 1 and x (inclusive)
    random_number = random.randint(1,x)
    guess = 0

    # Looping until guess equals random_number
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}:'))

        # Checking if the guess is less than the random number
        if guess < random_number:
            print('Sorry, guess again. Too low.')

        # Checking if the guess is greater than the random number
        elif guess > random_number:
            print('Sorry, guess again. Too high')
        
    print(f'Congrats, You have guessed the number correctly.The number is {random_number} ')

guess(10)


