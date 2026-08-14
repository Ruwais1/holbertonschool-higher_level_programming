from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    data = []

    if source == 'json':
        try:
            with open('products.json', 'r') as file:
                data = json.load(file)
        except Exception:
            data = []
            
    elif source == 'csv':
        try:
            with open('products.csv', 'r') as file:
                reader = csv.DictReader(file)
                data = list(reader)
        except Exception:
            data = []
            
    elif source == 'sql':
        try:
            conn = sqlite3.connect('products.db')
            # sqlite3.Row allows accessing columns by name, similar to a dictionary
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            if product_id:
                cursor.execute('SELECT id, name, category, price FROM Products WHERE id = ?', (product_id,))
            else:
                cursor.execute('SELECT id, name, category, price FROM Products')
                
            rows = cursor.fetchall()
            # Convert rows to a list of dictionaries
            data = [dict(row) for row in rows]
            conn.close()
        except sqlite3.Error as e:
            data = []
            
    else:
        # Invalid or missing source
        return render_template('product_display.html', error_message="Wrong source")

    # Filter data for JSON and CSV if id is provided
    # (SQL already filtered it via the WHERE clause)
    if source in ['json', 'csv'] and product_id:
        filtered_data = [product for product in data if str(product.get('id')) == str(product_id)]
        data = filtered_data

    # Check if a specific ID was requested but not found
    if product_id and not data:
        return render_template('product_display.html', error_message="Product not found")

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
