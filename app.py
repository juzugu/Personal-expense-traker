import json
from flask import Flask, redirect,render_template,request, url_for

app = Flask(__name__)
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
    except (FileNotFoundError, json.JSONDecodeError):
        return [], 0

@app.route('/delete/<int:index>')
def delete_expense(index):
    my_expenses, budget = load()
    try:
        my_expenses.pop(index)
        save(my_expenses, budget)
        return redirect(url_for('home'))
    except IndexError:
        return redirect(url_for('home'))
    
@app.route('/')
def home():
    my_expenses, budget = load()
    return render_template("index.html", budget=budget, expenses=my_expenses)
@app.route('/add', methods=['POST'])
def add_expenses():
    my_expenses, budget = load()
    product = request.form.get('product')
    price = float(request.form.get('price'))
    quantity = int(request.form.get('quantity'))
    my_expenses.append({"product": product, "quantity": quantity, "price": price})
    save(my_expenses, budget)
    return redirect(url_for('home'))
if __name__ == '__main__':
    app.run(debug=True)