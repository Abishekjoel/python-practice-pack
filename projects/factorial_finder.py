def factorial(x):
    if x==1:
        return x
    else:
       return(x*factorial(x-1))

while True:
    num=int(input("enter a number to get its factorial:"))
    print(f"the factorial of",num,"is",factorial(num))