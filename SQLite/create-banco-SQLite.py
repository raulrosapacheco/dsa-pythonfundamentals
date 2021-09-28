import os
import sqlite3

# Removing file with SQLite database (if any)
os.remove("university.db") if os.path.exists("university.db") else None

# Creating a connection to the database, if the database does not exist, it will be created
connect = sqlite3.connect('university.db')

# Creating cursor that will allow you to scroll through all records in a dataset
cursor = connect.cursor()

# Creating the first SQL statement
# table name : courses
# column : id (integer, primary key), title (varchar(100)) , category (varchar(140))
sql_create = 'create table courses (id integer primary key, title varchar(100), category varchar(140))'

# Executing the sql statement at the cursor
cursor.execute(sql_create)

# Creating another SQL statement for insert registry
sql_insert = 'insert into courses values (?, ?, ?)'

# Data
data_set = [(1000, 'R', 'Data Science'), (1001, 'SQL', 'Big Data'),
            (1002, 'Python', 'Programming')]

# Entering data
for data in data_set:
    cursor.execute(sql_insert, data)

# Recording transaction
connect.commit()

# Select records
sql_select = 'select * from courses'

# Select all records with the cursor and take all selected records, save anda print
cursor.execute(sql_select)
data_set2 = cursor.fetchall()
print(data_set2)
for data in data_set:
    print('Course ID: %d, Title: %s, category: %s' % data)

print()
# Creating other registry
data_set3 = [(1003, 'MongoDB', 'Big Data'), (1004, 'R', 'Data Analytics')]
for data in data_set3:
    cursor.execute(sql_insert, data)
connect.commit()
cursor.execute('select * from courses')
data_set4 = cursor.fetchall()
print(data_set4)
