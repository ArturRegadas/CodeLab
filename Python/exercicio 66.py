n=0
x=0
num=0
num2=0
while True:
    num=int(input('digite um numero [999 para parar]'))
    x=x+1
    num2=num2+num
    if num == 999:
        break
print(f'no total tiveram {x-1} numeros, que ao todo resultam em {num2-999}')