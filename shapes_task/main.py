from shapes_task.square import Square
from shapes_task.triangle import Triangle
from shapes_task.rectangle import Rectangle
from shapes_task.circle import Circle

shapes = [
    Square(5),
    Triangle(0, 0, 3, 0, 0, 4),
    Rectangle(4, 6),
    Circle(3),
    Square(7),
    Triangle(0, 0, 6, 0, 3, 5),
    Rectangle(5, 5),
    Circle(4.5),
    Triangle(1, 1, 4, 1, 2, 5),
    Rectangle(2, 8)
]


def get_max_area_shape(figures):
    return sorted(figures, key=lambda shape: shape.get_area(), reverse=True)[0]


def get_second_max_perimeter_shape(figures):
    return sorted(figures, key=lambda shape: shape.get_perimeter(), reverse=True)[1]


max_area_shape = get_max_area_shape(shapes)
print("Фигура с максимальной площадью:")
print(max_area_shape)
print(f"Площадь: {max_area_shape.get_area()}")
print()

second_perimeter_shape = get_second_max_perimeter_shape(shapes)
print("Фигура со вторым по величине периметром:")
print(second_perimeter_shape)
print(f"Периметр: {second_perimeter_shape.get_perimeter()}")
