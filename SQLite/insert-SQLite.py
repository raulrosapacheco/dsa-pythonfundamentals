import os
import sqlite3
import random
import datetime

os.remove('dsa.db') \
    if os.path.exists('dsa.db') else None

connect = sqlite3.connect('dsa.db')
cursor = connect.cursor()


#  Function to create a table
def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT,'
                   'prod_name TEXT, value REAL)')


# Function to insert a line
def data_insert():
    cursor.execute("INSERT INTO products VALUES(10, '2020-05-02 14:32:11', 'keyboard', 90)")
    connect.commit()


# Using variables to enter data
def data_insert_var():
    new_date = datetime.datetime.now()
    new_prod_name = 'monitor'
    new_value = random.randrange(50, 100)
    cursor.execute("INSERT INTO products (date, prod_name, value) VALUES (?, ?, ?)",
                   (new_date, new_prod_name, new_value))
    connect.commit()


# Performing the functions
create_table()
data_insert()

# Generating values and inserting into the table
for i in range(10):
    data_insert_var()


# Closing the connection
cursor.close()
connect.close()
