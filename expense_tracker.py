# Topic: Expense Tracker
# Purpose: Create a program to record, manage, and analyze expenses while tracking the remaining budget.
# Concepts: Variables, user input, lists, loops, conditional statements, list methods (append()), sum(), len(), and basic arithmetic.

budget = float(input("Enter your monthly budget: "))
expenses = []  # list to store expenses
a = int(input("Enter the number of expenses you want to record: "))
for i in range(a):
    expense = float(input(f"Enter expense {i + 1}: "))
    expenses.append(expense)