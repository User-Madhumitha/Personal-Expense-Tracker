
# Personal Expense Tracker

print("================================")
print("     PERSONAL EXPENSE TRACKER")
print("================================")

income = float(input("Enter your total income: "))

number = int(input("How many expenses do you want to enter? "))

total_expenses = 0
expenses = {}

for i in range(number):

    print("\nExpense", i + 1)

    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))

    total_expenses = total_expenses + amount

    if category in expenses:
        expenses[category] = expenses[category] + amount
    else:
        expenses[category] = amount

savings = income - total_expenses

print("\n========== CATEGORY REPORT ==========")

for category, amount in expenses.items():
    print(category, ":", amount)

print("\n========== FINAL REPORT =============")
print("Total Income:", income)
print("Total Expenses:", total_expenses)
print("Total Savings:", savings)
print("===============================")
