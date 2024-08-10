n1 = float(input())
n2 = float(input())
situacao = "aprovado"
n3 = 0
if (n1 + n2) / 2 < 6:
    n3 = float(input())
    if (n1 + n2 + n3) / 3 < 5:
        situacao = "reprovado"
print(f"O aluno foi {situacao} com a média {(n1 + n2 + n3) / 3}")

