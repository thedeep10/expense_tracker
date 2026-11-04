# Expense Tracker

A command-line expense tracker built in Python with SQLite for persistent storage.

## Features
- Add expenses with amount, category, and date
- View all expenses
- View spending summary grouped by category
- Delete an expense by ID
- Input validation (rejects invalid amounts, negative numbers, and badly formatted dates)
- Data persists between runs using a local SQLite database

## Tech used
- Python 3
- SQLite (via the built-in `sqlite3` module)

## How to run
python tracker.py

## Example

--- Expense Tracker ---

1. Add expense
2. View expenses
3. View summary by category
4. Delete an expense
5. Quit
Choose an option: 1
Amount: 250
Category (food, travel, etc.): food
Date (YYYY-MM-DD, blank for today):
Expense added!


## What I learned
Building this project helped me practice SQL (CREATE TABLE, INSERT, SELECT, DELETE, GROUP BY),
input validation with try/except, and using Git for version control.