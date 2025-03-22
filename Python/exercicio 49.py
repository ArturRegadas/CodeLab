s=0
print('\033[0;33mvamos saber a tabuada de um numero')
num=int(input('digite um numero \033[1;33m'))
for z in range(0, 10):
    s=s+1
    x=s+0
    print('\033[1;35m{}x{}={}'.format(num, x, num*x))