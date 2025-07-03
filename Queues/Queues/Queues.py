import queue

q=queue.Queue()
numbers=[10,20,30,40,60,70]

for number in numbers:
    q.put(number)

print(q.get())
print(q.get())

q1=queue.LifoQueue()
numberss=[1,2,3,4,5,6,7]
for x in numberss:
    q1.put(x)

print(q1.get())

q2=queue.PriorityQueue()
q2.put((2,"Hello World"))
q2.put((11,99))
q2.put((5,7.5))
q2.put((1,True))

while not q2.empty():
    print(q2.get()[1])