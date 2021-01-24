import mysql.connector
from mysql.connector import Error
import pandas as pd

PASSWORD = "Sep-0528"
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful.")
    except Error as e:
        print(f"The error '{e}' has occurred.")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful.")
    except Error as e:
        print(f"The error '{e}' has occurred.")

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' has occurred.")

def execute_list_query(connection, sql, val):
    cursor = connection.cursor()
    try:
        cursor.executemany(sql, val)
        connection.commit()
        print("Query successful.")
    except Error as e:
        print(f"The error '{e}' has occurred.")

# def create_database(connection, query):
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         print("Database created successfully.")
#     except Error as e:
#         print(f"The error '{e}' has occurred.")
#
# create_database_query = "CREATE DATABASE school"
# create_database(connection, create_database_query)


