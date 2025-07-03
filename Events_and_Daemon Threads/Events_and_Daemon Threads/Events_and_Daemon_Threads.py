# #import threading

# event=threading.Event()

# def myfunction():
#     print("Wait for event to trigger...")
#     event.wait()  # Wait until the event is set
#     print("Performing action XYZ now...")

# t1=threading.Thread(target=myfunction)
# t1.start()

# x=input("\nDo you want to trigger the event? (y/n)")

# if x=='y':
#     event.set()  # Trigger the event
 
import threading
import time 

path="text.txt"
text=""
def readFile():
    global path, text
    while True:
        with open("text.txt","r") as file:
            text=file.read()
        time.sleep(3)

def printLoop():
    for x in range(30):
        print(text)
        time.sleep(1)
          
t1=threading.Thread(target=readFile, daemon=True)
t2=threading.Thread(target=printLoop)

t1.start()
t2.start()
