from encodings.punycode import T

import threading 

def helloWorld():
    print("Hello World")
# Create a thread that runs the helloWorld function

t1= threading.Thread(target=helloWorld)
t1.start()

def function1():
    for x in range(1000):
        print("ONE")

def function2():
    for x in range(1000):
        print("TWO")

#function1() # This will run in the main thread  
#function2()

#t2=threading.Thread(target=function1)
#t3=threading.Thread(target=function2)

#t2.start()
#t3.start()

def hello():
    for x in range(50):
        print("HELLO")

t=threading.Thread(target=hello)
t.start()
t.join()  # Wait for the thread to finish before continuing
print("Another text")