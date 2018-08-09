#Task 8
student_name = 'Stanislav Chernyshev'
print(student_name)
student_name_lst = student_name.split(' ')
first_name = student_name_lst[0]
last_name = student_name_lst[1]
correct_student_name = ("%s %s") % (last_name, first_name)
print(correct_student_name)