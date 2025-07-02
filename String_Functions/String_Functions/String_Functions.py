text="Hello World"
print(text[6:])# This code prints the substring of 'text' starting from index 6 to the end.7

for letter in text:
    print(letter)

print(len(text))# This code prints the length of the string 'text'.

text2="Hello World \ntoday best of the day for me!" #escape
print(text2) # This code prints the string 'text2', which contains a newline character (\n).

#\t tab \b backspace \s space


name=input()
age=int(input())

#print("Hello my name is "+name+" and I am " +age+ "years old.") # This code concatenates the strings and prints a greeting message with the user's name and age.
print("Hello my name is %s and I am %d years old." %(name,age)) # This code uses string formatting to print a greeting message with the user's name and age.
print("Hello my name is {} and I am {} years old.".format(name,age)) # This code uses the format method to insert the user's name and age into the string.


text2="This is my text!"
print(text2) # This code prints the string 'text2'.
print(text2.count("text")) # This code counts the occurrences of the substring "text" in the string 'text2' and prints the result.
text2=text2.upper() # This code converts the string 'text2' to uppercase.
print(text2) # This code prints the uppercase version of 'text2'.
print(text2.count("T") + text2.count("t")) # This code counts the occurrences of both uppercase "T" and lowercase "t" in the string 'text2' and prints the total count.
print(text2.find("IS")) # This code finds the index of the substring "is" in the string 'text2' and prints the index.

seperator = ":"
mylist={'Kitchen', 'Dog', 'Bathroom', 'Bedroom'}
print(seperator.join(mylist)) # This code joins the elements of the set 'mylist' into a single string, separated by the specified separator (":") and prints the result.

text3 = "I am happy because I have a job!"
words=text3.split(' ')
print(words) # This code splits the string 'text3' into a list of words using space as the delimiter and prints the resulting list.)
print(text3.replace("happy", "sad")) # This code replaces the word "happy" with "sad" in the string 'text3' and prints the modified string.