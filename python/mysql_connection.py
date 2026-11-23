
import mysql.connector
from getpass import getpass

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=getpass("Enter your MySQL password: "),
        database="expense_tracker"
    )

    if connection.is_connected():
        print("Successfully connected to MySQL!")
        print("Database: expense_tracker")

    connection.close()
    print("Connection closed.")

except mysql.connector.Error as error:
    print("MySQL connection error:", error)
