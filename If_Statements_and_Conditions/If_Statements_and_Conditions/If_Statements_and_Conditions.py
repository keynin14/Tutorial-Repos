x=input("Enter first number: ")
y=input("Enter second number: ")    

x=int(x)
y=int(y)

if x<y:
    print("x is less than y")
    if x>0:
        print("x is positive")
    else:
        print("x is negative")

elif x>y:
    print("x is greater than y")
    if x>10:
        print("x is also greater than 10")

else:
    print("x is greater than or equal to y")

