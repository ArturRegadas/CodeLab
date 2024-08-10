Nhrs=0
sals = []
sal = float(input())
hrs = float(input())

while True:
    salbrut=sal
    if sal > 1600:
        nsal = sal - (22 * sal / 100)
    elif sal >= 800:
        nsal = sal - (13 * sal / 100)
    else:
        nsal = sal
    if hrs > 160:
        Nhrs = (salbrut/160)*0.5*(hrs-160)
    else:
        Nhrs = 0

    sals.append(nsal + Nhrs)
    print(f"o salário líquido desse funcionário é {nsal + Nhrs}")

    sal = float(input())
    if sal <= 0:
        break
    hrs = float(input())

print(f"o total de salários líquidos foi de {sum(sals)}")