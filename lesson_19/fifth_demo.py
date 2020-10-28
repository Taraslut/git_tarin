class Circle:

    def __init__(self, r=1):
        self.r = r
        # self.square = 3.14 * r ** 2

    @property
    def square(self):
        return 3.14 * self.r**2

    @staticmethod
    def double(x):
        return x * 2

    @classmethod
    def triple(cls, x):
        return x * 3


my = Circle(2)

print(my.square)
my.r = 100
print(my.r)
print(my.square)
print(my.double("Hello"))

print(Circle.triple("World! "))