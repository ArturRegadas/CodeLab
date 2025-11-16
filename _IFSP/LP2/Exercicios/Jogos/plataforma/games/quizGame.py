from random import randint

class QuizState:
    def __init__(self):
        self.questions = [
            {"q": "Pedro Cabral descobriu o Brasil?", "a": 1},
            {"q": "Colombo descobriu a América?", "a": 1},
            {"q": "Dom Pedro assinou a Lei Áurea?", "a": 0}
        ]
        self.score = 0
        self.current = None  

    def ask(self):
        idx = randint(0, len(self.questions) - 1)
        self.current = idx
        return self.questions[idx]["q"]

    def answer(self, ans):
        if self.current is None:
            return {"result": False, "error": "Nenhuma pergunta foi feita ainda."}
        correct = self.questions[self.current]["a"]
        if ans == correct:
            self.score += 1
            return {"result": True, "score": self.score}
        return {"result": False, "score": self.score}

    def serialize(self):
        return {
            "questions": self.questions,
            "score": self.score,
            "current": self.current     
        }

    @staticmethod
    def deserialize(obj):
        s = QuizState()
        s.questions = obj.get("questions", s.questions)
        s.score = obj.get("score", 0)
        s.current = obj.get("current", None) 
        return s
