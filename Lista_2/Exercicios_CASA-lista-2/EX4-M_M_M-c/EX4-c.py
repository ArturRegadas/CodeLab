n1 = int(input())
n2 = int(input())
n3 = int(input())
l1 = []
l1.append(n1)
l1.append(n2)
l1.append(n3)
l=sorted(l1)
print(f"o maior número é {l[2]}, o menor é {l[0]}, e o do meio é {l[1]}")