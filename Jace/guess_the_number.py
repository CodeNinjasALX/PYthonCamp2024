import random

number_to_guess = random.randint(1, 100)
user_input = int(input("Type in a number to guess! >"))

if user_input == number_to_guess:
    print("I bet my dog Joe Biden on this!")
else:
    print("You suck at guessing, your grandma will now break her legs, the correct value is " + str(number_to_guess))
    print("Get a wig, hohoho, from santa.")