import numpy as np
randomNumber = np.random.randint(1,100)
# print(randomNumber)

while 1:
    i = int(input("Guess the number"))
    if(randomNumber > i):
        print("Greater than your number")
    elif(randomNumber < i):
        print("Smaller than your number")
    elif(i == randomNumber):
        print(i,randomNumber,"what a guess love it")
        break
        