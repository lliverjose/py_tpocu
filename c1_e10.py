import math

wifes = input('Wifes traveling = ')
sacks = input('Sacks per wife = ')
cats = input('Cats per sack = ')
kittens = input('Kittens per cat = ')

w = int(wifes)
c = int(cats)
s = int(sacks)
k = int(kittens)

n = ((c * k) + c) * s * w + w + 1

print(n)