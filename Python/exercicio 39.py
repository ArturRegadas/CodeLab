print('\033[1;35m-='*36)
print('\033[0;31mvamos saber se voce esta ou não de recuperação')
not1=float(input('digite o valor da primeira nota \033[1;32m'))
not2=float(input('\033[0;31mdigite o valot da segunda nota\033[1;32m '))
ger=(not1+not2)/2
print('\033[1;35m-='*36)
if ger >=7 and ger <= 10:
    print('\033[0;33msua media foi de \033[1;32m{:.1f}\033[0;33m, voce foi APROVADO'.format(ger))
elif ger >= 5 and ger <=6.9:
    print('\033[0;33msua media foi de \033[1;32m{:.1f}\033[0;33m, voce está de recuperação'.format(ger))
elif ger < 4.9 and ger >=0:
    print('\033[0;33msua media foi de \033[1;32m{:.1f}\033[0;33m, voce foi reprovado'.format(ger))
else:
    print(' \033[1;31m  insira notas VALIDAS')
print('\033[1;35m-='*36)