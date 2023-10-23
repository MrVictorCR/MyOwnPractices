"""
    Welcome to GuessTheNumber.py
        In this case it would be a program to guess a number, it would be between 1:100
        If you fail it would display a message, that would say:
            The number is greater: If the number to guess is greater the one that you typed
            or 
            The number is less: If the number to guess is less than the one that you typed

        I would practice:
            While Loop and I'm going to import Random to get the random number
"""

#- Import Random -#

import random

#-----------------#

#- Random Number Creation -#

guessNum = random.randint(0, 100)

#--------------------------#

#- Main Program -#

print("\t.: Guess The Number :.\n")

# Count var: To save the attempts
count = 0

# Bucle para revisar si el número digitado es mayor o menor al número random
while True:

    try: 
        num = int(input("Type a Number: "))
        

        count += 1
        if num > guessNum:
            print("The number is less, Type another one...\n")
        elif num < guessNum:
            print("The number is greater, Type another one...\n")
        elif guessNum == num:
            print(f"\nCongratulations, you guess the number: {guessNum}\n")
            print(f"\tAttempts: {count}\n")
            break

    except ValueError as UnexpectedNumber:
        print("Error -> The option should be a digit, please try again")
    
#---------------#

#-    E n d    -#
