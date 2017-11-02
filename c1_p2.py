import datetime 

launched_date = datetime.date(1977,9,15)
base_date = datetime.date(2009,9,25)
base_dist = 16637000000		#distance from the sun at base_date since launch
km = 1.609344
au = 92955807.267433 
voyager_speed = 38241		#38241 miles/hour
light_speed = 299792458 	#meters / second
blank_days = False
meters = 1609.344			#1 mile = 1609.344 meters
d2s = 86400					#1 day = 86,400 seconds

ldo  = launched_date.toordinal()
bdo  = base_date.toordinal()
today = datetime.date.today()

print()
print('*********** Voyager 1 NASA Status ************')
print('Lauched date:',launched_date)
print('Base calculation date:',base_date)
print('Traveling speed:',voyager_speed,'miles/hour')
print('Traveled distance:',base_dist)
print('**********************************************')
print()

days_str = input('Enter days traveled: ')
if days_str == '':
	print("Days field entered blank, assumming today's date.")
	days = today.toordinal() - bdo
	blank_days = True
else:
	days = int(days_str)

distance = (voyager_speed * 24) * days 		#distance in miles

ldfo = launched_date.fromordinal(ldo+days)
bdfo = base_date.fromordinal(bdo+days)

day_str = 'day'
if days > 1: day_str = 'days'
print()
print('Base date period [',base_date,'to',bdfo,']')
print('  Traveled:',days,day_str)
print('  Distance:',distance,'miles')
print('  Distance:',distance*km,'km')
print('  Distance:',distance/au,'AU')

distance += base_dist
print()
print('Launched date period [',launched_date,'to',bdfo,']')
print('  Traveled:',days+bdo,'days')
print('  Distance:',distance,'miles')
print('  Distance:',distance*km,'km')
print('  Distance:',distance/au,'AU')

radio_com = ((distance*meters)/light_speed) * 2
print()
print('Round trip time for radio communication')
print('  :',radio_com,'second')
print('  :',radio_com/60,'minutes')
print('  :',radio_com/(60*60),'hours')
