import mysql.connector
from mysql.connector import Error


def database_connection(date, degree, status):
    try:
        create_database(hostname, dbname, username, password)
    except Error as e:
        print("Failed to create table:: {}".format(e))

# create database here


def create_database(hostname, dbname, username, password, tablename, date, degree, status):
    try:
        conn = mysql.connector.connect(
            host=hostname, database=dbname, username=username, password=password)
        fire = conn.cursor()
        fire.execute("SHOW TABLES")
        results = fire.fetchall()
        results_list = [item[0]
                        for item in results]  # conversion to list of str
        # print(results_list)
        if tablename in results_list:
            table_found(conn, tablename, date, degree, status)
        else:
            table_not_found(conn, tablename, date, degree, status)
            pass
    except Error as e:
        print("Failed to create table:: {}".format(e))

# if table is found in the database


def table_found(conn, tablename, date, degree, status):
    try:
        sql = "INSERT  INTO  "+tablename + \
            "(day, degree, status) VALUES (%s, %s, %s)"
        data = (date, degree, status)
        fire = conn.cursor()
        fire.execute(sql, data)
        # print(fire.rowcount, "Value inserted!!!")
        conn.commit()
    except Error as e:
        print("Failed to find the table:: {}".format(e))
    pass

# if table is not found in the database


def table_not_found(conn, tablename, date, degree, status):
    try:
        create_table = "CREATE TABLE "+tablename + \
            "(id INT NOT NULL AUTO_INCREMENT, day VARCHAR(10) NULL, degree VARCHAR(10) NULL, status VARCHAR(250) NULL, PRIMARY KEY(id))"
        fire = conn.cursor()
        fire.execute(create_table)
        table_found(conn, tablename, date, degree, status)
        # table_found(fire, tablename=tablename, date=date, degree=degree, status=status)
    except Error() as e:
        print("Failed to find the table:: {}".format(e))


if __name__ == "__main__":
    create_database("localhost", "temp", "root", "root",
                    "tempdata", "10", "10", "Cold")
