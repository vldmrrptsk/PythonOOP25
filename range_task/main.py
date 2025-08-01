from range_task.range import Range

diapason = Range(2.5, 7.8)
print(f"Диапазон: от {diapason.start} до {diapason.end}")
print(f"Длина диапазона: {diapason.length}")
input_number = 5.0
print(f"Число {input_number} внутри диапазона? {diapason.is_inside(input_number)}")
