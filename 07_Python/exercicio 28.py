from time import sleep
print('\033[36mvoce esta andando a quantos km/h?')
vel=int(input(' escreva sua velocidade\033[1;36m '))
z=vel-80
print('\033[0;33mprocessando.')
sleep(1)
print('\033[33mprocessando..')
sleep(1)
print('\033[33mprocessando...')
sleep(1)
if  vel >= 81:
	print('\033[36mvoce sera \033[1;36mmultado\033[0;36m, nesta rodovia o limite de km/h é de 80km/h')
	print('vá mais devagar da proxima vez, a multa saira no valor de R$\033[1;34m{}'.format(z*7))
else:
		print('\033[1;36mvoce esta na velocidade ideal')