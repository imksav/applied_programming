def calc_average(size):
    sum = 0
    for i in range(size):
        marks = int(input("Enter a marks:: "))
        sum += marks
        avg = sum/size
    return avg


size = int(input("Enter a size:: "))
marks = []
print(calc_average(size))
