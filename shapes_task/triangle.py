from shapes_task.shape import Shape
import math


class Triangle(Shape):
    def __init__(self, x_1: float, y_1: float, x_2: float, y_2: float, x_3: float, y_3: float) -> None:
        self.__x_1 = x_1
        self.__y_1 = y_1
        self.__x_2 = x_2
        self.__y_2 = y_2
        self.__x_3 = x_3
        self.__y_3 = y_3

    @property
    def x_1(self) -> float:
        return self.__x_1

    @x_1.setter
    def x_1(self, x_1) -> None:
        self.__x_1 = x_1

    @property
    def x_2(self) -> float:
        return self.__x_2

    @x_2.setter
    def x_2(self, x_2) -> None:
        self.__x_2 = x_2

    @property
    def x_3(self) -> float:
        return self.__x_3

    @x_3.setter
    def x_3(self, x_3) -> None:
        self.__x_3 = x_3

    @property
    def y_1(self) -> float:
        return self.__y_1

    @y_1.setter
    def y_1(self, y_1) -> None:
        self.__y_1 = y_1

    @property
    def y_2(self) -> float:
        return self.__y_2

    @y_2.setter
    def y_2(self, y_2) -> None:
        self.__y_2 = y_2

    @property
    def y_3(self) -> float:
        return self.__y_3

    @y_3.setter
    def y_3(self, y_3) -> None:
        self.__y_3 = y_3

    def get_width(self) -> float:
        return max(self.__x_1, self.__x_2, self.__x_3) - min(self.__x_1, self.__x_2, self.__x_3)

    def get_height(self) -> float:
        return max(self.__y_1, self.__y_2, self.__y_3) - min(self.__y_1, self.__y_2, self.__y_3)

    def get_area(self) -> float:
        return abs(
            (self.__x_1 * (self.__y_2 - self.__y_3) +
             self.__x_2 * (self.__y_3 - self.__y_1) +
             self.__x_3 * (self.__y_1 - self.__y_2)) / 2)

    def get_perimeter(self) -> float:
        side_a = math.hypot(self.__x_2 - self.__x_1, self.__y_2 - self.__y_1)
        side_b = math.hypot(self.__x_3 - self.__x_2, self.__y_3 - self.__y_2)
        side_c = math.hypot(self.__x_1 - self.__x_3, self.__y_1 - self.__y_3)

        return side_a + side_b + side_c

    def __repr__(self) -> str:
        return (f"Треугольник с вершинами ({self.__x_1} {self.__y_1})"
                f"({self.__x_2} {self.__y_2}), "
                f"({self.__x_3} {self.__y_3}),")

    def __eq__(self, other):
        if not isinstance(other, Triangle):
            return NotImplemented

        return (
                self.__x_1 == other.__x_1 and self.__y_1 == other.__y_1 and
                self.__x_2 == other.__x_2 and self.__y_2 == other.__y_2 and
                self.__x_3 == other.__x_3 and self.__y_3 == other.__y_3
        )

    def __hash__(self):
        return hash((self.__x_1, self.__x_2, self.__x_3,
                     self.__y_1, self.__y_2, self.__y_3))
