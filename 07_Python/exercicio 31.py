from datetime import date
print('vamos saber se um ano é bixesto')
ano=int(input('digite um ano, coloque 0 para analisar o ano atual '))
print('')
if ano == 0:
    ano=date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(' o ano de {} é bixesto'.format(ano))
else:
    print('o ano de {} não é bixesto'.format(ano))