print("Please enter 2 random numbers:")
userNum1 = int(input("Number 1:"))
userNum2 = int(input("Number 2:"))
print(" Please select any of the below based on the calculation you wish to perform:")
print("a for Addition")
print("b for Subtraction")
print("c for Division")
print("d for Multiplication")
print("e for Square (to the power of)")

userOperator = input("Please enter a value from the above operator:")

if (userOperator == "a"):
    print("The output of your calculation is: " + str(userNum1 + userNum2))
elif (userOperator == "b"):
    print("The output of your calculation is: " + str(userNum1 - userNum2))
elif (userOperator == "c"):
    print("The output of your calculation is: " + str(userNum1 / userNum2))
elif (userOperator == "d"):
    print("The output of your calculation is: " + str(userNum1 * userNum2))
elif (userOperator == "e"):
    print("The output of your calculation is: " + str(userNum1 ** userNum2))
else:
    print("Please enter a valid value between a-e next time.")

