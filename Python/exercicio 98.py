from time import sleep


def contagem():
    for i in range (0,10):

        if i+1==10:
            print(i + 1)
            print("")
        else:
            print(i+1, end=", ")

def contagem2():
    for o in range(-10,0):
        if o*-1==1:
            print(o * -1)
            print("")

        else:
            print(o*-1, end=", ")

def contagemper(v1, v2, v3):
    if v1 < v2:
        in2=v2

    #elif inicio == fim:

    #else:

contagem()
contagem2()

inicio=int(input("INICIO: "))
fim=int(input("FIM: "))
passo=int(input("PASSO: "))


contagemper(inicio, fim, passo)




