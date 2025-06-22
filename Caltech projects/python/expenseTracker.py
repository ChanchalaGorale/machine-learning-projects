import json

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.budgets = {}
        self.load_expenses()

    def add_expense(self, category, amount, description):
        expense = {
            'category': category,
            'amount': amount,
            'description': description,
            'date': input("Enter date (YYYY-MM-DD): ")
        }
        self.expenses.append(expense)
        self.save_expenses()

    def set_budget(self, category, amount):
        self.budgets[category] = amount
        print(f"Budget for {category} set to {amount}")

    def view_expenses(self):
        for expense in self.expenses:
            print(f"{expense['date']}: {expense['category']} - {expense['description']} - ${expense['amount']}")

    def view_budget(self):
        for category, budget in self.budgets.items():
            total_spent = sum(exp['amount'] for exp in self.expenses if exp['category'] == category)
            print(f"{category}: Budget: ${budget} - Spent: ${total_spent} - Remaining: ${budget - total_spent}")

    def save_expenses(self):
        with open("expenses.json", "w") as file:
            json.dump({'expenses': self.expenses, 'budgets': self.budgets}, file)

    def load_expenses(self):
        try:
            with open("expenses.json", "r") as file:
                data = json.load(file)
                self.expenses = data.get('expenses', [])
                self.budgets = data.get('budgets', {})
        except FileNotFoundError:
            pass

def main():
    tracker = ExpenseTracker()

    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. Set Budget")
        print("3. View Expenses")
        print("4. View Budget")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            category = input("Enter category (Food, Rent, etc.): ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            tracker.add_expense(category, amount, description)
        elif choice == '2':
            category = input("Enter category to set budget: ")
            amount = float(input("Enter budget amount: "))
            tracker.set_budget(category, amount)
        elif choice == '3':
            tracker.view_expenses()
        elif choice == '4':
            tracker.view_budget()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
