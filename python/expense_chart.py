
import mysql.connector
import matplotlib.pyplot as plt
from getpass import getpass

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=getpass("Enter MySQL password: "),
    database="expense_tracker"
)

cursor = connection.cursor()

cursor.execute("""
SELECT category, SUM(amount)
FROM expenses
GROUP BY category
""")

results = cursor.fetchall()

categories = [row[0] for row in results]
amounts = [float(row[1]) for row in results]

plt.figure(figsize=(8, 5))

plt.bar(categories, amounts)

plt.title("Category-wise Expense Analysis")
plt.xlabel("Expense Categories")
plt.ylabel("Amount (Rs.)")

plt.tight_layout()

plt.savefig("screenshots/category_expenses.png")

plt.show()

cursor.close()
connection.close()
