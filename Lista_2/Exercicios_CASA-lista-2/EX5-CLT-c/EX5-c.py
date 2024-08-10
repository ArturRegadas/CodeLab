Nhrs=0
sals = []
sal = float(input())
hrs = float(input())

while sal <= 0:
    if sal >= 1600:
        nsal = sal - (13 * sal / 100)
    elif sal > 1600:
        nsal = sal - (22 * sal / 100)
    else:
        nsal = sal

    if hrs > 160:
        Nhrs = (hrs - 160) * 100 / 160
        Nhrs = (hrs * sal) / 100
    else:
        Nhrs = 0

    sals.append(nsal + Nhrs)
    print(f"o salário líquido desse funcionário é {nsal + Nhrs}")

    sal = float(input())
    hrs = float(input())

print(f"o total de salários líquidos foi de {sum(sals)}")