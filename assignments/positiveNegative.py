def checkPositiveNegative(num1):
    if(num1 > 0):
        return "Positive Number"
    elif (num1 < 0):
        return "Negative Number"
    else:
        return "Zero"


num1 = int(input("Enter a number:: "))
print(checkPositiveNegative(num1))
