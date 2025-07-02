#print(9/0) # This will raise a ZeroDivisionError
#x="hello"
#int(x) # This will raise a ValueError

try:
    x=int(input("Enter first number: "))
    y=int(input("Enter second number: "))
    print(x/y)

except ValueError:
    print("An error occurred. Please check your input.")    

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    y=1
    print(x/y)

finally:
    print("DONE!")


k=100
l=10

assert(k>l), "k should be greater than l"