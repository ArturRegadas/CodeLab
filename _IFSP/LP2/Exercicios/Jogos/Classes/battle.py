from random import randint, choice

class Ship:
    def __init__(self, positions:int) -> None:
        self._positions = positions
        self._hits = set()

    def isAt(self, y:int, x:int) -> bool:
        return (y, x) in self._positions

    def registerHit(self, y:int, x:int) -> None:
        if self.isAt(y, x):
            self._hits.add((y, x))

    def isSunk(self) -> bool:
        return set(self._positions) == self._hits


class NavalGame:
    def __init__(self, height:int, width:int, numShips:int, shipSize:int) -> None:
        self._height = height
        self._width = width
        self._board = [["." for _ in range(width)] for _ in range(height)]
        self._ships = []
        self._placeShips(numShips, shipSize)

    def _placeShips(self, numShips:int, shipSize:int) -> None:
        count = 0
        while count < numShips:
            horizontal = choice([True, False])
            if horizontal:
                x = randint(0, self._width - shipSize)
                y = randint(0, self._height - 1)
                positions = [(y, x + i) for i in range(shipSize)]
            else:
                x = randint(0, self._width - 1)
                y = randint(0, self._height - shipSize)
                positions = [(y + i, x) for i in range(shipSize)]

            if all(not any(ship.isAt(py, px) for ship in self._ships) for py, px in positions):
                self._ships.append(Ship(positions))
                count += 1

    def showBoard(self) -> None:
        for i in range(self._height):
            print(" ".join(self._board[i]))
        print()

    def play(self, y:int, x:int) -> str:
        y -= 1
        x -= 1
        if not (0 <= y < self._height and 0 <= x < self._width):
            return "Fora."
        if self._board[y][x] != ".":
            return "Já jogou aqui."

        for ship in self._ships:
            if ship.isAt(y, x):
                ship.registerHit(y, x)
                self._board[y][x] = "O"
                if ship.isSunk():
                    return "Você destruiu um navio!"
                return "Acertou um navio!"
        self._board[y][x] = "X"
        return "Água."

    def allSunk(self) -> bool:
        return all(ship.isSunk() for ship in self._ships)


def main():
    x, y = 10, 10
    qtdBoats = 4
    boatSize = 3

    game = NavalGame(x, y, qtdBoats, boatSize)
    game.showBoard()

    while not game.allSunk():
        try:
            a = input("(p - parar)[linha coluna]: ")
            if a == "p":break
            y, x = map(int, a.strip().split())
            resultado = game.play(y, x)
            print(resultado)
            game.showBoard()
        except:
            print("invalido")

    if a != "p":
        print("Todos os navios destruídos!")

main()
