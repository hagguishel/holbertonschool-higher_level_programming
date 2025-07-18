import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/items')
def items():
    with open("items.json", "r") as file:
        data = json.load(file)
        item_list = data.get("items", [])

    return render_template("items.html", items=item_list)
