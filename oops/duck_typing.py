class animal:
    is_alive=True


class dog(animal):
    def sound(self):
        print("bark")


class cat(animal):
    def sound(self):
        print("meow")

class bike():
    #i have to add is_alive to this class because it does not have animal as its parent class
    is_alive=False
    def sound(self):
        print("shuuu")

animals=[dog(),cat(),bike()]

for anima in animals:
    anima.sound()
    print(anima.is_alive)