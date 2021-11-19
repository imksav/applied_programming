def checkOddEven(n):
    if n % 2 != 0:
        print("Odd")
    else:
        print("Even")
        s = 0
        num2 = 5
        while(s < 100):
            s = s+num2
            print(s)


num1 = int(input("Enter a number:: "))
checkOddEven(num1)
