#Task 7
european_date = '13.01.1992'
print('\nEuropean date -', european_date)
european_date_lst =european_date.split('.')
day   = int(european_date_lst[0])
month = int(european_date_lst[1])
year  = int(european_date_lst[2])
american_year = ('%d.%d.%d') % \
                (month, day, year)
print("\nAmerican date -", american_year)