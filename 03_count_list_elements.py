# Counting elements in a list using a function

def lst(s):
    d = 0

    for i in s:
        d = d + 1

    print("Number of elements:", d)


l1 = [10, 20, 30, 40, 50]

lst(l1)