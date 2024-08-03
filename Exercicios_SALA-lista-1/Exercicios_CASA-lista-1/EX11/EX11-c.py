a = input()
b = input()
a += b
tamanho_a = len(a)
tamanho_b = len(b)
b = a[:tamanho_a - tamanho_b]
a = a[tamanho_a - tamanho_b:]
print("a:", a)
print("b:", b)