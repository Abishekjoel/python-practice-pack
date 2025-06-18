def honey(fun):
    def food(*args, **kwargs):
        print("add honey")
        fun(*args, **kwargs)
    return food

def oil(fun):
    def food(*args, **kwargs):
        print("add oil")
        fun(*args, **kwargs)
    return food

@oil
def non_veg(meat):
    print(f"{meat} is ready")

@honey
def veg(vegetable):
    print(f"{vegetable} is ready")

# Call the decorated function
non_veg("chicken")
veg("Mushroom")
