from random import randint
class NavalGame:
    def __init__(self, height:int, widht:int, qtdBoats:int) -> None:
        self._board = [[False for i in range(widht)]for i in range(height)]
        self._boardPlay =[["."]*widht for i in range(height)]
        self._height = height
        self._widht = widht
        self._boats = 0
        for i in range(qtdBoats):
            y = randint(0, height-1)
            x = randint(0, widht-1)

            if (not self._board[x][y]):
                self._board[x][y] = True
                self._boats+=1
            
    def getBoats(self):
        return self._boats

    def play(self, x:int, y:int) -> bool:
        x-=1
        y-=1
        if x < 0 or x >= self._height or y < 0 or y >= self._widht:
            return False
        self._boardPlay[y][x] = "O" if self._board[y][x] else "X"
        for i in self._boardPlay:
            for j in i:
                print(j, end="")
            print()
        if(self._board[y][x]):
            print("acertou")
            self._boats-=1
            return False
        print("errou")
        return True
    

def main():
    navalGame = NavalGame(5, 5, 3)
    while(1):
        x, y = list(map(int, input("[x y]").split()))
        navalGame.play(x, y)
        if(navalGame.getBoats() <=0):
            print("ganhou")
            break

main()