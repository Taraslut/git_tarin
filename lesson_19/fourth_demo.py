def fail_foo(fn):
    print(f"in deco {fn.__name__}")
    def inner(x):
        return "Foo is failed"
    return inner


@fail_foo
def double(x):
    return x * 2


@fail_foo
def triple(var):
    return var * 3


print(double("Hello"))
print(triple("World"))
