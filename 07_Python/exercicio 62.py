print('vamos fazer a PA de um numero')

termo=int(input('digite a primeiro termo'))
razao=int(input('digite a razao'))
soma=termo
for z in range (0, 10):
    print(soma, end='->')
    soma=soma+razao
print(soma,end='->PAUSA')
ntermo=1
tempos=11
print('')
while ntermo != 0 :
    ntermo=int(input('quantos termos a mais voce quer'))
    print('')
    tempos=tempos+ntermo
    for bl in range(0, ntermo):
        print(soma, end='->')
        soma = soma + razao

print('')
print('o numero de termos mostrados foi de ', tempos)

