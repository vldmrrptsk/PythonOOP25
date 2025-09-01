from shapes_task.shape import Shape


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.__width = width
        self.__height = height

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, width) -> None:
        self.__width = width

    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, height) -> None:
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_area(self):
        return self.__width * self.__height

    def get_perimeter(self):
        return 2 * (self.__width + self.__height)

    def __repr__(self) -> str:
        return f"Прямоугольник с шириной {self.__width} и высотой {self.__height}"

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented

        return self.__width == other.__width and self.__height == other.__height

    def __hash__(self):
        return hash((self.__width, self.__height))
