from array_list_home_task.arraylist import ArrayListHome

list_home = ArrayListHome()
print("Список: ", list_home.read_from_file("list"))
print("Список без четных чисел: ", list_home.remove_even())

list_home = ArrayListHome()
list_home.read_from_file("list")
print("Список никальных значения: ", list_home.get_unique_array())
