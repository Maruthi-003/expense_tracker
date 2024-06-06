expenses = []
expense1 = {'amount': '51.00', 'category': 'shirt'}
expenses.append(expense1)
expense2 = {'amount': '21.55', 'category': 'groceries'}
expenses.append(expense2)

def removeExpense():
    while True:
        listExpenses()
        print("What Expense would you like to remove? (Enter the number)")
        try:
            expenseToRemove = int(input("> "))
            if 0 <= expenseToRemove < len(expenses):
                del expenses[expenseToRemove]
                break
            else:
                print("Invalid input. Please enter a valid expense number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def addExpense(amount, category):
    expense = {'amount': amount, 'category': category}
    expenses.append(expense)

def printMenu():
    print("Please choose from one of the following options...")
    print("1. Add A New Expense")
    print("2. Remove An Expense")
    print("3. List All Expenses")
    print("4. Exit")

def listExpenses():
    print("\nHere is a list of your expenses...")
    print("------------------------------------")
    for index, expense in enumerate(expenses):
        print(f"# {index} - {expense['amount']} - {expense['category']}")
    print("\n")

while True:
    ### Prompt The User
    printMenu()
    optionSelected = input("> ")

    if optionSelected == "1":
        print("How much was this expense?")
        while True:
            amountToAdd = input("> ")
            try:
                float(amountToAdd)  # Check if it can be converted to a float
                break
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        
        print("What category was this expense?")
        category = input("> ")
        addExpense(amountToAdd, category)

    elif optionSelected == "2":
        removeExpense()

    elif optionSelected == "3":
        listExpenses()

    elif optionSelected == "4":
        break

    else:
        print("Invalid input. Please try again.")
