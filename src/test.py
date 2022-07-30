import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(host='db', user='root', password='12345')
if connection.is_connected():
    db_Info = connection.get_server_info()
    print("Connected to MySQL Server version ", db_Info)
    cursor = connection.cursor()
    cursor.execute("show databases")
    for d in cursor:
        print(d[0])