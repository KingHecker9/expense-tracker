expenses: list[dict] = []

def add_expense(amount: float, category: str, description: str) -> None:
    expenses.append({
        "amount": amount,
        "category": category,
        "description": description
    })
    print(f"Added: {description} (${amount}) [{category}]")

def list_expenses() -> None:
    if not expenses:
        print("No expenses yet.")
        return
    for e in expenses:
        print(f"  {e['category']}: {e['description']} — ${e['amount']}")

def total() -> None:
    print(f"Total: ${sum(e['amount'] for e in expenses):.2f}")

# Test it
add_expense(20.0, "food", "lunch")
add_expense(5.5, "transport", "bus fare")
list_expenses()
total()