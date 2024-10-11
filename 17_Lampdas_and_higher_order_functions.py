square = lambda num: num * num  # 5 * 5

# print(square(5))


def funcBuilder(x):
    return lambda y: x * y  # x * y


doubler = funcBuilder(2)  # sets x to 2
tripler = funcBuilder(3)  # sets x to 3

# print(doubler(5))  # sets y to 5 and results in 10
# print(tripler(5))  # sets y to 5 and results in 15


# higher order function


numbers = [3, 7, 12, 20, 1]
squared_nums = map(lambda num: num * num, numbers) # takes each item in the list and applies the function to it and returns a new map object ,  which can be converted to a list
print(list(squared_nums)) # [9, 49, 144, 400, 1]



odd_nums = filter(lambda num: num % 2 != 0, numbers) # takes each item in the list and applies the function to it and returns a new filter object ,  which can be converted to a list
print(list(odd_nums)) # [3, 7, 1] 


from functools import reduce


sum = reduce(lambda a, b: a + b, numbers) # takes each item in the list and applies the function to it and returns a new reduce object ,  which can be converted to a list
print(sum) # 33