from math import pi as math
import sys
import random
from enum import Enum

from custom_module import (
    random_fun_fact,
    capital,
    flower,
    bird,
    song,
)  # importing items from another module
import custom_module

print(random_fun_fact())
print(f"{capital}")
# print(dir(random))  # gets all the functions in the module

print(
    __name__
)  # printing the name of the module which is __main__ in this case , because it's the main file that im running, im not importing it from anywhere
print(custom_module.__path__)  # getting the path of the module
print(custom_module.__name__)  # getting the name of the module
random.choice([1, 2, 3, 4, 5])
