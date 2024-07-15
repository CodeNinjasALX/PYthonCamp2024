import random 

attempts =  5
guess_count = 0
secret_number = random.randint(1, 10)

print("You have " + str(attempts) + " to guess the right number 1-10.")

while attempts > 0:
    user_input = int(input("Guess the number 1-10"))
    guess_count += 1

    if user_input > secret_number:
        print("Too high! Guess agian" )
    elif user_input > secret_number:
        print("Too low! Try again")
    else: 
        print("Great job! You got it correct in " + str(guess_count)+ "guesses")
    attempts -= 1
    print("Wrong you have " + str(guess_count) )


if attempts == 0:
    ("You suck It was actually" + str(secret_number))

        

