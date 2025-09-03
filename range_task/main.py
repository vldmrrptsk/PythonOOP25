from range_task.range import Range
import random

range = Range(2.5, 7.8)
print(f"Диапазон: от {range.start} до {range.end}")
print(f"Длина диапазона: {range.length}")

input_number = 5.0
print(f"Число {input_number} внутри диапазона? {range.is_inside(input_number)}")

left_border_1 = random.randint(0, 100)
right_border_1 = random.randint(left_border_1, 100)

left_border_2 = random.randint(0, 100)
right_border_2 = random.randint(left_border_2, 100)

range_1 = Range(left_border_1, right_border_1)
range_2 = Range(left_border_2, right_border_2)

print(f"Пересечение интервалов {left_border_1, right_border_1},"
      f" {left_border_2, right_border_2}:"
      f" {range_1.get_intersection(range_2)}")
print(f"Объединение интервалов {left_border_1, right_border_1}, "
      f"{left_border_2, right_border_2}: "
      f"{range_1.get_union(range_2)}")
print(f"Разность интервалов {left_border_1, right_border_1}, "
      f"{left_border_2, right_border_2}: "
      f"{range_1.get_difference(range_2)}")
