from random import choice
from time import sleep
print('\033[31mvamos fazer um jogo')
print('tente adivinhar um numero entre 1 e 5')
print('')
z=input('digite um numero \033[1;31m')
print('')
x= choice(['1', '2', '3', '4', '4'])
print('\033[0;33mPROCESSANDO...')
sleep(4)
print('\033[31mo numero escolhido foi \033[1;31m{}'.format(x))
print('\033[35m=-='*17)
print('\033[0;33mPROCESSANDO...')
sleep(2)
if x == z:
	print('\033[32mvoce ganhou')
else:
	print('\033[32mvoce perdeu')