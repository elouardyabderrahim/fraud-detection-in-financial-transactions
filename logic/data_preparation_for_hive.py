from pyhive import hive
import requests


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
    


        return True;
    except Exception as e:
        print(f'Error connecting to Hive{e}')
        return False
    
# create data base for Fraud detection
def create_db(db_name):
    try:
        cursor.execute(f'CREATE DATABASE {db_name}')
        print('DataBase created successfully !! ')

    except Exception as e :
        print(f'error creating DataBase : {e}')
    return True



if test_hive_connection():
    print("Performing actions on Hive...")
    create_db("frauddb")
    cursor.execute("show DATABASES ")
    dbs = cursor.fetchall()
    for i in dbs:
        print(i)
  

else:
    print("Connection to Hive failed. Unable to perform actions.")
   




def get_data_from_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Check if the response is in JSON format
        if 'application/json' in response.headers.get('content-type', '').lower():
            data = response.json()
            print("data:", data)

        else:
            data = response.text
            print("data:", data)


        return data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None


# get_data_from_api(customer_url)
# get_data_from_api(transactions_url)
# get_data_from_api(external_data_url)


cursor.close()
connect.close()