# Task 17
import math
def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4 * a * c
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    if discriminant > 0:
        return x1, x2
    if discriminant == 0:
        return x1, None
    if discriminant < 0:
        return None, None

root1, root2 = solve_quadratic_equation(1, -2, -3)
print("First root = %d and Second root = %d" % (root1, root2))
