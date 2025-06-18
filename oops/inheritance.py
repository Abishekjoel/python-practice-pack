# inheritance allows a class to inherit another class attributes and methods
# fish is the parent class

                            # code1
class fish:

    def __init__(self,name):
        self.name=name
        self.is_alive=True

    def water(self):
        print(f"{self.name} can live in water")

    def swim(self):
        print(f'{self.name} can swim in water')

# star_fish,shark,gold_fish are child class

class star_fish(fish):
    pass

class shark(fish):
    pass

class gold_fish(fish):
    pass


star=star_fish("star_fire")
shrk=shark("megaladon")
gold=gold_fish("silver")

print(star.name)
print(star.is_alive)
star.swim()
star.water()

print()
print(shrk.name)
print(shrk.is_alive)
shrk.swim()
shrk.water()

print()

print(gold.name)
print(gold.is_alive)
gold.swim()
gold.water()

                                            # code2


# class fruit:

#     def __init__(self,name,color):
#         self.name=name
#         self.color=color
#         self.fruit=True
    
#     def can_eat(self):
#         print(f'{self.name} can be eaten')

#     def can_cut(self):
#         print(f'{self.name } can be cut')

# class fruit1(fruit):
#     def inside(self):
#         print(" the inside color is white")

# class fruit2(fruit):
#     def inside(self):
#         print("the inside color is yellow")

# class fruit3(fruit):
#     def inside(self):
#         print("the inside color is red")

# apple=fruit1("apple","red")
# mango=fruit2("mango","yellow")
# watermelon=fruit3("watermelon","green")

# print(apple.name)
# print(apple.color)
# apple.can_cut()
# apple.can_eat()
# apple.inside()
# print()


# print(mango.name)
# print(mango.color)
# mango.can_cut()
# mango.can_eat()
# mango.inside()

# print()

# print(watermelon.name)
# print(watermelon.color)
# watermelon.can_cut()
# watermelon.can_eat()
# watermelon.inside()


