import random

number_to_guess = random.randint(1, 1000000)
user_input = int(input("Type in a number to guess"))

if user_input == number_to_guess:
    print("you got lucky but i can still do better")

else:
    print("My grandma can do better than this, the correct value is " + str(number_to_guess))