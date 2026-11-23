
import mysql.connector
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

print("\n----- PERSONAL EXPENSE REPORT -----")

for record in records:
    print(record)

cursor.close()
connection.close()
