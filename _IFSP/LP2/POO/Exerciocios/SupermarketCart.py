# implementação de linkedList usando conceitos de POO,
# desafiador fazer sem tipagem 
class Product:
    def __init__(self, name:str, price:float) -> None:
        self._name = name
        self._price = price
        self._parent = None #product
        self._neighbor = None #product

    def getName(self) -> str:
        return self._name

    def getNeighbor(self) -> 'Product':
        return self._neighbor
    
    def getPrice(self) -> float:
        return self._price

    def setNeighbor(self, neighbor: 'Product') -> None:
        self._neighbor = neighbor


class SupermarketCart:
    def __init__(self, name:str = None, price:float = None) -> None:
        if(name is None or price is None):
            self._root = None
            self._head = None
            return
        self._root = Product(name, price)
        self._head = self.root
        
    def _setRoot(self, root: 'Product') -> None:
        self._root = root;

    def _setHead(self, head: 'Product') -> None:
        self._head = head
        
    def add(self, name:str, price:float) -> None:
        if(self._root is None):
            self._root = Product(name, price)
            self._head = self._root
            return
        self._head.setNeighbor(Product(name, price))
        self._head = self._head.getNeighbor()
    
    def _getTotalValueRecursive(self, value: float, current: 'Product') -> float:
        if(current.getNeighbor() is None):
            return value + current.getPrice()
        return self._getTotalValueRecursive(value+current.getPrice(), current.getNeighbor())
        

    def getTotalValue(self) -> float:
        if(self._root is None):return 0
        return self._getTotalValueRecursive(0, self._root)
    
    def _printProductsRecursive(self, current: 'Product') -> None:
        print(current.getName())
        if(current.getNeighbor() is None):
            return
        self._printProductsRecursive(current.getNeighbor())

    def printProducts(self) -> None:
        if(self._root is None):
            print("Vazio")
            return
        self._printProductsRecursive(self._root)

    def _removeRecursive(self, key:str, ant:'Product',current: 'Product') -> bool:
        if(current is None):
            return False
        if(current.getName() == key):
            ant.setNeighbor(current.getNeighbor())
            return True
        return self._removeRecursive(key, current, current.getNeighbor())
        

    def remove(self, key:str) -> bool:
        if(self._root is None):
            return False
        if(self._root.getName() == key):
            self._root = self._root.getNeighbor()
            return True
        return self._removeRecursive(key,self._root ,self._root.getNeighbor())

def main():
    myList = SupermarketCart()

    myList.add("cellPhone", 500)
    myList.add("Computer", 700)
    myList.add("Tv", 200)
    myList.add("freezer", 120)

    myList.printProducts()
    print(myList.getTotalValue())
    print("\n")

    myList.remove("Computer")

    myList.printProducts()
    print(myList.getTotalValue())
    print("\n")

    myList.remove("cellPhone")

    myList.printProducts()
    print(myList.getTotalValue())
    print("\n")

    myList.remove("freezer")

    myList.printProducts()
    print(myList.getTotalValue())
    print("\n")

    myList.remove("Tv")

    myList.printProducts()
    print(myList.getTotalValue())

if __name__ == "__main__":
    main()