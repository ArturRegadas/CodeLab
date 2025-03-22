num=int(input('digite um numero, [999 para parar] '))
num1=0
x=0
while num != 999:
    x=x+1
    num1=num1+num
    num=int(input('digite um numero, [999 para parar]'))
print('voce somou {} numeros que ao todo deu {}'.format(x, num1))