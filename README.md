# Personal Expense Tracker

## Project Overview

The Personal Expense Tracker is a Python and MySQL-based application that helps users record, store, manage, and analyze their daily expenses.

It also provides expense summaries, category-wise analysis, Excel-compatible reports, and data visualizations.

## Technologies Used

- Python
- MySQL
- MySQL Connector
- Matplotlib
- Excel / CSV
- Visual Studio Code

## Features

1. Add expense details using Python.
2. Store expense records in MySQL.
3. View all saved expenses.
4. Calculate total expenses.
5. Generate category-wise expense reports.
6. Export expense records to CSV.
7. Visualize expenses using bar charts.
8. Visualize spending percentages using pie charts.

## Project Structure

```text
Personal-Expense-Tracker/
│
├── dataset/
├── excel/
│   └── expense_report.csv
├── python/
│   ├── expense_analysis.py
│   ├── mysql_connection.py
│   ├── add_expense.py
│   ├── view_expenses.py
│   ├── expense_summary.py
│   ├── export_to_csv.py
│   ├── expense_chart.py
│   └── expense_pie_chart.py
├── screenshots/
│   └── category_expenses.png
├── sql/
└── README.md
```

## Database

Database Name: `expense_tracker`

Table Name: `expenses`

The table stores:

- Expense ID
- Category
- Description
- Amount
- Expense Date

## Learning Outcomes

- Python programming and database connectivity.
- SQL queries and data retrieval.
- Data analysis using Python.
- Exporting data to CSV.
- Data visualization using Matplotlib.

## Future Improvements

- Add income tracking.
- Add monthly expense reports.
- Create a graphical user interface.
- Develop a Power BI dashboard.

## Author

B.E. CSE (Data Science) Student
