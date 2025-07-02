def helloWorld():
    print("Hello, World!")

helloWorld()

def add(x,y):
    return x+y

result=add(19,32)
print(result)

def add2(x=0,y=0):
    return x+y

result2=add2()
print(result2)

def mysum(*numbers):
    result=0
    for number in numbers:
        result+=number
    return result
result3=mysum(1,2,3,4,5)
print(result3)