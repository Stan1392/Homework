# Task 11
import math
def degrees2radians(degrees):
    result = degrees * math.pi / 180
    return result

result_cos60 = degrees2radians(60)
result_cos45 = degrees2radians(45)
result_cos40 = degrees2radians(40)
print('\nCos60 = %.2f rad, Cos45 = %.2f rad, Cos40 = %.2f rad'
      % (result_cos60, result_cos45, result_cos40))

