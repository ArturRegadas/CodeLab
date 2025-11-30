class Animal:
    def __init__(self, name:str, age:int) -> None:
        self.name = name
        self.age = age
    def sound(self) -> str:
        return "genericSound"
class Dog(Animal):
    def sound(self) -> str:
        return "AuAuAu"
class Cat(Animal):
    def sound(self) -> str:
        return "Miau"

print(Dog("Preta", 7).sound())

