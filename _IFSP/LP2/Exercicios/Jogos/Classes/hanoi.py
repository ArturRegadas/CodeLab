class HanoiTower:
    def __init__(self) -> None:
        self.tower = [[1, 0, 0], [2, 0, 0], [3, 0, 0], [4, 0, 0], [5, 0, 0]]

    def win_check(self) -> bool:
        return all(self.tower[i][2] != 0 for i in range(5))

    def print_hanoi(self) -> None:
        for row in self.tower:
            print(" ".join(map(str, row)))
        print()

    def validate(self, init:int, destiny:int) -> bool:
        return not (init == destiny or init < 1 or init > 3 or destiny < 1 or destiny > 3 or self.tower[4][init - 1] == 0)

    def get_top(self, column:int) -> int:
        for i in range(5):
            if self.tower[i][column] != 0:
                return i
        return 5

    def swap_hanoi(self, init:int, destiny:int) -> bool:
        init -= 1
        destiny -= 1
        idx_top_init = self.get_top(init)
        idx_top_destiny = self.get_top(destiny)

        if idx_top_destiny < 5 and self.tower[idx_top_init][init] > self.tower[idx_top_destiny][destiny]:
            return False

        if idx_top_destiny == 5:
            self.tower[idx_top_init][init], self.tower[4][destiny] = self.tower[4][destiny], self.tower[idx_top_init][init]
        else:
            self.tower[idx_top_init][init], self.tower[idx_top_destiny - 1][destiny] = self.tower[idx_top_destiny - 1][destiny], self.tower[idx_top_init][init]
       
        return True


def main():
    game = HanoiTower()

    while True:
        game.print_hanoi()
        init, destiny = map(int, input("Escolha seu movimento [inicio | destino](1|2|3): ").split())

        if game.validate(init, destiny):
            if game.swap_hanoi(init, destiny):
                print("ok!")
            else:
                print("movimento invalido")

            if game.win_check():
                game.print_hanoi()
                print("voce ganhou!\n")
                break
        else:
            print("movimento invalido")


main()