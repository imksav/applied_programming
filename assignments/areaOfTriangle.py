breadth = float(input("Enter a breadth (in m):: "))
height = float(input("Enter a height (in m):: "))


def area(b, h):
    area = (1/2)*b*h
    print(area, "square meter")


area(breadth, height)
