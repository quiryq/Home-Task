import datetime

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1)

print(yesterday, today, tomorrow, sep="\n")