from time import sleep
from random import choice
print('\033[1;35m=-'*18)
print('\033[0;33mvamos jogar pedra, papel e tesoura')
print('\033[1;35m=-'*18)
print('''\033[0;33m[1]pedra 
[2]papel
[3]tesoura''')
ale=choice(['tesoura', 'papel' , 'pedra'] )
opc=int(input('digite sua opção \033[1;31m'))
print('\033[1;35m=-'*18)
print('\033[0;33mpedra')
sleep(1)
print('papel')
sleep(1)
print('tesoura')
sleep(1)
print('\033[1;35m=-'*18+'\033[1;34m')
if opc ==1 and ale == 'tesoura':
    print('o computador jogou {}'.format(ale))
    print('voce ganhou!!!')
elif opc ==1 and ale== 'papel':
    print('o computador jogou {}'.format(ale))
    print('voce perdeu')
elif opc == 1 and ale == 'pedra':
    print('o computador jogou pedra')
    print('empate')
elif opc == 2 and ale == 'tesoura':
    print('o computador jogou tesoura')
    print('voce perdeu')
elif opc == 2 and ale == 'papel':
    print('o computador jogu papel')
    print('empate')
elif opc == 2 and ale == 'pedra':
    print('o computador jogou pedra')
    print('voce ganhou!!!')
elif opc == 3 and ale == 'tesoura':
    print('o computador jogou tesoura')
    print('empate')
elif opc == 3 and ale == 'papel':
    print('o computador jogou papel')
    print('voce ganhou!!!')
elif opc == 3 and ale == 'pedra':
    print('o computador jogou pedra')
    print('voce perdeu')
print('\033[1;35m=-'*18)