from constants_library import *

from classes.parts_classes import *
from functions.speed_tests import *
from functions.custom_functions import *

wheel1 = Wheel("Side Wheel", 15, 15, 7.5, 13)
w1v = wheel1.volume()

print(f"The volume of the wheel is: {w1v}")

test1result = speed_test1(wheel1, CONSTANT1)

print(f"The result of the first speed test is: {Round(test1result, 2)}")