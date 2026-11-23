# Personal Expense Tracker

A Python and MySQL-based application to record, manage, and analyze personal expenses.

## Project Overview

The Personal Expense Tracker helps users store daily expenses, view transaction records, analyze spending patterns, and generate reports.

## Technologies Used

- Python
- MySQL
- Pandas
- Matplotlib
- Excel / CSV
- Git and GitHub

## Features

- Add new expenses
- View all expense records
- Calculate total expenses
- Generate expense summaries
- Analyze category-wise spending
- Create bar charts and pie charts
- Export expense reports to CSV

## Project Structure

```text
Personal-Expense-Tracker/
│
├── dataset/
├── excel/
│   └── expense_report.csv
├── python/
│   ├── add_expense.py
│   ├── expense_analysis.py
│   ├── expense_chart.py
│   ├── expense_pie_chart.py
│   ├── expense_summary.py
│   ├── export_to_csv.py
│   ├── mysql_connection.py
│   └── view_expenses.py
├── screenshots/
├── sql/
├── .gitignore
└── README.md
```

## Database

Database name: `expense_tracker`

Table name: `expenses`

The database stores expense categories, descriptions, amounts, and dates.

## How to Run

1. Install Python.
2. Install MySQL Server.
3. Install the required Python libraries:

```bash
pip install mysql-connector-python pandas matplotlib
```

4. Configure your MySQL connection.
5. Open the project folder in VS Code.
6. Run the Python files from the terminal.

Example:

```bash
python python/add_expense.py
```

## Output

The project generates:

- Expense summaries
- Category-wise analysis
- Bar charts
- Pie charts
- CSV expense reports

## Author

GitHub: [User-Madhumitha](https://github.com/User-Madhumitha)

## Project Status

Completed initial version. Further improvements are planned.
