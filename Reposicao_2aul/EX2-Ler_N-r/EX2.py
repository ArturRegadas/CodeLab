soma = 0
f1 = f2 = f3 = f4 = f5 = 0
fs1=fs2=fs3=fs4=fs5=0
par = imp = 0
n = 0
maior = float('-inf')
escolha='s'
while (escolha!='n'):
    num=int(input("digite um numero: "))
    escolha=input("Continuar [s/n]")
    nu = int(num)
    soma += nu
    n += 1
    if nu > maior:
        maior = nu
    if nu < 0:
        f1 += 1
        faixa = 1
        fs1+=num
    elif 0 <= nu < 15:
        f2 += 1
        faixa = 2
        fs2+=num
    elif 15 <= nu < 100:
        f3 += 1
        faixa = 3
        fs3+=num
    elif nu >= 1000:
        f4 += 1
        faixa = 4
        fs4+=num
    elif 101 <= nu < 1000:
        f5 += 1
        faixa = 5
        fs5+=num
    
    if nu % 2 == 0:
        par += 1
        par_ou_impar = "par"
    else:
        imp += 1
        par_ou_impar = "ímpar"

    print(f"O número {nu} é {par_ou_impar}")
    print(f"O número {nu} está na faixa {faixa}")

print(f"\nA média foi de {soma / n:.2f}")
print(f"O maior número foi {maior}")


print(f"Ao todo foram:")
print(f"Faixa 1: {f1}, soma: {fs1}")
print(f"Faixa 2: {f2}, soma: {fs2}")
print(f"Faixa 3: {f3}, soma: {fs3}")
print(f"Faixa 4: {f4}, soma: {fs4}")
print(f"Faixa 5: {f5}, soma: {fs5}")

print(f"Ao todo foram {par} números pares e {imp} números ímpares")

print() 
