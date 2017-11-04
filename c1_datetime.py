import datetime

tb = datetime.datetime.today()

today = datetime.date.today()

print('start time: ',tb)
print('ctime:', today.ctime())
print('tuple:', today.timetuple())
print('to ordinal:', today.toordinal())
ordinal = today.toordinal()

days = 300
print('from ordinal:', today.fromordinal(ordinal+days))

print('Year:', today.year)
print('Mon :', today.month)
print('Day :', today.day)

print('Now    :', datetime.datetime.now())
print('Today  :', datetime.datetime.today())
print('UTC Now:', datetime.datetime.utcnow())

format = "%a %b %d %H:%M:%S %Y"
#format = "%H:%M:%S"

print('ISO     :', today)

s = today.strftime(format)
print('strftime:', s)

d = datetime.datetime.strptime(s, format)
print('strptime:', d.strftime(format))

toe = today.toordinal()
te = datetime.datetime.today()
print('end time: ',te)
print('start - end time: ', te - tb)
