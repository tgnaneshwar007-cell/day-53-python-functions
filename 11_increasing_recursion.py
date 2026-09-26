# Print 1 to 10 using recursion

def rec(n):
    if n == 11:
        return

    print(n)
    rec(n + 1)


rec(1)