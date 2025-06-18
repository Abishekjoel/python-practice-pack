#multiple inheritance--->when two or more parent class is used for a child class
#c(a,b)
#example 
# two parent class name under_water and Above water is used for cat,shark,tourtise class--
#  but in tourtise class we use both the parent class it is called multiple inheritance


# in multi-level inheritance we use a parent class to a child class and that child class will become parent class to another child class
#c(B) <- b(a) <- a

class lifes:
    def __init__(self, name):
        self.name = name
    def is_living(self):
        print(f"{self.name} is living")
        
class under_water(lifes):
    def water(self):
        print(f"{self.name} can live under water")

class above_water(lifes):
    def land(self):
        print(f"{self.name} can live above water")

class cat(above_water):
    pass

class shark(under_water):
    pass

class tortoise(above_water, under_water):
    pass

# Creating instances
Cat = cat("Tom")
Shark = shark("Sabertooth")
Tortoise = tortoise("Master Wu")

# Testing the instances
Cat.land()           
Shark.water()       
Tortoise.water()      
Tortoise.land()
Cat.is_living()      


