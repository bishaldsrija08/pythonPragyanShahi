import matplotlib.pyplot as plt
expenses = []

def add_expense():
    category = input("Enter the category of the expense (Food, Transport, Entertainment etc): ")
    amount = float(input("Enter the amount of the expense: "))
    date = input("Enter the date of the expense (YYYY-MM-DD): ")
    expenses.append({
        "category": category,
        "amount": amount,
        "date": date
    })
    print("Expense added successfully!")
    
for _ in range(3): # Allow the user to add three expenses
    add_expense()

for expense in expenses:
    print(f"Category: {expense['category']}, Amount: {expense['amount']}, Date: {expense['date']}")

# Generate a monthly summary of expenses
from collections import defaultdict # to create a dictionary that defaults to 0 for any new category

category_totals = defaultdict(float)
for expense in expenses:
    category_totals[expense['category']] += expense['amount']
    
print("\nMonthly Summary of Expenses:")
for category, total in category_totals.items():
    print(f"{category}: {total:.2f}")

# Generate a bar chart of expenses by category

categories = list(category_totals.keys())
totals = list(category_totals.values())

plt.bar(categories, totals)
plt.xlabel('Category')
plt.ylabel('Total Expenses')
plt.title('Total Expenses by Category')
plt.show()