import math


def infinite_square_roots(number=0):
    while True:
        yield math.sqrt(number)
        number += 1


print("Введите число элементов для вывода: ")
input_number = int(input())
root = infinite_square_roots()
for i in range(input_number):
    print(f"{next(root):.2f}")


def fibonacci():
    number_1 = 0
    number_2 = 1
    while True:
        yield number_1
        number_1 = number_2
        number_2 = number_1 + number_2


print("Введите число элементов для вывода чисел Фибоначчи: ")
input_number = int(input())
fib = fibonacci()
for i in range(input_number):
    print(next(fib))
