z=0
print(' vamos saber se um numero é primo')
num=int(input('digite um numero '))
for c in range(1, num+1):
    if num%c==0:
        print('\033[2;33m', end = ' ')
        z=z+c-c+1
    else:
        print('\033[m', end = ' ')
    print(c, end = ' ')
if z==2:
    print('''\033[m
no numero {} existe {} numeros divisiveis, seu numero é primo'''.format(num, z))
else:
    print('''\033[m
no numero {} existe {} numeros divisiveis, seu numero não é primo'''.format(num, z))