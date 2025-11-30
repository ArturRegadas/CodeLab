class Vehicle:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def show_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")


class Car(Vehicle):
    def __init__(self, brand: str, model: str, num_doors: int):
        super().__init__(brand, model)
        self.num_doors = num_doors

    def show_details(self):
        super().show_details()
        print(f"Number of doors: {self.num_doors}")
        print("-" * 30)


class Motorcycle(Vehicle):
    def __init__(self, brand: str, model: str, engine_cc: int):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

    def show_details(self):
        super().show_details()
        print(f"Engine displacement: {self.engine_cc} cc")
        print("-" * 30)



car1 = Car("Toyota", "Corolla", 4)
car2 = Car("Ford", "Mustang", 2)

motorcycle1 = Motorcycle("Yamaha", "MT-07", 689)
motorcycle2 = Motorcycle("Honda", "CB500F", 471)

car1.show_details()
car2.show_details()

motorcycle1.show_details()
motorcycle2.show_details()
