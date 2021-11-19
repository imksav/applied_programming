def checkOddEven(num):
    if num % 2 == 0:
        return "Even Number"
    return "Odd Number"


num = int(input("Enter a number:: "))
print(checkOddEven(num))
