import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


host= os.getenv('HOST')
database = os.getenv('MYSQL_DATABASE')
username = os.getenv('MYSQL_USERNAME')
password = os.getenv('MYSQL_PASSWORD')
        
mydb = mysql.connector.connect(
        host = host,
        user= username,
        passwd = password,
        database = database
)



if mydb.is_connected():
        print('Database connected')
        
else:
        print('Error connecting')
        


mycursor = mydb.cursor()