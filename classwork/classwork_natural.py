def addnatural(num):
    sum_num = 0
    n = 1
    while(n <= num):
        sum_num += n
        n = n+1
    return sum_num


num = int(input("Enter a term:: "))
print(addnatural(num))
