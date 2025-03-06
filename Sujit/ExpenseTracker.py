import csv
import os

EXPENSE_FILE = "expenses.csv"

# Function to load expenses from file
def load_expenses():
    if not os.path.exists(EXPENSE_FILE):
        return []
    with open(EXPENSE_FILE, "r") as file:
        reader = csv.reader(file)
        return list(reader)

# Function to save expenses to file
def save_expenses(expenses):
    with open(EXPENSE_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(expenses)

# Function to add a new expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = input("Enter amount: ")
    expense = [date, category, amount]
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!\n")

# Function to list all expenses
def list_expenses():
    if not expenses:
        print("No expenses recorded.\n")
        return
    print("Date       | Category  | Amount")
    print("----------------------------------")
    for exp in expenses:
        print(f"{exp[0]:10} | {exp[1]:8} | {exp[2]}")
    print()

# Function to delete an expense
def delete_expense():
    list_expenses()
    if not expenses:
        return
    try:
        index = int(input("Enter the expense number to delete: ")) - 1
        if 0 <= index < len(expenses):
            del expenses[index]
            save_expenses(expenses)
            print("Expense deleted successfully!\n")
        else:
            print("Invalid index!\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Main menu
def main():
    global expenses
    expenses = load_expenses()
    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            list_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()
