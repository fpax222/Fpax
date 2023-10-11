import math
import sys

import functions
import pypackage.pymodule


print(sys.path)
print(math.pi, math.sqrt(9))
print(functions.person, functions.factorial(3))
print(pypackage.VAR)
pypackage.do_something()
pypackage.pymodule.some_function()


# from math import pi as math_pi, sqrt

# from functions import person as person_dict, factorial, pi
# from pypackage import pymodule
#
#
# print(math_pi, sqrt(9))
# print(person_dict, pi, factorial(3))
# pymodule.some_function()
