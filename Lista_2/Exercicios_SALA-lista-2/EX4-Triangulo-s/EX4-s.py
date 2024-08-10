l1 = float(input())
l2 = float(input())
l3 = float(input())
st = "NÃO É UM"
tp = ""
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    st = "É UM"
    if l1 == l2 == l3:
        tp = "EQUILÁTERO"
    elif l1 != l2 and l2 != l3 and l1 != l3:
        tp = "ESCALENO"
    else:
        tp = "ISÓSCELES"
print(f"{st} triângulo {tp}")