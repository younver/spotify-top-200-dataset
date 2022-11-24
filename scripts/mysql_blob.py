import mysql.connector
from PIL import Image
import io

def f2b(path):
    with open(path, 'rb') as f:
        binary_data = f.read()
    return binary_data

def insert_blob():
    query = "INSERT INTO test_table(id, image) VALUES (%s, %s)"

    test_id = "2"
    test_img = f2b("test.jpeg")

    result = cursor.execute(query, (test_id, test_img))

    connection.commit()

    return result

def display_blob():
    query = "SELECT image FROM test_table WHERE id=1"
    
    result = cursor.execute(query)
    data = cursor.fetchall()
    img = data[0][0]
    img = Image.open(io.BytesIO(img))
    img.show()
    
    return result

try:
    connection = mysql.connector.connect(
        host="localhost", database="test", user="root", password="{password}"
    )

    cursor = connection.cursor()

    # insert_blob()
    display_blob()

except mysql.connector.Error as error:
    print(format(error))
 
finally:
   
    if connection.is_connected():
       
        cursor.close()
        connection.close()
        print("~~ mysql connection is closed")
