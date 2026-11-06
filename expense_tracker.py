# Topic: Expense Tracker
# Purpose: Create a program to record, manage, and analyze expenses while tracking the remaining budget.
# Concepts: Variables, user input, lists, loops, conditional statements, list methods (append()), sum(), len(), and basic arithmetic.

budget = float(input("Enter your monthly budget: "))
expenses = []  # list to store expenses
for i in range(5):  # loop to get 5 expenses from the user
    expense = float(input("Enter expense amount: "))
    expenses.append(expense)  # add expense to the list 
    
total_expenses = sum(expenses)
remaining_budget = budget - total_expenses

print(f"Total expenses: ${total_expenses:.2f}")
print(f"Remaining budget: ${remaining_budget:.2f}")



## code is in progress