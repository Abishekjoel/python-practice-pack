class Car:
    #this year,company and number_of_cars are called class variables which is shared through all the objects through the class

    year=2024
    company="Tesla"
    number_of_cars=0
    #constructor
    def __init__(self,model,color):
        self.model=model
        self.color=color
        Car.number_of_cars+=1

car1=Car("Tesla Semi","red")
car2=Car("cybertruck","blue")

print(f'{Car.company} and {Car.year } and {Car.number_of_cars}')
print(f'{car1.model} is {car1.color} in color')
print(f'{car2.model} is {car2.color} in color')