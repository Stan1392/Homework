# Task 15
import math
def circles_intersect(x1, y1, r1, x2, y2, r2):
    circles_distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    if circles_distance < r1 + r2:
        print("Circles intersect at two points")
        return True
    if circles_distance == r1 + r2:
        print("Circles intersect at one point")
        return True
    if circles_distance > r1 + r2:
        print("Circles do not intersect")
        return False




