from pyhive import hive


def test_hive_connection():
    try:
        connect=hive.Connection(host='localhost', port=10000)
        cursor = connect.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchall()
        print("Connection to Hive successful")
        cursor.close()

        connect.close()


        return True;
    except Exception as e:
        print(f'Error connecting to Hive{e}')
        return False
    


if test_hive_connection():
    print("Performing actions on Hive...")
else:
    print("Connection to Hive failed. Unable to perform actions.")
