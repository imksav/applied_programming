def gcd(num1, num2):
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1
    if num1 == num2:
        return num1
    if num1 > num2:
        return gcd(num1-num2, num2)
    else:
        return gcd(num1, num2-num1)


num1 = int(input("Enter first number:: "))
num2 = int(input("Enter second number:: "))
print(gcd(num1, num2))
