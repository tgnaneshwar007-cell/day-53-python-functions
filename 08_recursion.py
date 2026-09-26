# Recursion

def rec(n):
    if n == 1000:
        return

    print(n)
    n = n + 1
    rec(n)


rec(1)