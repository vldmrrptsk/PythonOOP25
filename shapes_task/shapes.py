from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def get_width(self):
        pass

    @abstractmethod
    def get_height(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass


class Square(Shape):
    def __init__(self, side: float) -> None:
        self.__side = side

    @property
    def side(self) -> float:
        return self.__side

    @side.setter
    def side(self, side: float) -> None:
        self.__side = side

    def get_width(self):
        return self.__side

    def get_height(self):
        return self.__side

    def get_area(self):
        return self.__side * self.__side

    def get_perimeter(self):
        return 4 * self.__side


class Triangle(Shape):
    def __init__(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float) -> None:
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__x3 = x3
        self.__y3 = y3

    @property
    def points(self):
        return self.__x1, self.__y1, self.__x2, self.__y2, self.__x3, self.__y3

    @points.setter
    def points(self, new_points) -> None:
        new_points = (self.__x1, self.__y1), (self.__x2, self.__y2), (self.__x3, self.__y3)

    def get_width(self) -> float:
        return max(self.__x1, self.__x2, self.__x3) - min(self.__x1, self.__x2, self.__x3)

    def get_height(self) -> float:
        return max(self.__y1, self.__y2, self.__y3) - min(self.__y1, self.__y2, self.__y3)

    def get_area(self) -> float:
        return abs(
            (self.__x1 * (self.__y2 - self.__y3) +
             self.__x2 * (self.__y3 - self.__y1) +
             self.__x3 * (self.__y1 - self.__y2)) / 2)

    def get_perimeter(self) -> float:
        side_a = math.hypot(self.__x2 - self.__x1, self.__y2 - self.__y1)
        side_b = math.hypot(self.__x3 - self.__x2, self.__y3 - self.__y2)
        side_c = math.hypot(self.__x1 - self.__x3, self.__y1 - self.__y3)
        return side_a + side_b + side_c


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.__width = width
        self.__height = height

    @property
    def sides(self):
        return self.__width, self.__height

    @sides.setter
    def sides(self, new_sides) -> None:
        new_sides = self.__width, self.__height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_area(self):
        return self.__width * self.__height

    def get_perimeter(self):
        return 2 * (self.__width + self.__height)


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.__radius = radius

    @property
    def radius(self) -> float:
        return self.__radius

    @radius.setter
    def radius(self, radius: float) -> None:
        self.__radius = radius

    def get_width(self):
        return 2 * self.__radius

    def get_height(self):
        return 2 * self.__radius

    def get_area(self):
        return math.pi * self.__radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.__radius
