class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def display1(self):
        print(f"Vehicle model {self.model} ")

car = Vehicle(2006,"Alto")
car.display1()
 
        