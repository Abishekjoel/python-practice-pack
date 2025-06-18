#  python object oriented programming

# objects is a the instance of class
# collection of objects is called class

# class fruit:
#     #this class a function called __init__ which will assign varaiable for the parameters inside the functon
#     def __init__(self,name,color,number,is_avalible):
#         self.name=name
#         self.color=color
#         self.number=number
#         self.is_avalible=is_avalible
# #creat an objects inside a class calle fruit1,2...
# fruit1=fruit("apple","red",4,True)
# fruit2=fruit("Mango","yellow",5,True)
# fruit3=fruit("watermelon","green",2,False)

# #by adding a . after the object name before the parameters above we can access its data
# print(fruit1.color)
# print(fruit2.number)
# print(fruit3.is_avalible)

#  in method two we use module method to use it 
from fruit_basket import fruit

fruit1=fruit("apple","red",4,True)
fruit2=fruit("Mango","yellow",5,True)
fruit3=fruit("watermelon","green",2,False)

#by adding a . after the object name before the parameters above we can access its data
print(fruit1.color)
print(fruit2.number)
print(fruit3.is_avalible)



# <<<----------------------------------note-------------------------------->>>

# in the above method first i use function in the same py file and run the code
#  but in the second one i store the class in a seperate py file and import the function in it and use it in another file

fruit1.eat()
fruit2.dont_eat()