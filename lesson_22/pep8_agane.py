class MyCircle:
    def __init__(self):
        self.name = "ASsfew"
        print('init')

    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)
        return args[0]

    def info(self):
        return self.__dict__


circle = MyCircle()

rez = circle("sdfsdf", 12, "world")
print(rez)
print("==" * 40)
print(circle.info())
