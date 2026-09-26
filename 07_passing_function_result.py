# Passing function result as parameter to another function

def add(x):
    return x * x

def out(r):
    print(r)

n = int(input("Enter a number: "))

out(add(n))