num = int(input())
omes = "numero invalido"
meses = ("janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro")
if 1 <= num <= len(meses):
    omes = meses[num - 1]
print(omes)