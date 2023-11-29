from flask import Flask, jsonify
import json

app = Flask(__name__)

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None 
    except json.JSONDecodeError:
        return None  

transactions_file_path = 'data/transactions_test.json'
customers_file_path = 'data/customers_test.json'
external_data_file_path = 'data/external_data_test.json'

transactions = load_json(transactions_file_path)
customers = load_json(customers_file_path)
external_data = load_json(external_data_file_path)

@app.route('/api/transactions', methods=['GET'])
def get_transactions():
    if transactions:
        return jsonify(transactions)
    else:
        return jsonify({"error": "Unable to load transactions data"}), 500

@app.route('/api/customers', methods=['GET'])
def get_customers():
    if customers:
        return jsonify(customers)
    else:
        return jsonify({"error": "Unable to load customers data"}), 500

@app.route('/api/external', methods=['GET'])
def get_external_data():
    if external_data:
        return jsonify(external_data)
    else:
        return jsonify({"error": "Unable to load external data"}), 500

if __name__ == '__main__':
    app.run(debug=True)
