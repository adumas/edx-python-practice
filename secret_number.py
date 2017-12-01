#!/usr/bin/python

"""
Guess a secret number 1-100 using bisection search

Please think of a number between 0 and 100!
Is your secret number 50?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.
"""


print("Please think of a number between 0 and 100!")
high = 100
low = 0

while high > low:
    guess = low + (high - low) / 2
    print("Is your secret number " + str(guess) + "? ")
    result = raw_input(
        "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.  ")

    if result == 'h':
        high = guess
    elif result == 'l':
        low = guess
    elif result == 'c':
        break

print("Game over. Your secret number was: " + str(guess))
