import json
from flask import Flask,render_template

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
@app.route('/')
def home():
    my_expenses, budget = load()
    return render_template("index.html", budget=budget)
    

if __name__ == '__main__':
    app.run(debug=True)