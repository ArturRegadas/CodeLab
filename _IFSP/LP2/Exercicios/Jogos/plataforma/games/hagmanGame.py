from random import choice

class HangmanState:
    def __init__(self, word=None, lifes=6):
        words = ["imperialismo", "calunia", "comunismo"]
        self.word = word or choice(words)
        self.ans = ["_" for _ in self.word]
        self.lifes = lifes

    def play_letter(self, letter):
        updated = False
        for i, ch in enumerate(self.word):
            if ch == letter:
                self.ans[i] = letter
                updated = True
        if not updated:
            self.lifes -= 1
        status = "playing"
        if "_" not in self.ans:
            status = "won"
        elif self.lifes <= 0:
            status = "lost"
        return {"ans": "".join(self.ans), "lifes": self.lifes, "status": status}

    def serialize(self):
        return {"word": self.word, "ans": self.ans, "lifes": self.lifes}

    @staticmethod
    def deserialize(obj):
        s = HangmanState(obj["word"], obj["lifes"])
        s.ans = obj["ans"]
        return s

# HANOI
