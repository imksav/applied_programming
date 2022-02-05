import mysql.connector
from mysql.connector import Error

# constructor
class temperature_database:
    def __init__(self, date, degree):
        self.date = date
        self.degree = degree

    # checking condition to get the report of the temperature
    def conditionStatus(self, temp):
        if temp > 85:
            return "Very Hot"
        elif temp > 65:
            return "Very Pleasant"
        else:
            return "very Cold"

    # database connection
    def display(self, status):
        try:
            conn = mysql.connector.connect(
                host="localhost", database="temp", username="root", password="root"
            )
            mysql_create_table = """CREATE TABLE tempdata1(id INT NOT NULL AUTO_INCREMENT, day VARCHAR(10) NULL, degree VARCHAR(10) NULL, status VARCHAR(250) NULL, PRIMARY KEY(id))"""
            cursor = conn.cursor()
            print(f"Temperature of day[{self.date}] is {self.degree} ℉. It's {status}.")
            sql = "INSERT  INTO  tempdata1(day, degree, status) VALUES (%s, %s, %s)"
            data = (self.date, self.degree, status)
            cursor.execute(sql, data)
            print(cursor.rowcount, "Value inserted!!!")
            conn.commit()
        except Error as e:
            print("Failed to create table:: {}".format(e))


# main function
if __name__ == "__main__":
    num_records = int(input("Enter the number of record you want to insert::"))
    tempList = []
    # user input
    print(f"==========Enter the temperature of {num_records} days==========\n")
    for i in range(1, num_records + 1):
        temp = float(input(f"Temperature of day[{i}]::"))
        tempList.append(temp)
    print("=" * 10, "Temperature Status", "=" * 10)
    # passing to the functions to display the result and insert into database
    for i in range(len(tempList)):
        t1 = temperature_database(i + 1, tempList[i])
        condition_status = t1.conditionStatus(tempList[i])
        t1.display(condition_status)
