print('\033[1;35m=-'*35)
print('\033[0;33mvamos saber qual numero é maior')
num1=int(input('digite um numero \033[1;32m'))
num2=int(input('\033[0;33mdigite o segundo numero\033[1;32m '))
print('\033[1;35m=-'*35)
if num1 > num2:
    print('\033[0;33mo primeiro numero é maior ')
elif num2 > num1:
    print('\033[0;33mo segundo numero é o maior')
elif num1 == num2:
    print('\033[0;33mos dois numeros são iguais')