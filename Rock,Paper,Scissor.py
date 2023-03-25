## Rock, Paper , Scissors ##

import random

## Function For Rock, Paper, Scissors game.

print("Let's Play Rock, Paper, Scissors.")
print("")
def play():
    user = input('Choose your Pick: "r" for Rock, "p" for Paper, "s" for scissor')
    computer = random.choice(['r', 'p', 's'])

    if user == computer:                                                ## Tie Condition
        return "It is a tie."
  
    if is_win(user, computer):                                          ## Win Condition
        return (f'Congrats, you won! Computer chose {computer}')

    return (f'You lost! Computer chose {computer}')                     ## User Loose Condition   

## Win Condition.
def is_win(player, opponent):

    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    
print(play())