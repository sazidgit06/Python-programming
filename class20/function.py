# pass


def isLesser(a, b):
    pass

# function

def isGreater(a, b):
    if(a > b):
        print("A is greater.")
    else:
        print("B is greater.")


a = int(input("Enter a: "))
b = int(input("Enter b: "))

isGreater(a, b)
isLesser(a, b)

# calling a function

def name(fname, lname):
    print("Hello ", fname, lname)

name1 = str(input("Enter a name: "))
name2 = str(input("Enter a name: "))

name(name1, name2)