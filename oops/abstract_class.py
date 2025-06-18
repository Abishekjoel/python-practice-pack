from abc import ABC,abstractmethod

class car:
    def __init__(self,name):
        self.name=name

    @abstractmethod
    def moveforward(self):
        pass

    @abstractmethod
    def movebackward(self):
        pass

    @abstractmethod
    def on_wipper(self):
        pass

    @abstractmethod
    def off_wipper(self):
        pass


class tesla(car):
    def movebackward(self):
        print(f'{self.name} car can move backward')

    def moveforward(self):
        print(f"{self.name} car can move forward")

    def on_wipper(self):
        print(f"{self.name} on wipper")

    def off_wipper(self):
        print(f"{self.name} off wipper")

Tesla=tesla("cybertruck")

Tesla.movebackward()
Tesla.moveforward()
Tesla.on_wipper()
Tesla.off_wipper()