from vector_task.vector import Vector
import math


def test_constructor():
    """Тестирование конструкторов"""
    print("=" * 50)
    print("ТЕСТИРОВАНИЕ КОНСТРУКТОРОВ")
    print("=" * 50)

    # Конструктор с размером
    v1 = Vector(3)
    print(f"Vector(3) = {v1}")

    # Конструктор со списком
    v2 = Vector([1, 2, 3])
    print(f"Vector([1, 2, 3]) = {v2}")

    # Конструктор с кортежем
    v3 = Vector((4, 5, 6))
    print(f"Vector((4, 5, 6)) = {v3}")

    # Конструктор копирования
    v4 = Vector(v2)
    print(f"Vector(v2) = {v4}")

    # Конструктор с размером и компонентами
    v5 = Vector(5, [7, 8, 9])
    print(f"Vector(5, [7, 8, 9]) = {v5}")

    print()


test_constructor()


def test_properties():
    """Тестирование свойств"""
    print("=" * 50)
    print("ТЕСТИРОВАНИЕ СВОЙСТВ")
    print("=" * 50)

    v = Vector([3, 4])
    print(f"Вектор: {v}")
    print(f"Размер: {v.size}")
    print(f"Длина: {v.length:.2f}")
    print(f"Проверка длины: {v.length == math.sqrt(3 ** 2 + 4 ** 2)}")


test_properties()


def test_addition():
    """Тестирование сложения"""
    print("=" * 50)
    print("ТЕСТИРОВАНИЕ СЛОЖЕНИЯ")
    print("=" * 50)

    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    v3 = Vector([7, 8])

    # Сложение одинакового размера
    result1 = v1 + v2
    print(f"{v1} + {v2} = {result1}")

    # Сложение разного размера
    result2 = v1 + v3
    print(f"{v1} + {v3} = {result2}")

    # In-place сложение
    v1_copy = Vector(v1)
    v1_copy += v2
    print(f"{v1} += {v2} = {v1_copy}")

    print()


test_addition()


def test_subtraction():
    """Тестирование вычитания"""
    print("=" * 50)
    print("ТЕСТИРОВАНИЕ ВЫЧИТАНИЯ")
    print("=" * 50)

    v1 = Vector([10, 20, 30])
    v2 = Vector([1, 2, 3])
    v3 = Vector([5, 6])

    # Вычитание одинакового размера
    result1 = v1 - v2
    print(f"{v1} - {v2} = {result1}")

    # Вычитание разного размера
    result2 = v1 - v3
    print(f"{v1} - {v3} = {result2}")

    # In-place вычитание
    v1_copy = Vector(v1)
    v1_copy -= v2
    print(f"{v1} -= {v2} = {v1_copy}")

    print()


test_subtraction()


def test_multiplication():
    """Тестирование умножения"""
    print("=" * 50)
    print("ТЕСТИРОВАНИЕ УМНОЖЕНИЯ")
    print("=" * 50)

    v = Vector([1, 2, 3])

    # Умножение на скаляр
    result1 = v * 2
    print(f"{v} * 2 = {result1}")

    v_copy = Vector(v)
    v_copy *= 4
    print(f"{v} *= 4 = {v_copy}")

    print()


test_multiplication()


def test_comparison():
    """Тестирование сравнения"""
    print("=" * 50)
    print("ТЕСТИРОВАНИЕ СРАВНЕНИЯ")
    print("=" * 50)

    v1 = Vector([1, 2, 3])
    v2 = Vector([1, 2, 3])
    v3 = Vector([4, 5, 6])
    v4 = Vector([1, 2])

    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v3 = {v3}")
    print(f"v4 = {v4}")

    print(f"v1 == v2: {v1 == v2}")
    print(f"v1 == v3: {v1 == v3}")
    print(f"v1 == v4: {v1 == v4}")
    print(f"v1 != v3: {v1 != v3}")

    print()


test_comparison()
