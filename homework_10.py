name_and_dates = 'Alexander Blok*1880-16-11*1921-08-07'
print('name and dates -', name_and_dates)
name_and_dates_lst = name_and_dates.split('*')
birthday     = name_and_dates_lst[1]
death        = name_and_dates_lst[2]
birthday_lst = birthday.split('-')
death_lst    = death.split('-')
age = int(death_lst[0]) - int(birthday_lst[0])
name_and_age = name_and_dates_lst[0], age
print('\nname and age -', name_and_age)
