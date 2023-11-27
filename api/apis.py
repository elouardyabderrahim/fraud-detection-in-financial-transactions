from flask import Flask, jsonify
import json

app = Flask(__name__)

with open('data/transactions_test.json', 'r') as transactions_file:
    transactions = json.load(transactions_file)

@app.route('/api/transactions', methods=['GET'])
def get_transactions():
    return transactions

with open('data/customers_test.json', 'r') as customers_file:
    customers = json.load(customers_file)

@app.route('/api/customers', methods=['GET'])
def get_customers():
    return customers

with open('data/external_data_test.json', 'r') as external_data_file:
    external_data = json.load(external_data_file)

@app.route('/api/external', methods=['GET'])
def get_external_data():
    return external_data

if __name__ == '__main__':
    app.run(debug=True)
