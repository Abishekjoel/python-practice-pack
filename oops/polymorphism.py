#Inheritance is about creating new classes based on existing ones.
#Polymorphism is about allowing different classes to define methods with the same name, 
# where the behavior depends on the specific class instance.

from abc import ABC,abstractmethod
class Shape:
    @abstractmethod
    def area(self):
        pass
class circle(Shape):
    def __init__(self,radius):
       self.radius=radius

    def area(self):
        return(f"the radius is {self.radius} cm")

class square(Shape):
    def __init__(self,height,width):
        self.height=height
        self.width=width

    def area(self):
        return(f"the height is {self.height} cm and width of {self.width}")


class triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    
    
    def area(self):
        return(f"the height is {self.height} cm and base of {self.base}")

class bread(square):
    def __init__(self, height, width,fillings):
        super().__init__(height, width)
        self.fillings=fillings


Shapes=[circle(4),square(6,6),triangle(10,5),bread(15,12,"tomato")]

for shape in Shapes:
    print(shape.area())

