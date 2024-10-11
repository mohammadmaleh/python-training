x = "1"
try:
    if not type(x) is int:
        raise TypeError("Only integers are allowed")  # raise error conditionally

    print(x / 0)  # will raise division by zero error
except NameError:  # catch name error
    print("Variable x is not defined")
except ZeroDivisionError:  # catch zero error
    print("Cannot divide by zero")
except Exception as error:  # catch the error that are not explicitly handled
    print(f"Error: {error}")
else:  # no error
    print("No error")
finally:  # always execute
    print("The 'try except' is finished")
