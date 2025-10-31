try:
    a = int(input("Enter a number "))
    print("The number is", a)
except ValueError as ex:
    print("Exception", ex)