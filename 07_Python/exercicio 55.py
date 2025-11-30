maior=0
menor=0
print('vamos sabe qul foi o maior peso')
for z in range (1, 6):
    peso=float(input('qual o peso da {}° pessoa '.format(z)))
    if z == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('''o maior peso lido foi {}, 
já o menor foi {}'''.format(maior, menor))