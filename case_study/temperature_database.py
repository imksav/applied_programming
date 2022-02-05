import mysql.connector
from mysql.connector import Error
from database import *


class temperature_database:
    # constructor
    def __init__(self, date, degree):
        self.date = date
        self.degree = degree

    # checking condition to get the report of the temperature
    def conditionStatus(self, temp, count_hot, count_pleasant, count_cold):
        if temp > 85:
            count_hot = count_hot + 1
            return "Very Hot", count_hot, count_pleasant, count_cold
        elif temp > 60:
            count_pleasant = count_pleasant + 1
            return "Very Pleasant", count_hot, count_pleasant, count_cold
        else:
            count_cold = count_cold + 1
            return "Very Cold", count_hot, count_pleasant, count_cold

    # database connection
    def display(self, status, tempList, hostname, dbname, username, password, tablename):
        for i in range(1):
            print(
                f"Temperature day[{self.date}] = {self.degree} Celcius {status}.")
            create_database(hostname, dbname, username, password,
                            tablename, self.date, self.degree, status)


# main function
if __name__ == "__main__":
    num_records = int(input("How many days to record?::"))
    tempList = []
    total_temp = 0
    count_hot = 0
    count_pleasant = 0
    count_cold = 0
# database details input
    hostname = input("Enter your host name:: ")
    dbname = input("Enter your database name:: ")
    username = input("Enter your username:: ")
    password = input("Enter your password:: ")
    tablename = input(("Enter your table name:: "))
    # user input
    print(
        f"-------------------Please enter {num_records} days temperature readings-------------------\n")
    for i in range(1, num_records + 1):
        temp = float(input(f"Temperature of day[{i}] = "))
        tempList.append(temp)
    print("-" * 10, "Temperature Status", "-" * 10)
    # passing to the functions to display the result and insert into database
    for i in range(len(tempList)):
        t1 = temperature_database(i + 1, tempList[i])
        condition_status, count_hot, count_pleasant, count_cold = t1.conditionStatus(
            tempList[i], count_hot, count_pleasant, count_cold)
        t1.display(condition_status, len(tempList), hostname,
                   dbname, username, password, tablename)
        total_temp = total_temp + int(tempList[i])
    print("The average Temp for", num_records,
          " days =", (total_temp/num_records), "Celcius.")
    print("Number of hot days = ", count_hot, " day/s.")
    print("Number of pleasant days = ", count_pleasant, " day/s.")
    print("Number of cold days = ", count_cold, " day/s.")
