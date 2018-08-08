import math
# Task1
a = 10
b = 14
c = 13
Result = a + b * (c / 2)
print("\nResult(task_1) for a = %d, b = %d, c = %d is equal %d" %
      (a, b, c, Result))
#------------------------------------------------------------

#Task2
a = 1
b = 0
Result = (a**2 + b**2) % 2
print('\nResult(task_2) for a = %d and b = %d is equal %d' %
      (a, b, Result))
#------------------------------------------------------------

# Task3
a = 10
b = 14
c = 13
Result = (a+b) / 12 * c % 4 + b
print("\nResult(task_3) for a = %d, b = %d, c = %d is equal %d" %
      (a, b, c, Result))
#------------------------------------------------------------

# Task4
a = 101
b = 144
c = 155
Result = (a - b * c) / (a + b) % c
print("\nResult(task_4) for a = %d, b = %d, c = %d is equal %d" %
      (a, b, c, Result))
#------------------------------------------------------------

# Task5
a = 12
b = 11241
c = 123
Result = math.fabs(a - b) / (a + b)**3 - math.cos(c)
print("\nResult(task_5) for a = %d, b = %d, c = %d is equal %0.4f" %
      (a, b, c, Result))
#------------------------------------------------------------

# Task6
a = 115
b = 222
c = 666
Result = (math.log1p(1 + c) / -b)**4 + math.fabs(a)
print("\nResult(task_6) for a = %d, b = %d, c = %d is equal %d" %
      (a, b, c, Result))
#------------------------------------------------------------
