def calc_avg(size):
    sum_total = 0
    for i in range(size):
        myList = float(input("Enter a marks (out of 100):: "))
        sum_total = sum_total+myList
    avg = sum_total/size
    return avg


myList = []
size = int(input("Enter a number of subjects:: "))
print(calc_avg(size))
