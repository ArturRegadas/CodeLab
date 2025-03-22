s=0
q=0
print('\033[1;32mvamos somar todos os numeros impares ')
for z in range(0, 6):
    num=int(input('digite um numero \033[1;33m'))
    if num%2==0:
        num=num
        q=q+1
    else:
        num=0
        q+=0
    s=s+num
print('\033[1;32mvoce informou \033[1;33m{}\033[1;32m numero(s) par(es), a soma entre els é de : \033[1;33m{}\033[1;32m'.format(q, s))