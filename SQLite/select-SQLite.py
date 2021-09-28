import sqlite3


connect = sqlite3.connect('dsa.db')
cursor = connect.cursor()


# Read all date
def read_all_data():
    cursor.execute('SELECT * FROM PRODUCTS')
    for row in cursor.fetchall():
        print(row)


# Read of specific records
def read_records():
    cursor.execute('SELECT * FROM PRODUCTS WHERE value > 60.0')
    for row in cursor.fetchall():
        print(row)


# Read of specific column
def read_column():
    cursor.execute('SELECT * FROM PRODUCTS')
    for row in cursor.fetchall():
        print(row[3])


read_all_data()
print()
read_records()
print()
read_column()

cursor.close()
connect.close()
