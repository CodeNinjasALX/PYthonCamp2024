import random

numbert_to_guess = random.randint(1,10)
user_input = int(input("Type in a number to guess!"))

if user_input == numbert_to_guess:7
    print("Great Job")
 
else:
    print("You suck it is " + str(numbert_to_guess))
                      
