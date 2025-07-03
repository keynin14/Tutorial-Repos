from typing import Self


class Person:

    def __init__(self):
        print("Hello World!")

x= Person() # This will print "Hello World!" when an instance of Person is created.


class Person2:
    def __init__(self):
        self.name ="Kenan"
        self.age = 22

x2=Person2() # This will create an instance of Person2 with name "Kenan" and age 22.
print(x2.name) # This will print the name of the person.
print(x2.age)  # This will print the name and age of the person.

class Person3():

    amount =0
    
    def __init__(self,name,age,height):
        self.name=name
        self.age = age # This is the age of the person
        self.height = height 
        Person3.amount += 1

    def helloWorld(self):
        print("Hello World!")

    def __str__(self):
        print("Name: {} , Age: {}, Height: {}".format(self.name, self.age, self.height))

    def get_older(years):
        self.age += years

    def __del__(self):
        Person3.amount -= 1
        print("Object deleted")
    
    

x3=Person3("Kenan",22,185)
print(x3.name)    # This will print the name of the person.
print(x3.age)     # This will print the age of the person.
print(x3.height)  # This will print the height of the person.

x3.name="Sinan"
print(x3.name)
x3.helloWorld()  # This will call the helloWorld method of the Person3 class, which prints "Hello World!".
x4=Person3("Inci",21,173) # This will create another instance of Person3 with name "Inci", age 21, and height 173.
del x4 # This will delete the instance of Person3 and call the __del__ method, which prints "Object deleted".

#del x3  # This will delete the instance of Person3 and call the __del__ method, which prints "Object deleted". If we didn't put '#' amount would be 0.
print(Person3.amount)