from flask import Flask, render_template, request
import json
import csv
import sqlite3

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

    elif source == 'sql':
        products = from_sql()
        if products is None:
            return render_template('product_display.html', error="Database error", products=[])
        else:
            data = products


    else:
        return render_template("product_display.html", error="Wrong source")

    # Filtrage par ID si demandé
    if product_id:
        data = [item for item in data if str(item.get("id")) == product_id or str(item.get("id")) == str(product_id)]
        if not data:
            return render_template("product_display.html", error="Product not found")

    return render_template("product_display.html", products=data)

def from_sql():
    try:
        connexion = sqlite3.connect('products.db')
        cursor = connexion.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        connexion.close()
        products = []
        for row in rows:
            products.append({'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]})
        return products
    except Exception as e:
        print(f"Database error: {e}")
        return None
if __name__ == "__main__":
    app.run(debug=True, port=5000)
