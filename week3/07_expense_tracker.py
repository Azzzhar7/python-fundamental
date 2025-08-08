# Mini Project: Expense Tracker

FILENAME = "expenses.csv"

import csv

def add_expense(name, amount):
    with open(FILENAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, amount])
    print("Expense added.")

def view_expenses():
    try:
        with open(FILENAME, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No expenses found.")

while True:
    print("\n1. Add Expense\n2. View Expenses\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Expense name: ")
        amount = input("Amount: ")
        add_expense(name, amount)
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        break
    else:
        print("Invalid choice.")
