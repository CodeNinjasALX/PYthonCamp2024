import random

tries = 5
guess_count = 0
num = random.randint(1, 20)
print("You have " + str(tries) + " attempts to guess the right number from 1-20")

while tries > 0:
    guess = int(input("guess a number from 1-20: "))
    guess_count += 1

    if guess > num:
        print("Too high! Guess again.")
    elif guess < num:
        print("Too low! Guess again.")
    else:
        print("Great job! You got it correct in " + str(guess_count) + " guesses.")
        break
    tries -= 1
    print("Incorrect! Go slap yourself with a fish. You have " + str(tries) + " attempts left!")

if tries == 0:
    print("you suck at this, you ran out of tries. i didn't even know it was possible to lose that badly. the number was " + str(num) + ".")