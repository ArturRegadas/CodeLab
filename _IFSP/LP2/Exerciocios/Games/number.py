from random import randint
class NumberGame:
    def __init__(self) -> None:
        pass
    
    def play(self, number:int) -> None:
        machine=randint(1, 5)
        print("a maquina escolheu", machine)
        print("voce ganhou" if machine == number else "voce perdeu")

def main():
    numberGame = NumberGame()
    numberGame.play(int(input("escolha um numero entre 1 e 5: ")))
main()
        