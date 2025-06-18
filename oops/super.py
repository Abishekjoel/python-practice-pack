#function used in child class to call the methods from the parent class is called supper class

class vechile:
    def __init__(self,name,color,no_of_wheels):
        self.name=name
        self.color=color
        self.no_of_wheels=no_of_wheels

    def move_forward(self):
        print("move forward")



class car(vechile):
    def __init__(self,no_of_wheels,name,color,wipper):
        super().__init__(name,color,no_of_wheels)
        self.wipper=wipper

class bike(vechile):
    def __init__(self, name, color,no_of_wheels,helmet):
        super().__init__(name, color,no_of_wheels)
        self.helmet=helmet

Car=car(name="tesla",no_of_wheels=4,color="black",wipper=" wipper")
Bike=bike(name="tesla",no_of_wheels=2,color="black",helmet=" helmet")

print(f'{Car.name} has {Car.no_of_wheels} wheels and it is {Car.color} in color and has {Car.wipper}')
Car.move_forward()
        
print()

print(f'{Bike.name} has {Bike.no_of_wheels} wheels and it is {Bike.color} in color and has {Bike.helmet}')
Bike.move_forward()