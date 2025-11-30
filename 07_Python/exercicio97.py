
frase=" "
def mostrar(txt):
    lenn = len(frase)+6
    print("-" * lenn)
    print(f"   {txt}   ")
    print("-"*lenn)
    print("")
while True:
    frase = str(input("digite algo (999-parar)"))
    if frase == "999":
        break


    mostrar(frase)




