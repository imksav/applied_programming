num = int(input("Enter a number:: "))
sum = 0
while num > 0:
    rem = num % 10
    if rem % 2 == 0:
        print(rem, " is an even number.")
    else:
        print(rem, " is an odd number.")
    sum = sum+rem
    num = num//10
print(sum)
# =========================================
# num1 = int(input("Enter a number:: "))
# sum = 0
# rem1 = num1 % 10
# sum1 = sum+rem1
# num2 = num1/10
# rem2 = num2 % 10
# sum2 = sum1+rem2
# num3 = num2/10
# rem3 = num3 % 10
# sum3 = sum2+rem3
# num4 = num3/10
# print("The sum of num1 is", sum3)
# =======================================
# num1 = (input("Enter a number:: "))
# sum1 = int(num1[0])+int(num1[1])+int(num1[2])
# print(sum1)
