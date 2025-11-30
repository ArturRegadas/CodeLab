num1=0
x=0
resp='s'
num=0
while resp != 'n':
    num2=num
    num=int(input('digite um numero'))
    if num > num2:
        maior1=num
        menor1=num2
    else:
        maior1=num2
        menor1=num

    x=x+1
    num1=num1+num
    resp = str(input('deseja continuar [s/n]'))
print("""voce somou {} numeros que ao todo deu {}, a media das somas foi {}
 O maior numero foi {} e o menor {}""".format(x, num1, num1/x, maior, menor))