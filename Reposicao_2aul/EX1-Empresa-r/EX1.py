
nome = input("Funcionário: ")
sa = float(input("Salario: "))
if sa <= 400.00:
    pct = 15
elif sa <= 700.00:
    pct = 12
elif sa <= 1000.00:
    pct = 10
elif sa <= 1800.00:
    pct = 7
elif sa <= 2500.00:
    pct = 4
else:
    pct = 0
ns = sa + (sa * pct / 100)
print(f"Nome do funcionário: {nome}")
print(f"% de aumento: {pct}%")
print(f"Salário atual: R$ {sa:.2f}")
print(f"Novo salário: R$ {ns:.2f}")
