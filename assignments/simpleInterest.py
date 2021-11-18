principal = float(input("Enter a principal (in Rs.):: "))
rate = float(input("Enter a rate( in annual):: "))
time = float(input("Enter a time period (in year):: "))


def simpleInterest(p, t, r):
    interest = (p*t*r)/100
    print("Simple Interest ::", interest)


simpleInterest(principal, time, rate)
