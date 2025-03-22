medidas=[]
def area():
    medidas.append(medidas[0]*medidas[1])



medidas.append(int(input("LARGURA (m) ")))
medidas.append(int(input("CUMPRIMENTO (m) ")))
area()

print(f"A área de um terrno {medidas[0]}x{medidas[1]} é {medidas[2]}m².")

