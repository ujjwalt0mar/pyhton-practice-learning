def hello10():
    print('hello '*10)

# def primamid():
#     star = '*'
#     for i in range(0,10):
#         print(star.center(30, ' '))
#         star += '**'

# def primamid(layers):
#     star = '*'
#     for i in range(0, layers):
#         print(star.center(30, ' '))
#         star += '**'

# def circle_area(radius):
#     import math
#     return math.pi * radius ** 2

def surface_area_of_cuboid(l, w, h):
    """this functions takes the length, width and height of a cuboid and returns its surface area"""
    return 2 * (l * w + l * h + w * h)

# hello10()
# primamid(4)
# print(circle_area(5))
print("surface area of cuboid:", surface_area_of_cuboid(3, 5, 7))
print( surface_area_of_cuboid.__doc__)

