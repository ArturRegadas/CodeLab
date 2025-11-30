print('\033[35mvamos saber se seu numero é impar ou par')
num=int(input('digite um numero \033[1;35m'))
num1= num %2
if num1 == 0:
    print('\033[33mseu numero é par')
else:
    print('\033[33mseu numero é impar')