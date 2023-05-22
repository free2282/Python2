import math


class Sphere:

    def __init__(self, radius=None, x=None, y=None, z=None):
        if radius is not None:
            self.__radius = radius
        else:
            self.__radius = 1.0

        if x is not None:
            self.__x = x
        else:
            self.__x = 0.0

        if y is not None:
            self.__y = y
        else:
            self.__y = 0.0

        if z is not None:
            self.__z = z
        else:
            self.__z = 0.0

    def get_volume(self) -> float:
        return 4 / 3 * math.pi * pow(self.__radius, 3)

    def get_square(self) -> float:
        return 4 * math.pi * pow(self.__radius, 2)

    def is_point_inside(self, x, y, z) -> bool:
        first_dist = self.__get_sqr(self.__x, x)
        second_dist = self.__get_sqr(self.__y, y)
        third_dist = self.__get_sqr(self.__z, z)
        return (first_dist + second_dist + third_dist) < pow(2, self.__radius)

    def get_radius(self) -> float:
        return self.__radius

    def get_center(self) -> tuple:
        return self.__x, self.__y, self.__z

    def set_radius(self, r):
        self.__radius = r

    def set_center(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    def __get_sqr(self, x, x1) -> float:
        return pow((x-x1), 2)


def main():
    s0 = Sphere(0.5)  # test sphere creation with radius and default center
    print(s0.get_center())
    print(s0.get_square())# (0.0, 0.0, 0.0)
    print(s0.get_volume())  # 0.523598775598
    print(s0.is_point_inside(0, -1.5, 0))  # False
    s0.set_radius(1.6)
    print(s0.is_point_inside(0, -1.5, 0))  # True
    print(s0.get_radius())  # 1.6


main()