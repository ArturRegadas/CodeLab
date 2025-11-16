from random import randint
class HangmanGame:
    def __init__ (self, word:str) -> None:
        self._word = word
        self._ansWord = "_"*len(word)
        self._lifes = 3
    def playRound(self, letter:str) -> None:
        aux = self._ansWord
        self._ansWord = ""
        for i in range(0, len(self._word)):
            self._ansWord += aux[i] if letter != self._word[i] else letter
       
        if self._ansWord == aux:
            self._lifes-=1
            print("nao acertou nada, agora esta com", self._lifes, "vidas")
       
        print(self._ansWord)
        if self._ansWord == self._word:
            print("ganhou")
       
def main():
    hangmanGame = HangmanGame(("imperialismo", "metanfetamina", "comunismo")[randint(0, 2)])
    while((l:=input("digite sua letra (-1 -> parar): ")) != "-1" ):
        hangmanGame.playRound(l.lower())
        print()

main()
