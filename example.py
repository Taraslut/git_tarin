# import first
def hello(name):
    # pass
    return f"hello a"

print("Hello from example")
print(__name__)

input = [
    'a',
    'Taras'
]

expected= [
    'hello a',
    'hello Taras'
]

def test():
    for test_case, expect in zip(input, expected):
        rez = hello(test_case)
        assert rez == expect, f'hello(\'{test_case}\') is expected =>\'{expect}\' but \'{rez}\' is present'


if __name__ == "__main__":
    print("In main scope")
    test()