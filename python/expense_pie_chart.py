
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

plt.figure(figsize=(7, 7))

plt.pie(
    amounts,
    labels=categories,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Category-wise Spending Percentage")
plt.savefig("screenshots/expense_pie_chart.png")
plt.show()

cursor.close()
connection.close()
