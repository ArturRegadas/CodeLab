from time import sleep
print('vamos saber como seria seu salario com um aumento')
sal=int(input('digite seu salario '))
print('pocessando.')
sleep(1)
print('processando..')
sleep(1)
print('processando...')
sleep(1)
if sal >= 1251:
    sal1=sal*10/100
    print('=-'*35)
    print('seu salario sera de R${}'.format(sal1+sal))
else:
    sal1=sal*15/100
    print('=-'*35)
    print('seu salario sera de R${}'.format(sal1+sal))
print('=-'*35)