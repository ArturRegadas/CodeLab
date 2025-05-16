#!/usr/bin/env python3
#Artur e Caue :0
from random import randint

class MenuItem:
    def __init__(self,name:str, description:str, price:float) -> None:
        self._name=name
        self._description = description
        self._price = price
    def getDetails(self) -> str:
        return f"Item: {self._name} - {self._description} - {self._price}"
    
    def getName(self):
        return self._name
    
    def getPrice(self):
        return self._price

class Client:
    def __init__(self, name:str, phoneNumber:str) -> None:
        self._name = name
        self._phoneNumber = phoneNumber

    def getDetails(self) -> str:
        return f"Client: {self._name} - {self._phoneNumber}"

class Order:
    def __init__(self, client:'Client') -> None:
        self._client = client
        self._itensOrder:list['MenuItem'] = []
        self._status = "Open"
    
    def addItem(self, itemToAdd:'MenuItem', qtd:int = 1) -> bool:
        if itemToAdd.getName() in [i.getName() for i in self._itensOrder]:
            ans = True
        else:
            ans = False
        for i in range(qtd):
            self._itensOrder.append(itemToAdd)
        return ans
    
    def calcTotal(self) -> float:
        return sum(i.getPrice() for i in self._itensOrder)
    
    def getDetails(self) -> str:
        return "\n".join([
            self._client.getDetails(),
            "\n".join([i.getDetails() for i in self._itensOrder]),
            "Status: "+ self._status,
            "total$$: "+str(round(self.calcTotal(), 2)),
            ""
        ])

    def finishOrder(self) -> None:
        self._status = "Finished"

class Menu:
    def __init__(self) -> None:
        self._menu:list['MenuItem'] = [
            MenuItem("X-Burger", "is Delicious", 29.99),
            MenuItem("Fries", "the best potato", 15.25),
            MenuItem("CocaCola", "refresh your mind", 7)
        ]
    def getItemForIndex(self, idx:int) -> 'MenuItem':
        return self._menu[idx]

def main():
    menu = Menu()
    order = Order(
        Client("Romero Brito", "11216969")
    )
    order.addItem(
        menu.getItemForIndex(randint(0,2)),
        2
    )
    order.addItem(
        menu.getItemForIndex(randint(0,2))
    )

    print(order.getDetails())

    order.finishOrder()

    print(order.getDetails())

if __name__=="_main__":
    main()