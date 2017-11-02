import datetime

today = datetime.date.today()
format = "%a %b %d %H:%M:%S"

d = datetime.datetime.now()

print(today.month,'/',today.day,'/',today.year,' ',end='')
d = datetime.datetime.now()

print(d.hour,':',d.minute,':',d.second)