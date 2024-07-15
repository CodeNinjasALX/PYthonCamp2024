import random

number_to_guess = random.randint(1,10)
user_input = int(input("type numr to gess  >"))

if user_input == number_to_guess:
    print("noice")
else:
    print("RONG it is" + str(number_to_guess))



