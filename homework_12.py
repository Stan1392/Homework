# Task 12
# a) using strings
def sum_of_digits(number):
    n1 = int(number[:1])
    n2 = int(number[1:2])
    n3 = int(number[2:])
    result = n1 + n2 + n3
    return result

sum = sum_of_digits("123")
print('\nSum of digits \'123\' = %d' % (sum))

#---------------------------------------
# b) without strings
def sum_of_digits(number):
    n1 = number // 100
    n2 = number // 10 % 10
    n3 = number % 10
    result = n1 + n2 + n3
    return result

sum = sum_of_digits(123)
print('\nSum of digits \'123\' = %d' % (sum))