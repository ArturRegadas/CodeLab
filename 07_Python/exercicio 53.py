m=0
frase1=''
print('vamos saber se uma frase é um palindromo')
frase=str(input('escreva uma frase'))
frase=frase.replace(' ', '').lower()
x=len(frase)
print('a frase {} ao contrario é '.format(frase), end =''),
for z in range(x, 0, -1):
    frasec=frase[m+z-1]
    frase1=frase1+frasec
    print(frasec, end='')
print('')
if frase==frase1:
    print('sua frase é um polindromo')
else:
    print('sua frase não é um polindromo')