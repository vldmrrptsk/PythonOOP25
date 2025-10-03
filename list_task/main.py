from list_task.list import SinglyLinkedList

new_list = SinglyLinkedList()

new_list.append(5)
new_list.append(6)
new_list.append(9)
new_list.append(-1)
new_list.append(100)
print(f"{new_list}, Размер: {new_list.get_size_list()}")

print(new_list.get_element(4))

new_list.change_element(2, 2)
print(f"{new_list}, Размер: {new_list.get_size_list()}")

new_list.push_head(10)
print(f"{new_list}, Размер: {new_list.get_size_list()}")

popped = new_list.pop_element(2)
print(f"Удален: {popped}, {new_list}")

new_list.push_element(1, 15)
print(f"{new_list}, Размер: {new_list.get_size_list()}")

new_list.pop_head()
print(f"{new_list}, Размер: {new_list.get_size_list()}")

new_list.pop_node(15)
print(f"{new_list}, Размер: {new_list.get_size_list()}")
