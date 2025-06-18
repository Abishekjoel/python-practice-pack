            # 1. print statemet
# print("hello world")

            # 2.variables
# a=5
# print(a)

            # 3.operators
# x=5
#  y=7
#  z=10
# a=12
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)



# = is the assignment operator
 #x=5
 #x+=10
 #print(x)

#  y-=2
#  print(y)

# z*=2
# print(z)

# a/=2
# print(a)

# by add operators to the variable we can edit values

            # 4.getting input

# basketball=input("enter something:")

# print(basketball)

            # 5.comments
""" dyftgvjhbmn """


            # 6.type conversion

# a=123 #int type
# b=1.23 #float type
# c=b+a
# print(b+a)

# to see the type of variable



# print(type(c))

# to convert from one type to another

# word="123"
# number=123

# # print(word+number) #this will show error because it is different datatypes to aviod it we have to convert it

# word=int(word)#here int() is a python function
# print(word+number)

            #7.numeric data types

# print(type(5)) #int
# print(type(5.2)) #float
# print(type(2+3j))#complex

            # 8.list

# syntax
# a=[]

# example
# a=[1,2,3,4,5,"apple",6.5]

# to get a specific value from a list
# this can be done by calling there index value
# a=[1,2,"apple",3.4]
# print(a[2])

# to chage a value from the list we have to call its index value and assign a new value

# a=["apple",1,2,3,3.555]
# a[2]="hello"
# a.append("basketball")
# print(a)

            # 9.tuples 

# it is similar to list but the values cannot be edited

# syntax
# a=()

# its value can be see as like list same method
# a=[1,2,"apple",3.4]
# print(a[2])

# both in list and tuple we can access value with negative index value to get reversed Value

# a=("apple","mango",1,2)
# print(a[-1])#this will print the last value in the list or tuple

# to delete a list we can use del keyword we can delete the entire tuple but not a single value in it

# a=(1,2,3,4,5)
# del a
# print(a)

            # 10.string

# if we place any values inside a "",'',""" used for multilines""",''' used for multilines''' it will become string

# a='abi'
# b="abi"
# c="""abi is 
# hello
# world"""
# d='''abi
# hello
# world'''

# print(a)
# print(b)
# print(c)
# print(d)

# to acces a specific letter from a string we can use index value

# a="apple"
# print(a[2])

# string concatenation
# it is used to combine two string values

# a="cute"
# b="cabbage"

# print(a+b)

# to multiply a string 
# a="cute"
# b="cabbage"
# print(a*3)

 #slicing

# it is use to get a specific portion  of a string or list
# in a string
# a="apple is a fruit"
# print(a[0:4])

# in a list
# a=["apple",1,3,"mango","elephant"]

# print(a[1:-1])

            # 11.sets
#syntax
# a={}
# a set is also like a list and tuple but we cannot contain duplicate values
# a={"apple","apple","apple",1,2,3,1,2,4}
# print(a)

# to add a value inside a set we have to use add() function

# a={1,2,3,4,5,6,}
# a.add("apple")
# print(a)

# # to update a value 
# a={1,2,3,4,5,6,}
# a.update([1,10,11])
# print(a)

# # to remove a value 
# a={1,2,3,4,5,6,}
# a.remove(2)
# print(a)

# |--> union symbol also union()function is also avaliable
# a={1,2,3,4}
# b={3,4,5,6,}
# print(a|b)

    #union()
# a={1,2,3,4}
# b={2,3,4,5,6}
# a=a.union(b)
# print(a)

# &--> intersection symbol and also intersection() funtion is avalible
#  takes the common value from both sets
# a={1,2,3,4,5}
# b={2,3,7.9}
# print(a&b)

    # intersection()
# a={1,2,3,4,5}
# b={2,3,7.9}
# a=a.intersection(b)
# print(a)

# set difference

# a={1,2,3,4,5}
# b={2,4,5,6,8}
# print(a-b)

# ^--> symbol for symmetric difference (it is the opposite of intersection)

# a={1,2,3,4,5}
# b={1,4,5,7,33}
# print(a^b)

            # 13.dictionary

# syntax 
# a={'key':'values'}

# example
# a={1:'apple','fruit':'mango','list':[1,2,3,"apple"]}

#  to access a specifc value we have to call its key in print statement inside a []
# a={1:'apple','fruit':'mango','list':[1,2,3,"apple"]}
# print(a['fruit'])
# print(a['list'])

# to change a value inside a dictionary
# a={1:'apple','fruit':'mango','list':[1,2,3,"apple"]}
# a['list']="orange"
# print(a)

# to add a key and value 
# a={1:'apple','fruit':'mango','list':[1,2,3,"apple"]}
# a['ball']="basketball"
# print(a)

# to delete a key and value we can use del function
# a={1:'apple','fruit':'mango','list':[1,2,3,"apple"]}
# del a[1]
# print(a)

            # 14.range
#syntax-1
#range(start,end)

# num=range(1,11)
#we have to use this functions to print a range # list(),tuple(),set(),dict.fromkeys() are some of the inbuilt function to creat them easy 
# print(list(num))
# print(tuple(num))
# print(set(num))
# a=1,2,3,4
# print(dict.fromkeys(num,list(a)))

#syntax-1
#range(start,end,step)
# num=range(1,11,2)
# print(list(num))

# for reverse order
# nums=range(10,1,-1)
# print(list(nums))

            # 15.if else

#syntax
# if condition1:
#     code to execute if True
# elif condition2:
#     code to execute if the condition2 True
# else:
#      code to execute if both condition2 false

# example
# a=10
# if a<0:
#     print("a is less than 0")
# elif a==0:
#     print("a is zero")
# else:
#     print("a is greater than 0")

            # 16.while loop
# this loop is used to repete the code untill the condition is satisified

#syntax
# while condition:
     # code block to execute

a=10
sum=0   
counter=1

while counter<=a:
    sum=sum+counter
    counter=counter+1
print(sum)

            # 17.for loop

# for loop is also like while but there is no condition here
# it is mainly used to apply condition in every values in list or tuple or set

#syntax
# for item in sequence:
    # code block to execute


# example for list
# a=[1,2,3,4,5,6]
# sum=0
# for num in a:
#     sum=sum+num
#     print(sum)


# example for tuple
# a=(1,2,3,4,5,6)
# sum=0
# for num in a:
#     sum=sum+num
#     print(sum)


# example for set
# a={1,2,3}
# sum=0
# for num in a:
#     sum=sum+num
#     print(sum)

            # 18.break

# it is used to stop a loop

# for letter in "hello world":
#     if letter=="o":
#         break
#     print(letter)
# print("nothing")

            # 19.continue

# its is also use in loop to skip the value and contine to the code 

# for letter in "cute cabbage":
#     if letter=="c":
#         continue
#     print(letter)
# print('nothing')

            # 20.function

# A function is a reusable block of code designed to perform a specific task.

# syntax 
# def function_name():
    # code
        # <------project calculator------>
# def add(a,b):
#     c=a+b
#     return c

# def sub(a,b):
#     c=a-b
#     return c

# def mul(a,b):
#     c=a*b
#     return c

# def div(a,b):
#     if b==0:
#         return("u cant divide 0")
#     else:
#         c=a/b
#     return c

# def cal():
#     while True:

#         a=int(input("Enter a number:"))
#         b=int(input("Enter a number:"))

#         c=int(input("select a operator:1-ADDITION,2-SUBRATION,3-MULTIPLICATION,4-DIVISION,5-EXIT:"))

    
#         if c==1:
#             result=add(a,b)
#         elif c==2:
#             result=sub(a,b)
#         elif c==3:
#             result=mul(a,b)
#         elif c==4:
#             result=div(a,b)
#         elif c==5:
#             print("bye dude😀")
#             break
#         else:
#             print("select a valid operation")
#             print (c)
#         print(f"{result}")
# cal()

        # in the above function
# to call a function "function_name()"
# values inside the function is call arguments
# to store the value we have to use returen in function


# recursive function 
# if a function call itsellf in its function again and again is called recursive

# example

# def factorial(x):
#     if x==1:
#         return 1
#     else:
#         return(x*factorial(x-1))
# while True:
#     num=int(input("enter a number:"))
#     print(f"the factorial of ",num,"is",factorial(num) )

            # 21.lambda
# it is a way to write function with many arguments but only one expression

#syntax
# lambda arguments: expression

# example
# a=int(input("enter a number:"))
# b=int(input("enter a number:"))
# add=lambda a,b:(a+b)#lamda function
# print(add(a,b))

            # 22.modules

# if we want to access a function from another ython file we can access them by using models
# we have to use import keyword to import the file and use its function
#  syntax 
# from python filename import function_name

# example
# from math import pi
# print(pi)

#             23.open file 
# we can open files using this open() function
# if we open  file we must close it to avoid unwantted data overwrite
# text=open("hello.txt")
# text.close()
#     modes
# r-read
# w-write
# x-it creat a new file to wirte
# a-(appending)it will add the content to the existing file 
# t-to open it in text format
# b-to open in binary format
# +-it will prepare the file to read and write

            # 24.Exception handling

# it is a method to handle errors
# syntax 
# try:
#     Code 
# except:
#     error code 

# first we have to import a module called sys 

# import sys
# lists=["apple",0,4]
# for li in lists:
#     try:
#         print("the value from the list is ",li)
#         i=1/li
#     except:
#         print("there is a",sys.exc_info()[0], "in your code")
#         print("next one")
#         print("----------------")
# print("the value of",li,"is", i)

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------


                           