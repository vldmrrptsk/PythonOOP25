from lambda_task.person import Person
from operator import attrgetter

people = [
    Person("Иван", 25),
    Person("Мария", 30),
    Person("Петр", 35),
    Person("Анна", 28),
    Person("Сергей", 42),
    Person("Сергей", 83),
    Person("Анна", 10),
    Person("Иван", 10),
    Person("Иван", 12),
]


def get_unique_names(people_list: list) -> list[str]:
    all_names = set(map(lambda p: p.name, people_list))
    unique_names = list(all_names)

    return unique_names


def get_people_filtered_age(people_list: list, age_filter_left: int = 0, age_filter_right: int = 100) -> tuple:
    all_names_less_filter = list(filter(lambda p: age_filter_left <= p.age <= age_filter_right, people_list))

    names = list(map(lambda p: p.name, all_names_less_filter))
    ages = list(map(lambda p: p.age, all_names_less_filter))

    names = ", ".join(names)
    average_age = round(sum(ages) / len(ages))

    return names, average_age


def get_grouped_by(people_list: list) -> dict:
    name_age_pairs = list(map(lambda p: (p.name, p.age), people_list))

    grouped = {}
    for name, age in name_age_pairs:
        if name not in grouped:
            grouped[name] = []
        grouped[name].append(age)

    average_age_by_name = {
        name: round(sum(ages) / len(ages))
        for name, ages in grouped.items()
    }

    return average_age_by_name


def get_sorted_range_names(people_list: list, age_filter_left: int = 0, age_filter_right: int = 100) -> tuple:
    sorted_names = sorted(people_list, key=attrgetter("age"), reverse=True)

    return get_people_filtered_age(sorted_names, age_filter_left, age_filter_right)[0]


print(f"a. Список уникальных имен: {get_unique_names(people)}", "\n")
print(f"б. Имена: {", ".join(get_unique_names(people))}", "\n")
print(f"в. {get_people_filtered_age(people, 0, 18)[0]} младше 18, и имеют средний возраст "
      f"{get_people_filtered_age(people, 0, 18)[1]}", "\n")
print(f"г. Группировка: {get_grouped_by(people)}")
print(f"д. Список людей от 20 до 45: {get_sorted_range_names(people, 20, 45)}", "\n")
