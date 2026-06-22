expenses: list[dict] = []

def add_expense() -> None:
    amount = float(input("Amount: $"))
    category = input("Category: ")
    description = input("Description: ")
    expenses.append({"amount": amount, "category": category, "description": description})
    print(f"✓ Added {description} (${amount}) [{category}]\n")

def list_expenses() -> None:
    if not expenses:
        print("No expenses yet.\n")
        return
    for e in expenses:
        print(f"  {e['category']}: {e['description']} — ${e['amount']}")
    print()

def total() -> None:
    print(f"Total: ${sum(e['amount'] for e in expenses):.2f}\n")

def main() -> None:
    while True:
        print("1. Add expense")
        print("2. List expenses")
        print("3. Show total")
        print("4. Quit")
        choice = input("Choose: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            list_expenses()
        elif choice == "3":
            total()
        elif choice == "4":
            break
        else:
            print("Invalid choice\n")

main()