import random

attempts = 5
guess_count = 0
secret_number = random.randint(1, 10)

print("you have " + str(attempts) + "left")

while attempts > 0:
    user_input = int(input("guess the number 1-10"))
    guess_count += 1

    if user_input > secret_number:
        print("too high")
    elif user_input < secret_number:
        print("too low")
    else:
        print("correct" + str(guess_count) + "guesses")
        break

    attempts -= 1
    print("wrong!" + str(attempts) + "left")

if attempts == 0:
    print("it was " + str(secret_number))