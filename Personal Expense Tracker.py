import json

# Function to save data to json file
def save(data_to_save):
    with open("saving_data.json", "w") as f:
        json.dump({"saving_data.json": data_to_save}, f)

# Function to load data from json file
def load():
    try:
        with open("saving_data.json", "r") as f:
            return json.load(f).get("saving_data.json", [])
    except FileNotFoundError:
            return []
    
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
    quantity = check_input_number("Enter the quantity bought if ")
    quantity = int(quantity)
    price = check_input_number("Enter the item price ")
    return product_bought, quantity, price

budget = check_input_number("Enter your budget for this ")

my_expenses = load()
#1 Function to add expenses
def add_expenses():
    while True:
        product_bought, quantity, price = input_for_expenses()
        my_expenses.append({"product": product_bought, "quantity": quantity, "price": price})
        want_to_continue = input("Do you want to continue? yes/no ")
        if want_to_continue.strip().lower() == "no":
            save(my_expenses)
            break

#2 Function to delete expenses
def delete_expenses():
    while True:
        for index, expense in enumerate(my_expenses):
            print(f"{index}. {expense['product']}")
        delete = input("Do you want to delete any item? yes/no ")
        if delete.strip().lower() == "yes":
            index_to_delete = check_input_number("Enter the number of the item to delete ")
            index_to_delete = int(index_to_delete)
            if 0 <= index_to_delete and index_to_delete < len(my_expenses):
                my_expenses.pop(index_to_delete)
            else:
                print("Invalid number")
        elif delete.strip().lower() == "no":
            save(my_expenses)
            break        

#3 Function to calculate and display expenses    
def calculate_expenses_start():
    print(my_expenses)
    total_expense = 0
    for index, expense in enumerate(my_expenses):
        expense_vault = expense["quantity"] * expense["price"]
        total_expense = total_expense + expense_vault
        print(f"the expense for {index} {expense['product']} is {expense_vault}")
    if total_expense > budget:
        print(f"You have exceeded your budget of {budget} for {total_expense - budget}")
    else:
        print(f"You are within the budget. You have {budget - total_expense} remaining")
    print(f"total expense is {total_expense}")
    save(my_expenses)
    
# Main menu 
while True:
    print("menu options")
    print("1. Add expenses")
    print("2. Delete expenses")
    print("4. Exit")
    user_choise = input("Enter your choice (1/2/3): ")
    if user_choise == "1":
        add_expenses()
    elif user_choise == "2":
        delete_expenses()
    elif user_choise == "3":
        calculate_expenses_start()
    elif user_choise == "4":
        save(my_expenses)
        break

