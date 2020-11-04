"""
This module is for It-Cluster course.
"""


class Circle:
    """
    Class is dedicated for circle base functionality.
    """

    def __init__(self, radius=1):
    # TODO After implementation Base class move this code to it.
        self.radius = radius
        # self.square = 3.14 * r ** 2

    @property
    def square(self):
        """
        Property to calculate circle square
        :return:
        """
        return 3.14 * self.radius ** 2

    @staticmethod
    def double(var_for_double):
        """
        fsdfsdfsd
        """
        return var_for_double * 2

    @classmethod
    def triple(cls, var_to_triple):
        """
        Class method to  triple variable.
        :param var_to_triple:
        :return:
        """
        print(cls.__name__)
        return var_to_triple * 3


class Sqaure(Circle):
    pass

my = Circle(2)

print(my.square)
my.radius = 100
print(my.radius)
print(my.square)
print(my.double("Hello"))

print(Circle.triple("World! "))
print(my.triple("hi! "))

print("="*40)
print(Sqaure.triple("World! "))
