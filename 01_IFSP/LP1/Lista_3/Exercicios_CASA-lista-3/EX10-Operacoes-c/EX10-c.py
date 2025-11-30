while (escolha:=input().upper())!= "P":
    if escolha == "+":
        print(int(input())+int(input()))
    elif escolha == "-":
        print(int(input())-int(input()))
    elif escolha =="*":
        print(int(input())*int(input()))
    elif escolha =="/":
        print(int(input())/int(input()))
    else:
        print("Opcao Invalida")