radius = float(input("Enter radius of a circle:: "))
pie = 22/7


def area(r):
    area = pie*r**2
    print(area)


def circumference(r):
    circumference = 2*pie*r
    print(circumference)


area(radius)
circumference(radius)
