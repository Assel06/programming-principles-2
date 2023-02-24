import math

def degreeToRad(degree):
    print(math.radians(degree))

def areaOfTrapezoid(height, base1, base2):
    print(height *(base1 + base2) / 2)

def areaOfRegPolygon(sides, length):
    area = int(((sides * (length ** 2)) / (4 * math.tan(math.pi / sides))))
    print(area)

def areaOfParallelogram(length, height):
    print(length * height)

degreeToRad(15)
areaOfTrapezoid(5, 5, 6)
areaOfRegPolygon(4, 25)
areaOfParallelogram(5, 6)