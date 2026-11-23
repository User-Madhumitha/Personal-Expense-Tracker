
import mysql.connector
from getpass import getpass

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=getpass("Enter MySQL password: "),
    database="expense_tracker"
)

cursor = connection.cursor()

category = input("Enter expense category: ")
description = input("Enter expense description: ")
amount = float(input("Enter expense amount: "))
expense_date = input("Enter date (YYYY-MM-DD): ")

query = """
INSERT INTO expenses
(category, description, amount, expense_date)
VALUES (%s, %s, %s, %s)
"""

values = (category, description, amount, expense_date)

cursor.execute(query, values)
connection.commit()

print("Expense added successfully!")

cursor.close()
connection.close()
