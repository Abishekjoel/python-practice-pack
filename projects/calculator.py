def add(a,b):
    c=a+b
    return c

def sub(a,b):
    c=a-b
    return c

def mul(a,b):
    c=a*b
    return c

def div(a,b):
    if b==0:
        return("u cant divide 0")
    else:
        c=a/b
    return c

def cal():
    while True:

        a=int(input("Enter a number:"))
        b=int(input("Enter a number:"))

        c=int(input("select a operator:1-ADDITION,2-SUBRATION,3-MULTIPLICATION,4-DIVISION,5-EXIT:"))

    
        if c==1:
            result=add(a,b)
        elif c==2:
            result=sub(a,b)
        elif c==3:
            result=mul(a,b)
        elif c==4:
            result=div(a,b)
        elif c==5:
            print("bye dude😀")
            break
        else:
            print("select a valid operation")
            print (c)
        print(f"{result}")
cal()
