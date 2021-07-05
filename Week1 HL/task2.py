userName = input("Please enter your name:")
randomNumUser = int(input("Hi " + userName + " Please enter a random number from 1-100 that comes to your mind."))
print("Here's your joke of the day:")
if randomNumUser < 1 or randomNumUser > 100:
    print("You get no jokes. The number should be between 1 and 100.")
elif randomNumUser >= 1 and randomNumUser < 50:
    print("I went to buy some camo pants but couldn’t find any.")
elif randomNumUser >=50 and randomNumUser <=70:
    print("I failed math so many times at school, I can’t even count.")
else:
   print("I used to have a handle on life, but then it broke.")