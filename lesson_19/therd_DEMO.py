import time


def get_timing(fn):
    print(f"in deco {fn.__name__}")
    def inner(var):
        start_time = time.monotonic_ns()
        rez = fn(var)
        end_time = time.monotonic_ns()
        print(f"Calling {fn.__name__} for {end_time - start_time} ns.")
        return rez

    return inner


@get_timing
def double(x):
    time.sleep(0.01)
    return x * 2


@get_timing
def triple(var):
    ll = []
    for i in range(10 **3):
        ll.append(i)
    ll[0] = ll[0] + ll[-1]
    del ll
    return var * 3


# double("Hello")
# triple("World")
