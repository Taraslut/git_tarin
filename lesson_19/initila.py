
def addition_action(fn):
    def inner(var):
        print("Before foo call")
        rez = fn(var)
        print("After foo call")
        return rez
    return inner

@addition_action
def double(x):
    print("In double")
    return x * 2

print(double("Hello"))
# print(addition_action(double)("Hello"))

# double = addition_action(double)
