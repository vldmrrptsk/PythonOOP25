class ListItem:
    def __init__(self, data=None, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        self.__next_node = next_node


class SinglyLinkedList:
    def __init__(self):
        self.__head = None
        self.__count = 0

    def get_size_list(self):
        return self.__count

    def get_head_list(self):
        return self.__head

    def check_list(self, index=None):

        if self.__head is None:
            raise IndexError("Список пустой")

        if isinstance(index, int) and (index >= self.__count or index < 0):
            raise IndexError("Индекс выходит за пределы границ")

    def append(self, data):
        new_item = ListItem(data)

        if self.__head is None:
            self.__head = new_item

        else:
            current_item = self.__head
            while current_item.next_node is not None:
                current_item = current_item.next_node
            current_item.next_node = new_item

        self.__count += 1

    def get_element(self, index):

        self.check_list(index)

        current_item = self.__head
        index_element = 0
        while index_element < index:
            current_item = current_item.next_node
            index_element += 1

        return f"Элемент {current_item.data} c индексом {index}"

    def change_element(self, index, element):

        self.check_list(index)

        current_item = self.__head
        index_element = 0

        while index_element < index:
            current_item = current_item.next_node
            index_element += 1

        current_item.data = element

    def push_head(self, data):

        new_item = ListItem(data)

        new_item.next_node = self.__head
        self.__head = new_item
        self.__count += 1

    def pop_element(self, index):
        self.check_list(index)

        if index == 0:
            self.pop_head()
        else:
            previous_item = self.__head
            current_item = self.__head
            index_element = 0

            while index_element < index:
                previous_item = current_item
                current_item = current_item.next_node
                index_element += 1

            popped_data = current_item.data
            previous_item.next_node = current_item.next_node

            self.__count -= 1

        return popped_data

    def push_element(self, index, data):
        self.check_list(index)

        if index == 0:
            self.push_head(data)

        else:
            new_item = ListItem(data)
            previous_item = self.__head
            current_item = self.__head
            index_element = 0

            while index_element < index:
                previous_item = current_item
                current_item = current_item.next_node
                index_element += 1

            previous_item.next_node = new_item
            new_item.next_node = current_item

            self.__count += 1

    def pop_head(self):

        self.check_list()
        popped_data = self.__head.data
        self.__head = self.__head.next_node
        self.__count -= 1
        return popped_data

    def pop_node(self, element):

        self.check_list()

        if self.__head.data == element:
            self.pop_head()
            return True

        previous_item = self.__head
        current_item = self.__head.next_node

        while current_item is not None:
            if current_item.data == element:
                previous_item.next_node = current_item.next_node
                self.__count -= 1
                return current_item.data
            previous_item = current_item
            current_item = current_item.next_node

        return False

    def __repr__(self):
        if self.__head is None:
            raise IndexError("Список пустой")

        list_elements = []
        current_item = self.__head
        while current_item:
            list_elements.append(current_item.data)
            current_item = current_item.next_node

        return f"Cписок: {str(list_elements)}"
