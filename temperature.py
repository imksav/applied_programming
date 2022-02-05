def tempDetails(countDay):
    print("Please enter", countDay, "days temperature readings")
    for i in range(1, countDay+1):
        temp = int(input(f'Temperature day {[i]} = '))
        tempList.append(temp)

    print("Temperature Reports")
    for i in tempList:
        if i >= 85:
            print(f'Temperature {i} degree Farhenit Very hot')
        elif i >= 65:
            print(f'Temperature {i} degree Farhenit Pleasant day')
        else:
            print(f'Temperature {i} degree Farhenit Very cold')


countDay = int(input("Enter a number of days:: "))
tempList = []
tempDetails(countDay)
