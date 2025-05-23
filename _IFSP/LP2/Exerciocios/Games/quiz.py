from random import randint
class Question:
    def __init__(self, question:str,  answer:int) -> None:
        self._question = question
        self._answer = answer
   
    def getQuestion(self) -> str:
        return self._question
   
    def getAnswer(self) -> int:
        return self._answer
       
class Quiz:
    def __init__(self) -> None:
        self._questions = [
            Question("pedro cabral descbriu the BRAZUCA?", 1),
            Question("colombis descobriu the AMRErIKA AMRErIKA ", 1),
            Question("Dom pedrinho assinou the Aurea Lei ?", 1),
            ]
        self._score = 0
   
    def doQuestion(self)-> None:
        question = self._questions[randint(0, 2)]
        ans = int(input(question.getQuestion() + "\n[1 - verdadeiro]\n[0 - falso]\n: "))
        if ans == question.getAnswer():
            print("acertou")
            self._score+=1
        else:
            print("errou")
           
        print("sua pontuação é:", self._score)
        print()

def main():
    quiz = Quiz()
    while((l:=input("p -> parar:  ")) != "p" ):
        quiz.doQuestion()

main()