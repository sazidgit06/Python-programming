# default arguments

def average(a=1, b=3):
    print((a+b) / 2)

# average()

# keyword arguments

def name(fname = "sazid", lname = "Hasan"):
    print("Hello, ", fname, lname)

# name(lname = "akter", fname = "shamima")

# required arguments 

def mul(pi, r):
    print(pi*r*r)

# mul(3.14, 6)    #must provide all data in required arguments

# variable length arguments

def name(**name):
    print("Hello, ", name["fname"], name["mname"], name["lname"])

name(fname = "Liton", mname = "Kumar", lname = "Das")

def nm(*nm):
    return ("Hello, ", nm[0], nm[1], nm[2])

print(nm("Shaheen", "Shah", "Afridi"))