from constants_library import *

from classes.parts_classes import *
from classes.plane_class import *
from functions.speed_tests import *
from functions.custom_functions import *

wheel1 = Wheel("Side Wheel", 15, 15, 7.5, 13)
# w1v = wheel1.volume()

# print(f"The volume of the wheel is: {w1v}")

# test1result = speed_test1(wheel1, CONSTANT1)

# print(f"The result of the first speed test is: {Round(test1result, 2)}")

lwing = Part("Left Wing", 11, 22, 5, 40)
rwing = Part("Right Wing", 11, 22, 5, 40)

parts = [wheel1, lwing, rwing]

plane1 = Plane("The Banshee", parts)
print(f"The parts of {plane1.name} are: ")
for x in plane1.parts:
  print(f"* {x.name}")