import random
num = random.randint(1, 10)
guess = int(input("guess the number: "))
if num == guess:
    print("correct!")
else:
    print("I don't think i have ever seen someone as intellectually lost as you,\n get a job you suck you have no life i have better things to do than speak to you. the number was: " + str(num) + ".")