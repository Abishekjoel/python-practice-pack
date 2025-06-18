grocery_list=[]
grocery_quantity=[]
grocery_price=[]
def getdata():

    grocery_list.append (str(input("Enter the product name:")))
    grocery_quantity.append(int(input("enter the quantity of the product:")))
    grocery_price.append(int(input("enter the price of the product:")))
def display():
     print("-----------------------------------------")
     for index, grocery in enumerate(grocery_list, start=1):
         print(f"{index}. item:{grocery}. Quantity:{grocery_quantity[index-1]}.Price:{grocery_price[index-1]}")
     print("-----------------------------------------")

def delete():
    delr=int(input("enter the product id to delete:"))-1
    if 0 <= delr < len(grocery_list):
        grocery_price==grocery_list==grocery_quantity==delr
        grocery_list.pop(delr)
        grocery_quantity.pop(delr)
        grocery_price.pop(delr)
    else:
        print("enter something vaild bro")

def edit():
    edit_id = int(input("Enter product no to edit: ")) - 1
    if 0 <= edit_id < len(grocery_list):
         grocery_list[edit_id] = str(input("Enter new product name: "))
         grocery_quantity[edit_id] = int(input("Enter new quantity: "))
         grocery_price[edit_id] = int(input("Enter new price: "))
    else:
        print("enter something vaild bro")

def options_input():
   return str(input("enter e to edit the product,enter d to delete the product,enter q to quit shopping, a to add a product:")).lower()

def total():
    total=sum(grocery_quantity[i]*grocery_price[i] for i in range(len(grocery_list)))
    print(f"The total amount is:{total}")
  

def main_function():
    getdata()

    options=""
    while options != "q":
        display()
        total()
        options = options_input()

        if options=="a":
            getdata()
        elif options=="d":
            delete()
        elif options=="e":
            edit()
        elif options=="q":
            break
        else:
            print("invalid retry ")

    print("thanks for shopping with us 😀😘 ")

main_function()