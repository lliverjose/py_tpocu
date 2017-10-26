'''
str_s = input('input a str = ')
str_i = input('input an int = ')
str_f = input('input a float = ')
print(str_s)
print(str_i)
print(str_f)

a = 10
b = 5
print('a//b = ', a // b)
print('a%b = ' , a %  b)
print('a**b = ', a ** b)
a *= b
print('a*=b = ', a )
'''

m = 0
n = 5
for i in range(4):
    m += n
    n = 5

    for j in range(i):
        n *= n
    print(n)
    print(m)
