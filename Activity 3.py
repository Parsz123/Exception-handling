Valid = False
while Valid is not True:
    try:
        n = int(input("Enter a number: "))
        while n%2 == 0:
            print("bye")
        Valid = True
    except ValueError:
        print("Invalid")