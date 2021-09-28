import sqlite3
import matplotlib.pyplot as plt

connect = sqlite3.connect('dsa.db')
cursor = connect.cursor()


# Generating graphic
def data_graphic():
    cursor.execute("SELECT id, value FROM products")
    ids = []
    values = []
    data = cursor.fetchall()
    for row in data:
        ids.append(row[0])
        values.append(row[1])

    plt.bar(ids, values)  # create a bar graph with matplotlib plt object
    plt.show()


data_graphic()
