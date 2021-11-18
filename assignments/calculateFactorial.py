def computeFactorial(num):
    if num == 0:
        return 1
    else:
        return num*computeFactorial(num-1)


num = int(input("Enter a number:: "))
if num >= 0:
    print(computeFactorial(num))
else:
    print("Invalid input!!! ")
