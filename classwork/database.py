print("""
1. connect() method of the MySQL Connector class with the required arguments to connect MySQL. It would return a MySQLConnection object if the connection established successfully
2. cursor() method of a MySQLConnection object to create a cursor object to perform various SQL operations.
3. execute() methods run the SQL query and return the result.
4. cursor.fetchall() or fetchone() or fetchmany() to read query result.
5. cursor.close() and connection.close() method to close open connections after your work completes
""")

import mysql.connector
from mysql.connector import Error

try:
          conn = mysql.connector.connect(host="localhost", database="pythondatabase", username="root", password="root")
          
          mysql_create_table = """CREATE TABLE irdsystem(id varchar(10), name varchar(250), monthly_salary varchar(250), tax_amount varchar(250), tax_payment_date varchar(250), primary key(id))"""
          cursor = conn.cursor()
          # result = cursor.execute(mysql_create_table)
          print("Table is created successfully!!!")
          usedatabase = cursor.execute("use pythondatabase;")
          sql = "INSERT INTO pythondatabase.irdsystem(id, name, monthly_salary, tax_amount, tax_payment_date) VALUES('25', 'Keshav Bhandari', '18000', '18', '2022-01-15')"
          # val = "'3', 'Keshav Bhandari', '18000', '18', '2022-01-14'"
          result_insert = cursor.execute(sql)
          print(sql)
          
          print(cursor.rowcount ,"Value inserted!!!")
          
except Error as e:
          print("Failed to create table:: {}".format(e))
finally:
          if conn.is_connected():
                    cursor.close()
                    conn.close()
                    print("MySQL connection is closed.")          