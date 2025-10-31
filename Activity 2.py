try:
    num1,num2 = eval(input("Enter 2 numbers separated by a comma: "))
    result = num1/num2
    print("The result is", result)
except ZeroDivisionError:
    print("ZeroDivisonError has occured")
except SyntaxError:
    print("Comma is missing. Enter two numbers separated by a comma like this 1,2")
except:
    print("Invalid input")
else:
    print("No exceptions raised")
finally:
    print("This will appear no matter what")