def hello():
    print("hello")


hello()


def sum(num1, num2=4):
    if type(num1) != int or type(num2) != int:
        print("num1 and num2 must be integers")
        return None
    return num1 + num2


print(sum(1, 2))


def multiple_items(*args):
    print(args)  # (1, 2, 3)
    print(type(args))  # <class 'tuple'>


multiple_items(1, 2, 3)


def mult_named_items(**kwargs):  # kwargs = keyword arguments
    print(kwargs)  # {'num1': 1, 'num2': 2, 'num3': 3}
    print(type(kwargs))  # <class 'dict'>


mult_named_items(num1=1, num2=2, num3=3)
