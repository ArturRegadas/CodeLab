n1 = int(input())
n2 = int(input())
if n1 - n2 < 0:
    n1 = n1 + n2
    n2 = n2 - n1
    n1 = n1 - n2
print(n1 - n2)