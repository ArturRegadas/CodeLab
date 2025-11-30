class HanoiState:
    def __init__(self, disks=5):
        self.disks = disks
        self.tower = [list(reversed(range(1, disks + 1))), [], []]

    def get_tower(self):
        return self.tower

    def move(self, init, destiny):
        i = init - 1
        d = destiny - 1
        if i == d or not (0 <= i < 3 and 0 <= d < 3):
            return {"ok": False, "error": "movimento invalido"}
        if len(self.tower[i]) == 0:
            return {"ok": False, "error": "nada para mover"}
        top = self.tower[i][-1]
        if len(self.tower[d]) > 0 and self.tower[d][-1] < top:
            return {"ok": False, "error": "movimento invalido: disco maior sobre menor"}
        self.tower[i].pop()
        self.tower[d].append(top)
        won = len(self.tower[2]) == self.disks
        return {"ok": True, "tower": self.tower, "won": won}

    def serialize(self):
        return {"disks": self.disks, "tower": self.tower}

    @staticmethod
    def deserialize(obj):
        s = HanoiState(obj.get("disks", 5))
        s.tower = obj["tower"]
        return s