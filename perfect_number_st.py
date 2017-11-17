import datetime

r = 1000000 
n = r
i = 2

print('Print the first perfect numbers in:',r,)
start_time = datetime.datetime.today()
print(start_time)

for j in range (1,r):
	p = 1
	perfect = []
	perfect.append(p)

	while (i < n): 
		if (n % i == 0):
			p += n / i
			perfect.append(int(n/i))
		i += 1

	if p == n:
		print('\n',sorted(perfect),': ',n,'Is a perfect number')
	#else:
	#	print(n, 'Is an imperfect number')

	i = 2
	n -= 1
	print(datetime.datetime.today())

end_time = datetime.datetime.today()
print(end_time)
print('Total time:', end_time - start_time)
