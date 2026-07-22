# negative indexing

marks = [3, 5, 6, "Hassam", "Hossen", 10]
# print(marks[-3])
# print(marks[len(marks) - 3])

# check if an item is present in list or not

list = ["Apple", "Bannana", "Orange", "Guava"]

userInput = str(input("Enter a string: "))

if userInput in list:
    print("Yes")
else:
    print("No")


fruits = ["Mango", "Apple", "Kewe", "Bannana", "Orange", "Lichi", "Jack fruit", "Strawberry", "pineapple", "blackberry"]

# print(fruits[-7:-3])
# print(fruits[:])    # fruits[0:len(fruits)]
# print(fruits[-4:])
# print(fruits[:-4])
print(fruits[2:1:6])

