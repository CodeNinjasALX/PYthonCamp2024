import random

attempts = 5
guess_count = 0
secret_number = random.randint(1, 5)

print("You have " + str(attempts) + " to guess the right number 1-100.")

while attempts > 0:
    user_input = int(input("Guess the number 1-100"))
    guess_count += 1

    if user_input > secret_number:
        print("Too high! Try again")
    elif user_input < secret_number:
        print("Too low! Try again")
    else:
        print("Good job! You got it correct in " + str(guess_count) + " guesses")
        break

    attempts -= 1
    print("You got it wrong, you have " + str(attempts) + " left!")

if attempts == 0:
    print("YOU SUCK MY GRANDMA BETTER THAN YOU, it actually was " + str(secret_number) + " GO GET A JOB and try again")