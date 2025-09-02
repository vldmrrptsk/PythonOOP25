from range_task.range import Range
import random

interval = Range(2.5, 7.8)
print(f"Диапазон: от {interval.start} до {interval.end}")
print(f"Длина диапазона: {interval.length}")

input_number = 5.0
print(f"Число {input_number} внутри диапазона? {interval.is_inside(input_number)}")

left_border_1 = random.randint(0, 100)
right_border_1 = random.randint(left_border_1, 100)

left_border_2 = random.randint(0, 100)
right_border_2 = random.randint(left_border_2, 100)

interval_1 = Range(left_border_1, right_border_1)
interval_2 = Range(left_border_2, right_border_2)

print(f"Пересечение интервалов {left_border_1, right_border_1},"
      f" {left_border_2, right_border_2}:"
      f" {interval_1.get_intersection(interval_2)}")
print(f"Объединение интервалов {left_border_1, right_border_1}, "
      f"{left_border_2, right_border_2}: "
      f"{interval_1.get_union(interval_2)}")
print(f"Разность интервалов {left_border_1, right_border_1}, "
      f"{left_border_2, right_border_2}: "
      f"{Range.get_difference(interval_1, interval_2)}")
