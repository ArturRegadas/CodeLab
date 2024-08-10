n1 = float(input())
n2 = float(input())
n3 = float(input())
situacao = "reprovado"
if (n1 + n2 + n3) / 3 >= 6:
    situacao = "aprovado"
print(f"O aluno foi {situacao} com a média {(n1 + n2 + n3) / 3:.2f}")