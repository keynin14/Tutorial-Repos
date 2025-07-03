import sqlite3

class Person:

    def __init__(self, id_number=-1, first="", last="", age=-1):
        self.id_number = id_number
        self.first = first
        self.last = last
        self.age = age
        self.connection = sqlite3.connect('mydata.db')
        self.cursor = self.connection.cursor() 

    def load_person(self, id_number):
        self.cursor.execute("""
        SELECT * FROM persons 
        WHERE id = ?
        """, (id_number,))
        results = self.cursor.fetchone()
        if results:
            self.id_number = results[0]
            self.first = results[1]
            self.last = results[2]
            self.age = results[3]
    def insert_person(self):
        self.cursor.execute("""
        INSERT INTO persons VALUES
        ({}, '{}', '{}', {})
        """.format(self.id_number,self.first,self.last,self.age))

        self.connection.commit()
        self.connection.close()

p1=Person(7,"Alex", "Robbins",30)   
p1.insert_person()
connection = sqlite3.connect('mydata.db')
cursor = self.connection.cursor() 

cursor.execute("SELECT * FROM persons")
results=cursor.fetchall()
print(results)

# p1 = Person()
# p1.load_person(1)
# print(p1.first)
# print(p1.last)
# print(p1.age)
# print(p1.id_number)


# connection = sqlite3.connect('mydata.db')
# cursor = connection.cursor()



# cursor.execute("""
# CREATE TABLE IF NOT EXISTS persons ( 
#     id INTEGER PRIMARY KEY,
#     first_name TEXT,
#     last_name TEXT,
#     age INTEGER
# )
# """)

# cursor.execute("""
# INSERT INTO persons VALUES
# ('Paul', 'Smith', 24),
# ('Mark', 'Johnson', 42),
# ('Anna', 'Smith',34)
# """)

# cursor.execute("""
# SELECT * FROM persons 
# WHERE last_name = 'Smith'
# """)

# rows=cursor.fetchall()
# print(rows)
# # Commit the changes and close the connection

# connection.commit()
#connection.close()

