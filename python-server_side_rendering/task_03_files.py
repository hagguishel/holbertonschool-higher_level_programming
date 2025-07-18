from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/products')
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    data = []

    if source == "json":
        with open("products.json", "r") as f:
            data = json.load(f)

    elif source == "csv":
        with open("products.csv", "r") as f:
            reader = csv.DictReader(f)
            data = list(reader)

    else:
        return render_template("product_display.html", error="Wrong source")

    # Filtrage par ID si demandé
    if product_id:
        data = [item for item in data if str(item.get("id")) == product_id or str(item.get("id")) == str(product_id)]
        if not data:
            return render_template("product_display.html", error="Product not found")

    return render_template("product_display.html", products=data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
