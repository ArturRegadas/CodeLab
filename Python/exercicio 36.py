print('\033[31mvamos fazer um convesor numerico')
print('\033[1;35m=-\033[m'*35)
print('\033[0;31m[1]para conversor BINARIO')
print('[2]para conversor OCTAL ')
print('[3]para conversor HEXADECIMAL')
print('\033[1;35m=-\033[m'*35)
opc=int(input('\033[0;31mescolha sua opção \033[1;31m'))
num=int(input('\033[0;31mescreva o numero a ser convertido \033[1;31m'))
print('\033[1;35m=-\033[m'*35)
if opc==1:
    num1=bin(num)
    num1=num1.replace('0b','')
    print('\033[0;31mo numero \033[1;31m{}\033[0;31m convertido para binario fica:\033[0;31m{}'.format(num, num1))
elif opc==2:
    num1=oct(num)
    num1=num1.replace('0o','')
    print('\033[31mo numero \033[1;31m{}\033[0;31m convertido para octal fica: \033[1;31m{}'.format(num, num1))
elif opc==3:
    num1=hex(num)
    num1=num1.replace('0x','')
    print('\033[31mo numero \033[1;31m{}\033[0;31m convertido para hexadecima fica \033[1;31m{}'.format(num, num1))
print('\033[1;35m=-\033[m'*35)
else:
    print('numero de opção ilegivel')