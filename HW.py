def check_age():
    try:
        age_input = input("Please enter your age: ")
        age = int(age_input)

        if age % 2 == 0:
            print(f"Your age is {age}, which is even.")
        else:
            print(f"Your age is {age}, which is odd.")

    except ValueError:
        print("Invalid input. Please enter a numeric value.")

check_age()