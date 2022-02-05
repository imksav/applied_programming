import random


def checkMultiple(randomValue):
    if randomValue % 2 == 0:
        for x in range(0, 11):
            print(randomValue, "X", x, "=", randomValue*x)
    elif randomValue % 3 == 0:
        for x in range(0, 11):
            print(randomValue, "X", x, "=", randomValue*x)
    else:
        print("Multiple of other number")


userValue = int(input("Enter a number:: "))
randomValue = random.randint(1, userValue)
checkMultiple(randomValue)
