import random
userName = input("Please enter your name:")
randomNum = random.randint(1, 10)
randomNumUser = int(input("Hi " + userName + "Please enter a random number from 1-10 that comes to your mind"))
if (randomNumUser > 10 or randomNumUser < 1):
    print("Enter a number between 1 and 10 please")
elif randomNum == randomNumUser:
    print("Bulls eye! "+ userName+ " You guessed it right")
else:
    print("Better luck next time!")