
import mysql.connector
import csv
from getpass import getpass

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=getpass("Enter MySQL password: "),
    database="expense_tracker"
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM expenses")

records = cursor.fetchall()

with open("excel/expense_report.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Expense ID",
        "Category",
        "Description",
        "Amount",
        "Date"
    ])

    writer.writerows(records)

print("Expense report exported successfully!")

cursor.close()
connection.close()
