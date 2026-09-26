# Passing a list to a function

def lst(s):
    d = 0
    res = ""

    for i in s:
        if type(i) == int:
            d = d + i
        else:
            res = res + i

    print("Sum of integers:", d)
    print("Characters:", res)


l1 = [10, "H", "A", 40, 50, "R", "T"]

lst(l1)