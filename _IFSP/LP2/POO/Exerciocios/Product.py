#!/usr/bin/env python3
class Product:
    def __init__(self, name:str, price:float, qtd:int) -> None:
        self._name = name
        self._price = price
        self._qtd = qtd
    
    def calcTotalValue(self) -> float:
        return self._price*self._qtd
    
    def setQtd(self, newQtd:int) -> None:
        self._qtd = newQtd
    
def main():
    product = Product("Potato", 2.5, 5)

    print(product.calcTotalValue())
    
    product.setQtd(10)
    
    print(product.calcTotalValue())

if (__name__ == "__main__"):
    main()