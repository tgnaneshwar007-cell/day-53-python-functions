# Function inside another function

def one():
    def two():
        print("Inner function")

    print("Outer function")
    two()


one()