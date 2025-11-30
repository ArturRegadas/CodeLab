print('\033[1;32m=-=-=-=-=-=\033[1;33mLOJAS\033[1;32m-=\033[1;33mLENIN\033[1;32m-=-=-=-=-=-=-')
print('\033[0;34mvamos fazer uma compra')
val=int(input('\033[0;34mqual po valor da compra: R$\033[1;33m'))
print('\033[0;34mescolha uma das opções:')
print('\033[1;32m=-'*18)
print('''\033[1;32m[1]\033[0;33m a vista dinheiro/cheque
\033[1;32m[2]\033[0;33m a vista cartão
\033[1;32m[3]\033[0;33m 2x no cartão
\033[1;32m[4]\033[0;33m 3x ou mais no cartão''')
opc=int(input('escolha uma das opções acima:\033[1;33m '))
print('\033[1;32m=-'*18)
if opc==1:
    rel=(val*10)/100
    print('''\033[0;34mo valor a se pagar sera de R$\033[0133m{:.0f}\033[0;34m, 
já que nesta opção há 10% de desconto'''.format(val-rel))
elif opc==2:
    rel=(val*5)/100
    print('''\033[0;34m\033[0;34mo valora se pagar será de R$ \033[0;34m{:.0f}\033[0;34m,
já que nesta opção há 5% de desconto'''.format(val-rel))
elif opc == 3:
    rel=val/2
    print('\033[0;34mvoce pagará 2 parcelas de R$\033[0;34m{:.0f}'.format(rel))
elif opc==4:
    par=int(input('\033[0;34mdigite em quantas parcelas deseja pagar\033[1;33m '))
    par1=(val*20)/100
    par2=par1+val
    rel= par2/par
    print('\033[0;34mvoce pagará em  \033[0;33m{:.0f}\033[0;34m parcelas de R$\033[1;33m{:.0f}\033[0;34m,'. format(par, rel))
    print('ao total voce pagara R$\033[1;33m{:.0f}'.format(par2))
else:
    print('   \033[1;31mERROR\033[0;31m (insira uma opção valida) ')
print('\033[1;32m=-'*18)