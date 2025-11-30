s=0
m=0
maior = 0
for z in range( 1, 5):
    print('{} {}º PESSOA {}'.format('='*5, z, '='*5))
    nome=input('digite o nome da {}º pessoa '.format(z))
    idade=int(input('digite a idade da {}ºpessoa '.format(z)))
    sexo=input('digite o sexo da {}º pessoa(F/M) '.format(z)).lower()
    s=s+idade
    if sexo == 'm':
        if idade > maior:
            maior = idade
            n=nome
    if sexo == 'f':
        if idade < 20:
            m=m+1
print('')
print('a média de idade do grupo é {}'.format(s/4))
print('o homem mais velho é o {} com {} anos'.format(n, maior))
print('ao todo {} mulheres tem menos de 20 anos'.format(m))