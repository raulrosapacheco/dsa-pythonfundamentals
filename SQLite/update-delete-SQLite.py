import sqlite3

connect = sqlite3.connect('dsa.db')
cursor = connect.cursor()


# Update
def update_data():
    cursor.execute('UPDATE products SET value = 70.00 WHERE value = 98.0')
    connect.commit()


# Delete
def delete_data():
    cursor.execute('DELETE FROM products WHERE value = 62.0')
    connect.commit()


# Read all date
def read_all_data():
    cursor.execute('SELECT * FROM PRODUCTS')
    for row in cursor.fetchall():
        print(row)


read_all_data()
print()
update_data()
read_all_data()
print()
delete_data()
read_all_data()
