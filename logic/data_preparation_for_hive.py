from pyhive import hive
import requests
from datetime import datetime as dt

customer_url="http://127.0.0.1:5000/api/customers"
transactions_url="http://127.0.0.1:5000/api/transactions"
external_data_url="http://127.0.0.1:5000/api/external"

connect=hive.Connection(host='localhost', port=10000)
cursor = connect.cursor()


def test_hive_connection():
    try:
        cursor.execute("SELECT 1")
        result = cursor.fetchall()
        print("Connection to Hive successful")
        return True
    except Exception as e:
        print(f'Error connecting to Hive: {e}')
        return False

# create data base for Fraud detection
def create_db(db_name):
    try:
        cursor.execute(f'CREATE DATABASE {db_name}')
        print('DataBase created successfully !! ')

    except Exception as e :
        print(f'error creating DataBase : {e}')
    return True


def get_data_from_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        
        # Check if the response is in JSON format
        if 'application/json' in response.headers.get('content-type', '').lower():
            data = response.json()
            

        else:
            data = response.text
    


        return data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None




# create table for transactions
def create_transactions_table():
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS frauddb.transactionsssss (
                transaction_id STRING,
                date_time  STRING,
                amount DOUBLE,
                currency STRING,
                merchant_details STRING,
                customer_id STRING,
                transaction_type STRING,
                location STRING
            )
        """)
        print("Table 'transaction' created successfully!")
    except Exception as e:
        print(f'Error creating table: {e}')

def create_customers_table():
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS frauddb.customers (
                customer_id STRING,
                age INTEGER,
                location STRING,
                avg_transaction_value DOUBLE
            )
        """)
        print("Table 'customers' created successfully!")
    except Exception as e:
        print(f'Error creating table: {e}')



def insert_transactions_data(data):
    try:       
        # print("entry",modified_entry)
         print(data)
         cursor.execute(f"""
               INSERT INTO frauddb.transactionsssss
               VALUES ('{data["transaction_id"]}', '{data["date_time"]}', '{data["amount"]}','{data["currency"]}', '{data["merchant_details"]}','{data["customer_id"]}', '{data["transaction_type"]}', '{data["location"]}')
            """)
         
         print("Transactions data inserted successfully!")
    except Exception as e:
        print(f'Error inserting transactions data: {e}')

def insert_customer_data(data):
    try:       
        # print("entry",modified_entry)
         print(data)
         customer_id = data["customer_id"]
         age = data["demographics"]["age"]
         location = data["demographics"]["location"]
         avg_transaction_value = data["behavioral_patterns"]["avg_transaction_value"]

         cursor.execute(f"""
               INSERT INTO frauddb.customers
               VALUES ('{ customer_id}', '{age}','{location}', '{avg_transaction_value}')
            """)
         
         print("customer data inserted successfully!")
    except Exception as e:
        print(f'Error inserting transactions data: {e}')

if test_hive_connection():
    print("Performing actions on Hive...")
    create_db("frauddb")
    cursor.execute("USE frauddb")
    create_transactions_table()
    create_customers_table()
    transactions_data = get_data_from_api(transactions_url)
    customer_data=get_data_from_api(customer_url)
    external_data_data=get_data_from_api(external_data_url)



    for data_cust in customer_data:
        insert_customer_data(data_cust)

    
    for data in transactions_data:
        insert_transactions_data(data)

else:
    print("Connection to Hive failed. Unable to perform actions.")

cursor.close()
connect.close()

