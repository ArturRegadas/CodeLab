from random import randint

class NumberState:
    def __init__(self):
        self.last_machine = None

    def play(self, number):
        machine = randint(1, 5)
        self.last_machine = machine
        ok = machine == number
        return {"machine": machine, "win": ok}

    def serialize(self):
        return {"last_machine": self.last_machine}

    @staticmethod
    def deserialize(obj):
        s = NumberState()
        s.last_machine = obj.get("last_machine")
        return s