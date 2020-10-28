def addition_info(fn):
    def inner(var):
        print("="*40)
        print(f"Calling {fn.__name__}")
        print(f"with params {var}")
        rez = fn(var)
        print(f"Get rezult = {rez}")
        print("="*40)
        return rez
    return inner

@addition_info
def double(x):
    return x * 2

@addition_info
def triple(var):
    return var * 3

print(double("Hello"))
print(triple("World"))

