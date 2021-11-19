def gcd(num1, num2):
    if(num1 == 0):
        return num2
    else:
        return gcd(num2 % num1, num1)


def lcm(num1, num2):
    return (num1/gcd(num1, num2)*num2)


num1 = int(input("Enter first number:: "))
num2 = int(input("Enter second number:: "))
print(lcm(num1, num2))
