# 💸 Expense Analyzer

A simple Python tool that reads a bank statement CSV and shows where your money goes.

Built as my first project after completing my Python course at NIAT, Pune.

## Features

- Reads transactions from a CSV file
- Auto-categorizes spending (Food, Travel, Shopping, etc.) using keywords
- Shows total spending by category and by month
- Lists the top 3 categories and top 5 biggest expenses
- Flags unusual spends (more than 2x the average)
- Saves a summary report to `report.csv`

## Concepts Used

Dictionaries, lists, loops, functions, `csv`, `datetime`, `collections.defaultdict`, sorting, file handling

## How to Run

1. Make sure Python 3 is installed
2. Download or clone this repository
3. Keep `main.py` and `transactions.csv` in the same folder
4. Run:

```
python3 main.py
```

## Sample Data Format

```
date,description,amount
2026-10-01,Swiggy order,450
2026-10-02,Uber ride,230
```

The included `transactions.csv` is **demo data only**.

## Using Your Own Statement

Banks use different column names and date formats. Change these lines in `main.py` to match your file:

- the file name in `open(...)`
- the column names (`row["Date"]`, `row["Details"]`, `row["Debit"]`)
- the date format in `strptime(...)`

## Future Improvements

- Compare each spend with its own category's average
- Add charts
- Add more categories

## Author

Swarup,a Python learner 🫡
