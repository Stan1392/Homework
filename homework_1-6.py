import math
#Integration
# Task1
a = 10
b = 14
c = 13
result = a + b * (c / 2)
print("\nResult(task_1) for a = %d, b = %d, c = %d is equal %d" %
      (a, b, c, result))
#------------------------------------------------------------

#Task2
a = 2
b = 1
result = (a**2 + b**2) % 2
print('\nResult(task_2) for a = %d and b = %d is equal %d' %
      (a, b, result))
#------------------------------------------------------------

# Task3
a = 10
b = 14
c = 13
result = (a+b) / 12 * c % 4 + b
print("\nResult(task_3) for a = %d, b = %d, c = %d is equal %d" %
      (a, b, c, result))
#------------------------------------------------------------

# Task4
a = 101
b = 144
c = 155
result = (a - b * c) / (a + b) % c
print("\nResult(task_4) for a = %d, b = %d, c = %d is equal %d" %
      (a, b, c, result))
#------------------------------------------------------------

# Task5
a = 12
b = 11241
c = 123
result = math.fabs(a - b) / (a + b)**3 - math.cos(c)
print("\nResult(task_5) for a = %d, b = %d, c = %d is equal %0.4f" %
      (a, b, c, result))
#------------------------------------------------------------

# Task6
a = 115
b = 222
c = 666
result = (math.log1p(1 + c) / -b)**4 + math.fabs(a)
print("\nResult(task_6) for a = %d, b = %d, c = %d is equal %d" %
      (a, b, c, result))
#------------------------------------------------------------
