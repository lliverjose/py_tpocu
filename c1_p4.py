'''
birth = 7
death = 13
immigrant = 35
days = 365
population = 307357870
'''
birth = 8
death = 11
immigrant = 32
days = 365.25
population = 307357870


year = input('Enter number of years:')
y = int(year)

s = (y * days * 24 * 60 * 60)
b = s/birth
d = s/death
i = s/immigrant

p = b + i - d

year = 'years'
if y == 1: year = 'year'

print('****** US Census Estimates *******')
print('   1 birth every:', birth,'seconds')
print('   1 death every:',death,'seconds')
print('   1 immigrants every:',immigrant,'seconds')
print('   initial population:',population)
print('**********************************')
print()

net_p = ((1/birth) + (1/immigrant) - (1/death)) * 3600
print('   Net gain:',net_p,'per hour')
net_p *= 24
print('   Net gain:',net_p,'per day')

print('   Estimated population [',p,'] population in [',y,'] ',year)
print('   Current population:',p+population)
print()