import datetime

today_date = datetime.datetime.now()

ms = today_date.strftime("%f")

today_without_ms = today_date - datetime.timedelta(microseconds = int(ms))

print(today_without_ms)