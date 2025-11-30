print('vamos fazer a fatoração de um numero')
num=int(input('digite um numero'))
n=1
for z in range(num, 0, -1):
    if z != 1 :
        print('{} x'.format(z), end=' ')
        n=n*z
    else:
        print(' 1 = {}'.format(n))
