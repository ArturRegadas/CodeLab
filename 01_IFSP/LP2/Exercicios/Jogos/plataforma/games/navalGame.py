from random import randint, choice

class NavalGameState:
    def __init__(self, height=10, width=10, num_ships=4, ship_size=3):
        self.height = height
        self.width = width
        self.board = [["." for _ in range(width)] for _ in range(height)]
        self.ships = []  # list of dicts {positions: [(y,x)...], hits: []}
        self._place_ships(num_ships, ship_size)

    def _place_ships(self, num_ships, ship_size):
        count = 0
        while count < num_ships:
            horizontal = choice([True, False])
            if horizontal:
                x = randint(0, self.width - ship_size)
                y = randint(0, self.height - 1)
                positions = [(y, x + i) for i in range(ship_size)]
            else:
                x = randint(0, self.width - 1)
                y = randint(0, self.height - ship_size)
                positions = [(y + i, x) for i in range(ship_size)]

            conflict = False
            for py, px in positions:
                for ship in self.ships:
                    if (py, px) in ship["positions"]:
                        conflict = True
                        break
                if conflict:
                    break
            if not conflict:
                self.ships.append({"positions": positions, "hits": []})
                count += 1

    def play(self, y, x):
        y -= 1
        x -= 1
        if not (0 <= y < self.height and 0 <= x < self.width):
            return {"result": "Fora."}
        if self.board[y][x] != ".":
            return {"result": "Já jogou aqui."}

        for ship in self.ships:
            if (y, x) in ship["positions"]:
                ship["hits"].append((y, x))
                self.board[y][x] = "O"
                if set(ship["positions"]) == set(ship["hits"]):
                    return {"result": "Você destruiu um navio!", "board": self.board}
                return {"result": "Acertou um navio!", "board": self.board}
        self.board[y][x] = "X"
        return {"result": "Água.", "board": self.board}

    def all_sunk(self):
        return all(set(s["positions"]) == set(s["hits"]) for s in self.ships)

    def serialize(self):
        return {"height": self.height, "width": self.width, "board": self.board, "ships": self.ships}

    @staticmethod
    def deserialize(obj):
        g = NavalGameState(obj["height"], obj["width"], 0, 1)
        g.board = obj["board"]

        ships = []
        for s in obj.get("ships", []):
            raw_positions = s.get("positions", [])
            positions = []
            for p in raw_positions:
                if isinstance(p, (list, tuple)) and len(p) == 2:
                    positions.append((int(p[0]), int(p[1])))

            raw_hits = s.get("hits", [])
            hits = []
            if raw_hits is None:
                raw_hits = []

            for h in raw_hits:
                if isinstance(h, (list, tuple)) and len(h) == 2:
                    hits.append((int(h[0]), int(h[1])))

            ships.append({
                "positions": positions,
                "hits": hits
            })

        g.ships = ships
        print(g.ships)
        return g
