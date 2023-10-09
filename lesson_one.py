class Point:
    'Doc'
    color = 'red'
    circle = 2


a = Point()
b = Point()

a.x = 1
a.y = 2

b.x = 10
b.y = 20

hasattr(a, 'color')
getattr(a, 'color')
setattr(a, 'prop', 'great')
delattr(a, 'prop')
