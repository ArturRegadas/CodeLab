class Bank:
    def __init__(self, balance:float) -> None:
        self._balance = balance

    def deposit(self, value:int) -> bool:
        if (value > 0):
            self._balance+=value
            return True
        return False

    def getMoney(self, value:int) -> bool:
        if (value > 0 and value <= self._balance):
            self._balance -= value
            return True
        return False

    def getBalance(self) -> float:
        return self._balance
    
        