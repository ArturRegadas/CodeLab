s=0
print('\033[1;34ma soma de todos os numeros impares divididos por 3 é:\033[1;35m')
for x in range(1, 500):
    if x%2 == 1 and x%3==0:
        s=s+x
print(s)