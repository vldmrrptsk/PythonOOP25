from shapes_task.shape import Shape
import math


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.__radius = radius

    @property
    def radius(self) -> float:
        return self.__radius

    @radius.setter
    def radius(self, radius: float) -> None:
        self.__radius = radius

    def get_width(self) -> float:
        return 2 * self.__radius

    def get_height(self) -> float:
        return 2 * self.__radius

    def get_area(self) -> float:
        return math.pi * self.__radius ** 2

    def get_perimeter(self) -> float:
        return 2 * math.pi * self.__radius

    def __repr__(self) -> str:
        return f"Окружность с радиусом {self.__radius}"

    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented

        return self.__radius == other.__radius

    def __hash__(self):
        return hash(self.__radius)
