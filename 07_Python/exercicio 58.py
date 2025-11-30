from random import choice
from time import sleep
w=1
print('\033[31mvamos fazer um jogo')
print('tente adivinhar um numero entre 1 e 5')
print('')
vc=input('digite um numero \033[1;31m')
print('')
pc= choice(['1', '2', '3', '4', '4'])
print('\033[0;33mPROCESSANDO...')
sleep(4)
print('\033[31mo numero escolhido foi \033[1;31m{}'.format(pc))
print('\033[35m=-='*17)
print('\033[0;33mPROCESSANDO...')
sleep(2)
while vc != pc:
	pc = choice(['1', '2', '3', '4', '4'])
	print('tente novamente')
	vc=str(input('voce escolheu o numero errado, tente novamente digitando outro numero'))
	print('o computador escolheu um novo numero, que é o numero {}'.format(pc))
	print('')
	w +=1
if vc == pc:
	print('voce acertou o numero, parabens')
print('voce precisou de {} tentarivas'.format(w))