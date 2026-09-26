# Passing function as parameter to another function

def add(x):
    return x + 10

def out(r):
    print(r)

out(add(5))