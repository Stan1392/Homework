# Task 13
import math
def cone_square_and_volume(radius, height):
    result_cone_square = math.pi * radius * math.sqrt(radius**2 + height**2) + math.pi * radius**2
    result_cone_volume = 1 / 3 * math.pi * radius**2 * height
    return result_cone_square, result_cone_volume

cone_square, cone_volume = cone_square_and_volume(10, 25)
print("\nFull cone square = %.2f, Cone volume = %.2f" % (cone_square, cone_volume))