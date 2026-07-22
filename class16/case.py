# case statement in python

# name = str(input("Enter the name you want to search: "))

# match name:
#     case "Roni":
#         print("This is Roni")
#     case "Sazid":
#         print("This is Sazid")
#     case _:
#         print("The name isn't here. Thank you")

num = int(input("Enter a number: "))

match num:
    case 4 if num % 2 == 0:
        print("This is 4")
    case 6 if num % 2 != 0:
        print("this is 6")
    case _ if num > 10:
        print("Number is greater than 10")