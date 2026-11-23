
import mysql.connector
from getpass import getpass

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=getpass("Enter MySQL password: "),
    database="expense_tracker"
)

cursor = connection.cursor()

# Calculate total expenses
cursor.execute("SELECT SUM(amount) FROM expenses")
total = cursor.fetchone()[0]

print("\n----- EXPENSE SUMMARY -----")
print("Total Expenses: Rs.", total)

# Category-wise expense analysis
cursor.execute("""
SELECT category, SUM(amount)
FROM expenses
GROUP BY category
""")

results = cursor.fetchall()

print("\n----- CATEGORY-WISE EXPENSES -----")

for category, amount in results:
    print(category, ":", "Rs.", amount)

cursor.close()
connection.close()
