from range_task.range import Range
import random

range = Range(2.5, 7.8)
print(f"Диапазон: от {range.start} до {range.end}")
print(f"Длина диапазона: {range.length}")

input_number = 5.0
print(f"Число {input_number} внутри диапазона? {range.is_inside(input_number)}")

a = random.randint(0, 100)
b = random.randint(a, 100)
c = random.randint(0, 100)
d = random.randint(c, 100)
range1 = Range(a, b)
range2 = Range(c, d)
print(f"Интервал пересечения, {(a, b)}, {c, d}: {Range.get_interval_intersection(range1, range2)}")
print(f"Интервал объединения, {(a, b)}, {c, d}: {Range.get_interval_union(range1, range2)}")
print(f"Разность интервалов, {(a, b)}, {c, d}: {Range.get_interval_difference(range1, range2)}")

