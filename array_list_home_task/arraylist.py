class ArrayListHome:
    def __init__(self):
        self.__list_items = []

    def read_from_file(self, name: str):
        with open(f"{name}.txt", "r", encoding="utf-8") as file:
            for line in file:
                numbers_in_line = [int(num) for num in line.split()]
                self.__list_items.extend(numbers_in_line)
        return self.__list_items

    def remove_even(self):
        fix_idx = 0
        number_of_elements = len(self.__list_items)

        for index in range(number_of_elements):
            if abs(self.__list_items[index]) % 2 != 0:
                self.__list_items[fix_idx] = self.__list_items[index]
                fix_idx += 1

        self.__list_items = self.__list_items[:fix_idx]
        return self.__list_items

    @staticmethod
    def check_in(array_list, element):
        for item in array_list:
            if item == element:
                return True
        return False

    def get_unique_array(self):
        new_list = []
        for item in self.__list_items:
            if not self.check_in(new_list, item):
                new_list.append(item)

        return new_list
