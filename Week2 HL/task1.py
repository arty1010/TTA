userName = input("Please enter your name:")
print("Hi " + userName + " Please enter your menu option.")
userMain = input("Enter a for burger or b for wrap?")

if (userMain == "a"):
    userSide = input("Enter a for french fries or b for no sides")
    if (userSide == "a"):
        print("Here is your burger with french fries on the side")
    else:
        print("Here is your burger with no sides")
elif (userMain == "b"):
    userSide = input("Enter a for salad or b for no sides")
    if (userSide == "a"):
        print("Here is your wrap with salad on the side")
    else:
        print("Here is your wrap with no sides")
else:
    print("Wrong option - please try again.")
