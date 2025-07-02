


from re import M


mylist=[10,20,30,"hello",True,8.97]

print(mylist)
print(mylist[3])
#print(mylist[9]) IndexError: list index out of range
print(mylist[:3])  # Slicing the first three elements
print(mylist[2:5])  # Slicing from index 2 to 4
print(mylist[-1])  # Accessing the last element
mylist[3]="WORLD"  # Changing the value at index 3
print(mylist)
mylist[4]=56  # Changing the value at index 4
print(mylist)

for x in mylist:
    print(x)


x=[1,2,3]
y=[4,5,6]
print(x+y)  # Concatenating two lists
print(x*3)  # Repeating the list three times

print(len(x))  # Length of the list
print(max(x))  # Maximum value in the list
print(min(x))  # Minimum value in the list

x.append(86)  # Appending a value to the end of the list
print(x)
#x.append(2,92)  # This will raise an error because append takes only one argument
x.append([2,92])  # Appending a list as a single element
print(x)
x.insert(2,"New walue")  # Inserting a value at index 2
print(x)
x.insert(3,74)  # Inserting a value at index 3
print(x)
x.remove("New walue")  # Removing the value "New value"
print(x)
x.pop(3)  # Removing the value at index 3
print(x)

t=[9,4,63,52,78,6,2,3]
t.sort()
print(t) # Sorts the list in place
print(sorted(t))  # Returns a new sorted list without modifying the original

k=[1,2,3,4,5]
l=(1,2,3,4,5)  # Tuple
#l[2]=100  # Tuples are immutable, this will raise an error
l=list(l)  # Converting tuple to list
l[2]=100  # Now we can modify the list
print(l)  # Prints the modified list

person={'name':"Kenan",'age':22,'gender':'M'}
print(person)  # Prints the dictionary
print(person['name'])
person['new key']=185  # Adding a new key-value pair
print(person)
print(person.keys())  # Prints all keys in the dictionary
print(person.values())  # Prints all values in the dictionary
print(person.items())  # Prints all key-value pairs in the dictionary

print(2 not in k) # Checks if 2 is not in the list k
print(4 in k)  # Checks if 4 is in the list k

p=10

if type(p) is str:
    print("p is a string")
else:
    print("p is not a string")
    if type(p) is int:
        print("p is an integer")