

with open('sample.txt','r') as f:
    content = f.read()
    print(content) 

file=open('sample.txt','r')
content = file.read()
print(content)

file=open('sample.txt','w')
file.write("HELLO WORLD!") 
file.close()
file.flush()

with open('sample.txt','w') as f:
    file.write("HELLO WORLD!")


from os import *

mkdir('new_folder') 
chdir('new_folder')
mkdir('sub_folder')

rename('sub_folder', 'renamed_folder')
remove('sample.txt')

