from datetime import date
print('\033[1;35m-='*26)
print('\033[0;36mvamos saber em que categoria voce se encaixa')
ano=int(input('digite o ano em que voce nasceu\033[1;32m '))
atual=date.today().year
idade=atual-ano
print('\033[1;35m-='*26)
if idade <=9 and idade >= 0:
    print('\033[0;33mvoce foi classificado como \033[1;32mMIRIM\033[0;33m, já que voce tem \033[1;32m{}\033[0;33m ano(s)'.format(idade))
elif idade > 9 and idade <= 14:
    print('\033[0;33mvoce foi classificado como \033[1;32mINFANTIL\033[0;33m, já que voce tem \033[1;32m{}\033[0;33m anos'.format(idade))
elif idade > 14 and idade <= 19:
    print('\033[0;33mvoce foi classificado como \033[1;32mJUNIOR\033[0;33m,  já que voce tem \033[1;32m{}\033[0;33m anos'.format(idade))
elif idade > 19 and idade <= 25:
    print('\033[0;33mvoce foi classificado como \033[1;32mSÊNIOR\033[0;33m, já que voce tem \033[1;32m{}\033[0;33m anos'.format(idade))
elif idade > 25 and idade <= 150:
    print('\033[0;33mvoce foi classificado como\033[1;32m MASTER\033[0;33m, já que voce tem \033[1;32m{}\033[0;33m anos'.format(idade))
else:
    print('    \033[1;31mERROR\033[0;31m (insira uma data  valida)')
print('\033[1;35m-='*26)