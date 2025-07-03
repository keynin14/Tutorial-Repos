n=7

fact = 1
while n> 1:
    fact = fact * n
    n= n - 1

print(fact)

def factorial(n):
    if n<1:
        return 1
    else:
        number=n*factorial(n-1)
        return number

print(factorial(7))    


def fibonacci(k):
    a,b=0,1
    for x in range(k):
        a,b=b,a+b
        return a
print(fibonacci(7))

def fibonacci2(k):
    if k<=1:
        return k
    else:
        return (fibonacci2(k-1) + fibonacci2(k-2))

print(fibonacci2(7))
