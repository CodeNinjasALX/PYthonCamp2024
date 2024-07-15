import random

attempts = 5
guess_count = 0
secret_number = random.randint(1, 1000)

print("you have " + str(attempts) + " to geuss the right number 1-1000.")

while attempts > 0:
   user_input = int(input("geuss the number 1-1000")) 
   guess_count += 1

   if user_input > secret_number:
      print("Too high! geuss again bozo")
   elif user_input < secret_number:
      print ("Too low geuss again")
   else:
      print("Great job trash player you finnaly got it right you human trash, get a life i know you cant do it again.") + str(guess_count) + " geusses"
      break
   
   attempts -= 1
   print("wrong womp womp go get a life you dumpster fire) you have " + str(attempts) + " left")
   
if attempts == 0:
   
    print("wow your terrible could NEVER BE ME YOUR DOG WATER GO CRY Of course it was " + str(secret_number) + " Try getting good")