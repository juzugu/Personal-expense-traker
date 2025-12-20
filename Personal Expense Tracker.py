import json
def save(data_to_save):
    with open("saving_data.json", "w") as f:
        json.dump({"saving_data.json": data_to_save}, f)

def load():
    try:
        with open("saving_data.json", "r") as f:
            return json.load(f).get("saving_data.json", [])
    except FileNotFoundError:
            return []

my_expenses = load()

def input_for_expenses ():
    product_bought = input("Enter the product you bought ")
    quantity = int(input("Enter the quantity bought if "))
    price = int(input("Enter the item price "))
    return product_bought, quantity, price
while True:
    product_bought, quantity, price = input_for_expenses()
    my_expenses.append({"product": product_bought, "quantity": quantity, "price": price})
    want_to_continue = input("Do you want to continue? yes/no ")
    if want_to_continue.strip().lower() == "no":
        break
print(my_expenses)
total_expense = 0
for expense in my_expenses:
    expense_vault = expense["quantity"] * expense["price"]
    total_expense = total_expense + expense_vault
    print(f"the expense for {expense['product']} is {expense_vault}")
print(f"total expense is {total_expense}")
save(my_expenses)