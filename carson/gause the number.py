import random

number_to_guess = random.randint(1, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
user_input = int(input("type a number to geuss! >"))

if user_input == number_to_guess:
    print("great job dude!")
else:
    print("wrong! " + str(number_to_guess) + " is the correct number")