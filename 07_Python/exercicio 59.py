num1=int(input('digite o primeiro numero'))
num2=int(input('digite o segundo numero'))
print('''[1] SOMAR OS NUMEROS
[2] MULTIPLICAR OS NUMEROS 
[3] MAIOR NUMERO
[4] NOVOS NUMEROS 
[5] ENCERRAR PROGRAMA''')
opc=int(input('escolha uma das opções'))

while opc != 5 and opc <5:
    if opc == 1:
        print('a soma entre {} + {} é de {}'.format(num1, num2, num1+num2))
        print('')
        print('''[1] SOMAR OS NUMEROS
[2] MULTIPLICAR OS NUMEROS 
[3] MAIOR NUMERO
[4] NOVOS NUMEROS 
[5] ENCERRAR PROGRAMA''')
        opc = int(input('escolha uma nova opção'))
    elif opc == 2 :
        print('a multiplicação entre {} x {} é {}'.format(num1, num2, num1*num2))
        print('')
        print('''[1] SOMAR OS NUMEROS
[2] MULTIPLICAR OS NUMEROS 
[3] MAIOR NUMERO
[4] NOVOS NUMEROS 
[5] ENCERRAR PROGRAMA''')
        opc = int(input('escolha uma nova opção'))
    elif opc == 3 :
        if num1 > num2:
            print('o maior numero é o numero {}'.format(num1))
        else:
            print('o meior numero é o numero {}'.format((num2)))
        print('')
        print('''[1] SOMAR OS NUMEROS
[2] MULTIPLICAR OS NUMEROS 
[3] MAIOR NUMERO
[4] NOVOS NUMEROS 
[5] ENCERRAR PROGRAMA''')
        opc = int(input('escolha uma nova opção'))
    elif opc == 4:
        num1 = int(input('digite o primeiro numero'))
        num2 = int(input('digite o segundo numero'))
        print('')
        print('''[1] SOMAR OS NUMEROS
[2] MULTIPLICAR OS NUMEROS 
[3] MAIOR NUMERO
[4] NOVOS NUMEROS 
[5] ENCERRAR PROGRAMA''')
        opc = int(input('escolha uma nova opção'))
if opc > 5 :
    print('insira uma opção valida')
print('o programa foi finalisado')