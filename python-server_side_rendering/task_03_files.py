from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/products')
def products():
    # Get query parameters
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    data = []

    # Check the source type
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
    else:
        # Invalid or missing source
        return render_template('product_display.html', error_message="Wrong source")

    # Filter data if id is provided
    if product_id:
        filtered_data = [product for product in data if str(product.get('id')) == str(product_id)]
        
        if not filtered_data:
            return render_template('product_display.html', error_message="Product not found")
        
        data = filtered_data

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
