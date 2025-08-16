from range_task.range import Range
import random

rg = Range(2.5, 7.8)
print(f"Диапазон: от {rg.start} до {rg.end}")
print(f"Длина диапазона: {rg.length}")

input_number = 5.0
print(f"Число {input_number} внутри диапазона? {rg.is_inside(input_number)}")

first_left_boarder = random.randint(0, 100)
first_right_boarder = random.randint(first_left_boarder, 100)
second_left_boarder = random.randint(0, 100)
second_right_boarder = random.randint(second_left_boarder, 100)

interval_1 = Range(first_left_boarder, first_right_boarder)
interval_2 = Range(second_left_boarder, second_right_boarder)

print(f"Пересечение интервалов {first_left_boarder, first_right_boarder},"
      f" {second_left_boarder, second_right_boarder}:"
      f" {interval_1.get_interval_intersection(interval_2)}")
print(f"Объединение интервалов {first_left_boarder, first_right_boarder}, "
      f"{second_left_boarder, second_right_boarder}: "
      f"{interval_1.get_interval_union(interval_2)}")
print(f"Разность интервалов {first_left_boarder, first_right_boarder}, "
      f"{second_left_boarder, second_right_boarder}: "
      f"{Range.get_interval_difference(interval_1, interval_2)}")
