"""
? LETTER COUNTER PROJECT:

1. Print a welcome message to the user.
2. Take a string and a letter from the user.
3. Count how many times the letter occured.
4. percentage of letter in the string.
5. Show the output to the user.
"""

## Print a welcome message to the user.
print("Welcome to LETTER COUNTER. This application will ask for a Message and a letter and,"
        "will then calcuate the no. of times letter occured in the string and also its percentage.")

## Getting User inputs:
user_message = input("Please Enter a Message.")
user_letter = input("Please enter the Letter")

## Count the number of occureneces:
count = user_message.count(user_letter)

## Percentage:
length_message = len(user_message)
letter_percentage = (count/length_message)*100 

## Printing the Output:
print("The number of occurences of letter", user_letter, "is", count)
print("The Percentage of letter", user_letter, "in", user_message, "is", letter_percentage)