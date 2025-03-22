num = int(input())
omes = "numero invalido"
meses=("Engenharia","Edificações","Sistemas Elétricos","Turismo","Análise de Sistemas")
if 1 <= num <= len(meses):
    omes = meses[num - 1]
print(omes)