n = []
n.append(int(input()))
n.append(int(input()))
n.append(int(input()))
L2 = []
L3 = []
for i in n:
    if i % 4 == 0:
        L2.append(i)
    if i % 5 == 0:
        L3.append(i)
print(f"números divisíveis por 4: {L2}")
print(f"números divisíveis por 5: {L3}")
