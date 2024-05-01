import os
import pandas as pd
from dotenv import load_dotenv
from mysql.connector import Error
import mysql.connector
from exract import df

load_dotenv()

HOST = os.getenv('HOST')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')
MYSQL_USERNAME = os.getenv('MYSQL_USERNAME')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')


def create_db_connect(
        host_name, 
        user_name,
        user_password,
        db_name
        ):
        
        #print("Hello")
        db_connection = None
        
        try:
                db_connection = mysql.connector.connect(
                    host = host_name,
                    user = user_name,
                    passwd = user_password,
                    database = db_name  
                ) 
                
                print('MYSQL CONNECTION IS SUCCESSFUL')
        
        except Error as e:
                print(f"[DATABASE CONNECTION ERROR]: '{e}'")
        
        return db_connection


# call connect function test
connection = create_db_connect(HOST, MYSQL_USERNAME,MYSQL_PASSWORD, MYSQL_DATABASE)

# Create table in nvda_historical_stocks DB

def create_table(db_connection):
        
        CREATE_TABLE_SQL_QUERY = """
        
        CREATE TABLE IF NOT EXISTS historical_data (
                `id` BIGINT AUTO_INCREMENT PRIMARY KEY, 
                `date` DATE,
                `open` DECIMAL,
                `close` DECIMAL,
                `high` DECIMAL,
                `low` DECIMAL,
                `volume` INT         
        )
        
        """
        
        
        try:
                cursor = db_connection.cursor()
                cursor.execute(CREATE_TABLE_SQL_QUERY)
                db_connection.commit()
                print("Table created successfully")
        except Error as e:
                print(f"[CREATING TABLE ERROR]: '{e}'")
                
        
        ALTER_TABLE_SQL_QUERY = """
        ALTER TABLE historical_data
        MODIFY COLUMN `id` BIGINT AUTO_INCREMENT;
    """
        try:
                cursor.execute(ALTER_TABLE_SQL_QUERY)
                db_connection.commit()
                print("Table altered successfully")
        except Error as e:
                print(f"[ALTERING TABLE ERROR]: '{e}'")
      
    

create_table(connection)


# INSERT DATA INTO SQL DB

def insert_to_table(db_connection, df):
        
        cursor = db_connection.cursor()
        
        INSERT_DATA_QUERY = """
        
        INSERT INTO historical_data (
                `id`,
                `date`,
                `open`,
                `close`,
                `high`,
                `low`,
                `volume`
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s )
        
        ON DUPLICATE KEY UPDATE
                `id` = VALUES(`id`),
                `date` = VALUES(`date`),
                `open` = VALUES(`open`),
                `close` = VALUES(`close`),
                `high` = VALUES(`high`),
                `low` = VALUES(`low`),
                `volume` = VALUES(`volume`)       
        """
        
        # create list of tuple from DF values
        data_values_as_tuples = [tuple(x) for x in df.to_numpy()]
        
        # Execute
        
        cursor.executemany(INSERT_DATA_QUERY, data_values_as_tuples)
        db_connection.commit()
        print("Data inserted successfully")
        
        
        
# Call processed data with inserted data
# REMEMBER all commas, backticks etc!!!!!
insert_to_table(connection, df)


