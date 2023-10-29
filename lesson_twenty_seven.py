class Point2D:
    __slots__ = 'x', 'y'

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point3D(Point2D):
    __slots__ = 'z'

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z


pt3 = Point3D(10, 20, 30)
print(pt3.z)
pt3.y = 100
print(pt3.y)
