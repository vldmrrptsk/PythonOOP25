from shapes_task.shapes import Shape, Square, Triangle, Rectangle, Circle
import random

shapes_list = ['Square', 'Triangle', 'Rectangle', 'Circle']
area_dict = {}
perimetr_dict = {}
i, j, k, p, area, perimeter = 0, 0, 0, 0, 0, 0

for _ in range(1, 11):
    figure = random.choice(shapes_list)

    if figure == 'Square':
        side = random.randint(1, 20)
        sq = Square(side)
        area = sq.get_area()
        perimeter = sq.get_perimeter()
        i += 1
        figure = figure + str(i)

    if figure == 'Triangle':
        x1 = random.randint(0, 20)
        y1 = random.randint(0, 20)
        x2 = random.randint(0, 20)
        y2 = random.randint(0, 20)
        x3 = random.randint(0, 20)
        y3 = random.randint(0, 20)
        tr = Triangle(x1, y1, x2, y2, x3, y3)
        area = tr.get_area()
        perimeter = tr.get_perimeter()
        j += 1
        figure = figure + str(j)

    if figure == 'Rectangle':
        width = random.randint(1, 20)
        height = random.randint(1, 20)
        rc = Rectangle(width, height)
        area = rc.get_area()
        perimeter = rc.get_perimeter()
        p += 1
        figure = figure + str(p)

    if figure == 'Circle':
        radius = random.randint(1, 20)
        cr = Circle(radius)
        area = cr.get_area()
        perimeter = cr.get_perimeter()
        k += 1
        figure = figure + str(k)

    area_dict[figure] = area
    perimetr_dict[figure] = perimeter

sorted_areas = sorted(area_dict.items(), key=lambda x: x[1], reverse=True)
sorted_perimetrs = sorted(perimetr_dict.items(), key=lambda x: x[1], reverse=True)
print(f"Фигура с наибольшей площадью: {sorted_areas[0]}")
print(f"Фигура со вторым по величине периметром: {sorted_perimetrs[1]}")
