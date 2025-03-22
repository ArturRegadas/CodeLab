s=0
d=0
from datetime import date
print('vamos saber quem é mior de idade')
for z in range(1, 7):
    data=int(input('digite em que ano a {}º pessoa nasceu '.format(z)))
    atual=date.today().year
    idade=atual-data
    if idade >=18 and idade < 150:
        s=s+1
    elif idade < 18 and idade >=0:
        d=d+1
    else:
        print('insira uma data valida')
print('''hexistem {} pessoas maiores de idade e;
{} menores de idade'''.format(s, d))
