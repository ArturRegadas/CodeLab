from time import sleep
print('\033[1;32mvamos saber quanto voce pagara em uma viagem promocional')
km=float(input('escreva quantos km sera sua viajem\033[1;33m'))
print('\033[1;34mprocessando informações.')
sleep(1)
print('\033[1;34mprocessando informações..')
sleep(1)
print('\033[1;34mprocessando informações...')
sleep(1)
print('\033[1;35m-=-'*20)
if km >= 201 :
    print('    \033[1;32msua viajem custara: \033[1;33mR${:.1f}'.format(km*0.45))
else:
    print('    \033[1;32msua viajem custara \033[1;33mR${:.1f}'.format(km*0.5))