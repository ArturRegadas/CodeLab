from abc import (ABC, abstractmethod)
import math as mt

class GeometricForm(ABC):
    @abstractmethod
    def calcArea(self) -> None:
        pass

    @abstractmethod
    def calcPerimeter(self) -> None:
        pass

class Squid(GeometricForm):
    def __init__(self, widht:int, height:int) -> None:
        self._widht = widht
        self._height = height
    
    def calcArea(self) -> int:
        return self._widht*self._height
    
    def calcPerimeter(self) -> int:
        return 2 * self._widht + 2 * self._height

class Circle(GeometricForm):
    def __init__(self, radius:int) -> None:
        self._radius = radius
    
    def calcArea(self) -> float:
        return mt.pi * self._radius**2
    
    def calcPerimeter(self) -> float:
        return 2 * mt.pi * self._radius
        