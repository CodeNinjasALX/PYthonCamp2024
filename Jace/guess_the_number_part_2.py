import random

attempts = 5
guess_count = 0
secret_number = random.randint(1, 20)

print("You have " + str(attempts) + " to guess the right number 1-20.")

while attempts > 0:
    user_input = int(input("Guess the number 1-20"))
    guess_count += 1

    if user_input > secret_number:
        print("Too high! Use logic")
    elif user_input < secret_number:
        print("Too low! the same as your life")
    else:
        print("Great Job! You did something right for once, you got it correct in " + str(guess_count) + "guesses")
    break

    attempts -= 1
    print("Wrong!!! You have no reason to not be in a hospital. You have " + str(attempts) + "  Left!" )

if attempts == 0:
    print("YOU SUCK!!! THE NUMBER IS " + str(secret_number) + "YOU SMOOTH BRAIN")