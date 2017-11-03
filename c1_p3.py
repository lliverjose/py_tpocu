#constants
barrel = 19.5 		#1 ballel of oil produces 19.5 gallons of gasoline
CO2 = 20			#1 gallon of gasoline produces 20 pounds of CO2 when burned
BTU = 115000		#1 gallon of gasoline contains 115000 BTU of energy
ethanol = 75700		#1 gallon of ethanol contains 75700 BTU of energy
liter = 3.78541		#1 gallon = 3.78541 liter 
price = 2.753		#price per gallon

gasoline = input('Enter gallons of gasoline:')
g = float(gasoline)

l = liter * g
b = g / barrel
c = g * CO2
e = g * ethanol
p = g * price

print()
print('You entered:',g,'gallons of gasoline')
print('[',l,'] liters')
print('[',b,'] barrels of oil to make [',g,'] gallons of gasoline')
print('[',c,'] pounds of CO2 produced')
print('[',e,'] energy amount of ethanol gallons')
print('[',p,'] price in U.S. dollars')
print()