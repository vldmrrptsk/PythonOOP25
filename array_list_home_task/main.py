import random


def create_file_with_lists() -> str:
    print("Введите путь к файлу:")
    path = input().strip().strip('"').strip("'")
    print("Введите количестов строк:")
    number_lists = int(input().strip())
    print("Введите максимальную длину строки:")
    max_length = int(input().strip())
    print("Введите желаемы диапозон чисел в строке:")
    min_value, max_value = map(int, input().strip().split())

    with open(path, "w") as file:
        for i in range(number_lists):
            length = random.randint(1, max_length)
            numbers = [random.randint(min_value, max_value) for _ in range(length)]

            file.write(' '.join(map(str, numbers)) + "\n")

    return path


def read_lists_from_file(path: str) -> None:
    try:
        list_items = []
        with open(path, "r", encoding="utf-8") as file:
            for line in file.readlines():
                clean_line = line.strip()
                list_items.append(clean_line)
        return list_items

    except FileNotFoundError:
        print(f"Файл {path} не найден!")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")


created_path = create_file_with_lists()
print(f"Список строк из файла: {read_lists_from_file(created_path)}")
print()


def remove_even_number(input_list: list[int]) -> None:
    fixed_index = 0
    number_of_elements = len(input_list)

    for index in range(number_of_elements):
        if abs(input_list[index]) % 2 != 0:
            input_list[fixed_index] = input_list[index]
            fixed_index += 1

    input_list[:] = input_list[:fixed_index]


random_input_list = [random.randint(1, 100) for _ in range(10)]
print(f"Первоначальный список чисел: {random_input_list}")
remove_even_number(random_input_list)
print(f"Список без четных чисел: {random_input_list}")
print()


def get_unique_elements_list(input_list: list[int]) -> list[int]:
    new_list = []
    for item in input_list:
        if item not in new_list:
            new_list.append(item)

    return new_list


random_input_list = [random.randint(1, 100) for _ in range(10)]
print(f"Первоначальный список чисел: {random_input_list}")
print(f"Список без дублей: {get_unique_elements_list(random_input_list)}")
print()
