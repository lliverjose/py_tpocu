#c1_e40.py

import math

from string import ascii_lowercase, ascii_uppercase
def lowerChar(c):
	if 'A' <= c <= 'Z':
		return ascii_lowercase[ascii_uppercase.index(c)]
	else:
		return c

print('Weight (mass) option')
print('\t[K] Kilogram')
print('\t[P] Pound')
wo = input('Enter option = ')

wo = lowerChar(wo)
wo_str = 'pounds'
#if (wo == 'K' or wo == "k"): 
if (wo == "k"): 
	wo_str = 'kilogram'

print('Enter weight in',wo_str)
weight = input('weight = ')

print('Height option')
print('\t[M] Meter')
print('\t[F] Feet')
print('\t[I] Inches')
ho = input('Enter option = ')

ho = lowerChar(ho)

if (ho == 'm'):
	ho_str = 'meter'
elif (ho == 'f'):
	ho_str = 'feet'
else:
	ho_str = 'inches'

print('Enter height in',ho_str)
height = input('Enter height = ')

w = float(weight)
h = float(height)



if (wo == 'k' and (ho == 'f' or ho == 'i')):
	if ho == 'f':
		h /= 3.2808
	else:
		 h /= 39.37
	ho_str = 'meter'

if (wo == 'p' and ho == 'm'):
	if ( ho == 'm'):
		w *= 0.45359237
		wo_str = 'kilogram'

bmi = w / pow(h,2)

print('Your weight = ',w,wo_str)
print('Your height = ',h,ho_str)

print('Your BMI = ',bmi)
