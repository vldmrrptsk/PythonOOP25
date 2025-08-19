from shapes_task.shapes import Shape

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

    def __repr__(self) -> str:
        return f"Квадрат со стороной {self.__side}"

    def __eq__(self, other):
        if not isinstance(other, Square):
            return NotImplemented

        return self.__side == other.__side

    def __hash__(self):
        return hash(self.__side)