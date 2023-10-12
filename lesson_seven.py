class Point:
    MIN_COORD = 0
    MAX_COORD = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        self.x = x
        self.y = y

    def __getattribute__(self, __name):
        print('__getattribute__')
        return object.__getattribute__(self, __name)

    def __setattr__(self, __name, __value):
        print('__setattr__')
        object.__setattr__(self, __name, __value)

    def __getattr__(self, item):
        print('__gettattr__')

    def __delattr__(self, __name):
        print('__delattr__')
        object.__delattr__(self, __name)


pt1 = Point(1, 2)
pt2 = Point(10, 20)
del pt1.x
print(pt1.__dict__)
