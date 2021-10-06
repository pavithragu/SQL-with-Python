# access db with python
import sqlite3

# Creating Connection
connection = sqlite3.connect("database_path.db")
cursor = connection.cursor()

# table creation
cursor.execute("Create table table_name(NAME text, ID integer);")

# Adding data to the table
cursor.execute("insert into table_name(NAME, ID) values('your_name', 'your_id');")
connection.commit()

# Read data
cursor.execute("select * from table_name")
data = cursor.fetchall()
for item in data:
    print(item)

# update data
cursor.execute("update table_name set NAME='your_new_name' where NAME='your_name';")

# Check your name changed or not
cursor.execute("select * from table_name")
data = cursor.fetchall()
for item in data:
    print(item)

# Delete data
cursor.execute("delete from table_name where NAME='your_name';")

# Check your name deleted or not
cursor.execute("select * from table_name")
data = cursor.fetchall()
for item in data:
    print(item)

# add a column
cursor.execute("alter table table_name add column AGE;")

# Check your column added or not
cursor.execute("select * from table_name")
data = cursor.fetchall()
for item in data:
    print(item)

# drop a column
cursor.execute("alter table table_name drop column AGE;")

# Check your column deleted or not
cursor.execute("select * from table_name")
data = cursor.fetchall()
for item in data:
    print(item)

# change the data type of a column
cursor.execute("alter table table_name alter column NAME integer;")

# drop the table
cursor.execute("drop table table_name;")

# clear the table
cursor.execute("truncate table table_name;")

# Save and close
connection.commit()
cursor.close()
connection.close()
