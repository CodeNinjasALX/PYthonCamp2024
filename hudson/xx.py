import random

number_to_guess = random.randint(1, 10)
user_input = int(input("type in a number to guess!>"))

if user_input ==number_to_guess:
    print("your a god")
else:
    print("bad" + str(number_to_guess))

