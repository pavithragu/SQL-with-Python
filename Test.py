# access db with python
import sqlite3

# Creating Connection
connection = sqlite3.connect("database_path.db")
cursor = connection.cursor()


# To delete existing table
def delete():
    cursor.execute("drop table table_name")
    print("Existing Table deleted successfully...")
    create()


# table creation
def create():
    try:
        cursor.execute("""CREATE TABLE table_name (
    "ID"	INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
    "NAME"	TEXT NOT NULL,
    "AGE"	INTEGER NOT NULL default 18)""")
        print("New table created successfully...")
    except:
        choice = input("Table already exists!\nDo you want to delete the existing table? (Y/N):")
        delete() if choice.upper() == "Y" else print("Existing table loaded!")


create()

# Adding Data
cursor.execute("""insert into table_name(NAME, AGE) values
    ('Murugan', 51), 
    ('Thilagavathi', 49), 
    ('Sathiya', 32), 
    ('Suvitha', 29), 
    ('Raju', 27), 
    ('Ragu', 25),
    ('Thiru', 14),
    ('Dharnesh',12)""")

# Delete rows if age is 13
cursor.execute("delete from table_name where AGE = 13")

# Read Data
cursor.execute("select * from table_name")
data = cursor.fetchall()
for item in data:
    print(item)

# Save and close
connection.commit()
cursor.close()
connection.close()
