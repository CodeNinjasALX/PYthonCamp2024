import random

attempts = 5
guess_count = 0
secret_numbur = random.randint(1, 10)

print("you have" + str(attempts) + "to guess the right numbr 1-10000000000000000000000000000000000000")

while attempts > 0:
    user_input = int(input("guess the numbr 1-10000000000000000000000000000000000000"))
    guess_count += 1

    if user_input > secret_numbur:
        print("to high! guess again")
    elif user_input < secret_numbur:
        print ("to low")
    else:
        print("grat jobs")
        break

    attempts -= 1
    print ("noooo!" + str(attempts ) + "laft")

if attempts == 0:
    print("boo" + str(secret_numbur))