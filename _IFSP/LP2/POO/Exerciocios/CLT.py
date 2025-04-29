class Employ:
    def __init__(self, name:str, salary:float) -> None:
        self.name = name
        self.salary = salary

    def calcSalary(self) -> float:
        return self.salary

class Manager(Employ):
    def __init__(self, name:str, salary:float, extra:float) -> None:
        super().__init__(name, salary)
        self.extra = extra

    def calcSalary(self) -> float:
        return self.salary + self.extra
        
class Seller(Employ):
    def __init__(self, name:str,salary:float ,commission:float, sales:int) -> None:
        super().__init__(name, salary)
        self.commision = commission
        self.sales = sales
        
    def calcSalary(self) -> float:
        return self.salary + (self.commision * self.sales)

class Dev(Employ):
    def __init__(self, name:str, salary:float, level:int, experience:list) -> None:
        super().__init__(name, salary)
        self.level = level
        self.experience = experience
    def calcSalary(self) -> float:
        return self.salary
    
def main():
    manager = Manager("Cleiso", 1000, 400)
    seller = Seller("Mr. Brown", 1000, 4, 100)
    dev = Dev("Mara",1400, 4, ["Java", "C99", "Git"])

    print(manager.calcSalary())
    print(seller.calcSalary())
    print(dev.calcSalary())
if __name__ == "__main__":
    main()