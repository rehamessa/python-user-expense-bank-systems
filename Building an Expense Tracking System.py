#--------------------------------------------------------
# Simulated database
#--------------------------------------------------------

expenses = []

#---------------------------------------------------------
# Add Expense Function
#---------------------------------------------------------

def add_expense(amount: float, category: str, description: str) -> dict:

    if amount <= 0:
        raise ValueError("The amount is invalid")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)

    return expense


#--------------------------------------------------------------
# Calculate Total Expenses
#---------------------------------------------------------------

def calculate_total_expenses() -> float:

    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


#----------------------------------------------------------------------
# Calculate Total by Category
#----------------------------------------------------------------------

def calculate_total_by_category(category: str) -> float:

    total = 0

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            total += expense["amount"]

    return total


#----------------------------------------------------------------------
# Show All Expenses
#----------------------------------------------------------------------

def show_expenses() -> None:

    if not expenses:
        print("No expenses recorded.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['category']} - "
            f"{expense['description']}: ${expense['amount']}"
        )


#----------------------------------------------------------------------
# Test section
#----------------------------------------------------------------------

def run_test() -> None:

    try:
        add_expense(50, "Food", "Groceries")
        add_expense(20, "Transport", "Taxi")
        add_expense(0, "Investment", "Thndr")  # Invalid Example

    except ValueError as error:
        print("Error:", error)

    print("\nTotal Expenses:", calculate_total_expenses())

    print(
        "\nTotal Expenses by category:",
        calculate_total_by_category("Food")
    )

    show_expenses()


if __name__ == "__main__":
    run_test()