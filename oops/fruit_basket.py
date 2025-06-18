class fruit:
    #this class a function called __init__ which will assign varaiable for the parameters inside the functon
    def __init__(self,name,color,number,is_avalible):
        self.name=name
        self.color=color
        self.number=number
        self.is_avalible=is_avalible

    def eat(self):
        print(f"i am going to eat {self.name} whichi is {self.color} in color and i have a total of {self.number}")

    def dont_eat(self):
        print(f'i dont want to eat {self.name} whichi is {self.color} in color and i have a total of {self.number}')
