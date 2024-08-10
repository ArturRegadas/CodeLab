n = []
n.append(int(input()))
n.append(int(input()))
n.append(int(input()))
L2 = []
L3 = []
for i in n:
    if i % 2 == 0:
        L2.append(i)
    if i % 3 == 0:
        L3.append(i)
print(f"números divisíveis por 2: {L2}")
print(f"números divisíveis por 3: {L3}")