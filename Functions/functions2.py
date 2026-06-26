def hello10():
    print("this function is from", __name__)
    print('hello '*10)

def primamid():
    print("this function is from", __name__)
    star = '*'
    for i in range(0,10):
        print(star.center(30, ' '))
        star += '**'

def primamid(layers):
    print("this function is from", __name__)
    star = '*'
    for i in range(0, layers):
        print(star.center(30, ' '))
        star += '**'

def circle_area(radius):
    print("this function is from", __name__)
    import math
    return math.pi * radius ** 2

def surface_area_of_cuboid(l, w, h):
    print("this function is from", __name__)
    """this functions takes the length, width and height of a cuboid and returns its surface area"""
    return 2 * (l * w + l * h + w * h)

if __name__ == "__main__":
    hello10()
    primamid(4)
    print(circle_area(5))
    print("surface area of cuboid:", surface_area_of_cuboid(3, 5, 7))
    print(surface_area_of_cuboid.__doc__)

