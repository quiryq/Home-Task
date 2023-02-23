import datetime

f_day = int(input("enter the day of the first date "))
f_month = int(input("enter the month of the first date "))
f_year = int(input("enter the year of the first date "))

s_day = int(input("enter the day of the second date "))
s_month = int(input("enter the month of the second date "))
s_year = int(input("enter the year of the second date "))

first_date = datetime.datetime(f_year, f_month, f_day)
second_date = datetime.datetime(s_year, s_month, s_day)

if first_date > second_date:
    print((first_date - second_date).days * 86400)

else:
    print((second_date - first_date).days * 86400)