from random import randint
class ChoiceAtributes:
    def __init__(self, win:int, defeat:int, draw:int) -> None:
        self._win = win
        self._defeat = defeat
        self._draw = draw
       
    def getWin(self) -> int:
        return self._win
   
    def getDefeat(self) -> int:
        return self._defeat
       
    def getDraw(self) -> int:
        return self._draw
   
class JokenpoGame:
    def __init__(self) -> None:
        self._choices = {
            1:ChoiceAtributes(2, 3, 1), #paper
            2:ChoiceAtributes(3, 1, 2), #rock
            3:ChoiceAtributes(1, 2, 3)  #scissor
        }
   
    def play(self, p1:int, p2:int) -> None:
        if False in [i in [1, 2, 3] for i in [p1, p2]]:
            print("escolhas invalidas")
        elif self._choices[p1].getWin() == p2:
            print("p1 ganhou")
        elif self._choices[p1].getDraw() == p2:
            print("empate")
        else:
            print("p2 ganhou")

def main():
    jokenpoGame = JokenpoGame()
    while ((a :=input("p -> parar: ")) != "p"):
        p1, p2 = list(map(int, input("1-papel\n2-pedra\n3-tesoura\np1 p2: ").split()))
        jokenpoGame.play(p1, randint(1, 3))
main()
