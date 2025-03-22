from time import sleep
print('-='*35)
val1=int(input('digite um numero'))
print('-='*35)
val2=int(input('digite outro numero'))
print('-='*35)
val3=int(input('digite mais um numero'))
print('-='*35)
print('processando...')
sleep(1)
print('processando...')
sleep(1)
print('processando...')
sleep(1)
if val1-val2 >= 1:
    if val1-val3>=1:
        print('o maior valor foi {}'.format(val1))
else:
    if val2-val3 >= 1:
        print('o maior valor foi {}'.format(val2))
if val3 > val2 and val3 > val1:
    print('o maior valor é {}'.format(val3))
else:
    if val1 == val2 == val3:
        print('todos os numeros são iguais')
print('-='*35)
print('processando...')
sleep(1)
print('processando...')
sleep(1)
print('processando...')
sleep(1)
if val1-val2 <= -1:
    if val1 - val3 <= -1:
        print('o menor valor é {}'.format(val1))
else:
    if val2-val3 <= -1:
        print('o menor valor é {}'.format(val2))
if val3 < val2 and val3 < val1:
    print('o menor valor foi {}'.format(val3))
else:
    if val1==val2==val3:
        print('todos os numero são iguais')
print('-='*35)