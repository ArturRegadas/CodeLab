
from random import randint

class JokenpoState:
    def __init__(self):
        self.history = []

    def play(self, p1):
        p2 = randint(1, 3)
        mapping = {1: "Papel", 2: "Pedra", 3: "Tesoura"}
        if p1 == p2:
            out = "Empate"
        elif (p1 == 1 and p2 == 2) or (p1 == 2 and p2 == 3) or (p1 == 3 and p2 == 1):
            out = "Você ganhou"
        else:
            out = "Máquina ganhou"
        self.history.append({"p1": p1, "p2": p2, "result": out})
        return {"p1": mapping[p1], "p2": mapping[p2], "result": out}

    def serialize(self):
        return {"history": self.history}

    @staticmethod
    def deserialize(obj):
        s = JokenpoState()
        s.history = obj.get("history", [])
        return s