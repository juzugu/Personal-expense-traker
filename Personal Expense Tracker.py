import json

# Function to save data to json file
def save(data_to_save, budget):
    with open("saving_data.json", "w") as f:
        json.dump({"saving_data.json": data_to_save, "budget": budget}, f)

# Function to load data from json file
def load():
    try:
        with open("saving_data.json", "r") as f:
            data = json.load(f)
            return data.get("saving_data.json", []), data.get("budget", 0)
    except FileNotFoundError:
            return [], 0
    
# Function to check for valid number input 
def check_input_number(user_prompt):
    while True:
        try:
            value = float(input(user_prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to get expense details from user
def input_for_expenses ():
    product_bought = input("Enter the product you bought ")
    quantity = check_input_number("Enter the quantity bought")
    quantity = int(quantity)
    price = check_input_number("Enter the item price ")
    return product_bought, quantity, price


#1 Function to add expenses
def add_expenses(my_expenses, budget):
    while True:
        product_bought, quantity, price = input_for_expenses()
        my_expenses.append({"product": product_bought, "quantity": quantity, "price": price})
        want_to_continue = input("Do you want to continue? yes/no ")
        if want_to_continue.strip().lower() == "no":
            save(my_expenses, budget)
            break

#2 Function to delete expenses
def delete_expenses(my_expenses, budget):
    while True:
        for index, expense in enumerate(my_expenses):
            print(f"{index+1}. {expense['product']}")
        delete = input("Do you want to delete any item? yes/no ")
        if delete.strip().lower() == "yes":
            index_to_delete = check_input_number("Enter the number of the item to delete ")
            index_to_delete = int(index_to_delete) - 1
            if 0 <= index_to_delete and index_to_delete < len(my_expenses):
                my_expenses.pop(index_to_delete)
            else:
                print("Invalid number")
        elif delete.strip().lower() == "no":
            save(my_expenses, budget)
            break        

#3 Function to calculate and display expenses    
def calculate_expenses_start(my_expenses,budget):
    for expense in my_expenses:
        print(f"Expense: {expense['product']}, Quantity: {expense['quantity']}, Price: {expense['price']}")
    total_expense = 0
    for index, expense in enumerate(my_expenses):
        expense_vault = expense["quantity"] * expense["price"]
        total_expense = total_expense + expense_vault
        print(f"the expense for f{index} {expense['product']} is {expense_vault}")
    if total_expense > budget:
        print(f"You have exceeded your budget of {budget} for {total_expense - budget}")
    else:
        print(f"You are within the budget. You have {budget - total_expense} remaining")
    print(f"total expense is {total_expense}")
    save(my_expenses, budget)

def main():
    my_expenses, budget = load()
    # Main menu 
    while True:
        print("menu options")
        print("1.change budget")
        print("2. Add expenses")
        print("3. Calculate expenses")
        print("4. Delete expenses")
        print("5. Exit")
        user_choise = input("Enter your choice ")
        if user_choise == "1":
            budget = check_input_number("Enter your budget")
            save(my_expenses, budget)
        elif user_choise == "2":
            add_expenses(my_expenses, budget)
        elif user_choise == "3":
            calculate_expenses_start(my_expenses, budget)
        elif user_choise == "4":
            delete_expenses(my_expenses, budget)
        elif user_choise == "5":
            save(my_expenses, budget)
            break

if __name__ == "__main__":
    main()