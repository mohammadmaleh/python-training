# String data type
# literal assignment

first = "Mohammad"
last = "gray"

print(type(first))
print(type(first) == str)
print(isinstance(first, str))

# constructor function
pizza = str("Pepperoni")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# Concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number into a string
decade = str(1980)
print(type(decade))


# multiline
multiline = """Hi my Name is


Slim Shady!!!
"""
print(multiline)


# Escaping special characters
sentence = "I'm back a work! \t Hey! \n\n Where's this at \\location?"

print(sentence)

# String Methods

print(first)
print(first.lower())
print(first.upper())

print(multiline.title())
print(multiline.replace("Hi", "goodbye"))
print(len(multiline))


print("")

title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(20, ".") + "$1".rjust(4))
print("tea".ljust(20, ".") + "$12".rjust(4))
print("Cheesecake".ljust(20, ".") + "$3".rjust(4))


# String index
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# methods return boolean data
print(first.startswith("M"))
print(first.endswith("Z"))

# Boolean data type
myValue = True
x = bool(False)
print(type(x))
print(isinstance(myValue, bool))

# Numeric data type
# integer type
price = 100
x = int(80)
print(type(x))
print(isinstance(price, int))

# float type
gpa = 3.26
y = float(1.4)
print(type(gpa))
print(isinstance(gpa, float))

# complex type 