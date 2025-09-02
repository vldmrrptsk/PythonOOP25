import math


class Vector:
    def __init__(self, size: int or list[int] = None, components: list[int] or "Vector" = None) -> None:

        if size is None and components is None:
            raise ValueError(f"At least one argument must be filed in!")

        if size is not None and components is None:

            if isinstance(size, int):

                if size <= 0:
                    raise ValueError(f"Size must be > 0, Specified value = {size}")

                self.__size = size
                self.__items = [0] * size

            elif isinstance(size, (list, tuple)):
                self.__size = len(size)
                self.__items = [item for item in size]

            elif isinstance(size, Vector):
                self.__size = size.__size
                self.__items = size.__items.copy()

            else:
                raise TypeError(f"First argument must be integer, "
                                f"list, tuple or Vector not {type(size).__name__}")

        elif size is not None and components is not None:
            if not isinstance(components, (list | tuple)):
                raise TypeError(f"Components must be list or Vector type")

            self.__size = size
            components_length = len(components)

            if size < components_length:
                self.__items = [0] * components_length
            else:
                self.__items = [0] * size

            for element in range(components_length):
                self.__items[element] = components[element]

    @property
    def size(self) -> int:
        return self.__size

    @property
    def length(self) -> float:
        return math.sqrt(sum(x * x for x in self.__items))

    def __repr__(self) -> str:
        components_str = ", ".join(str(x) for x in self.__items)
        return f"{{{components_str}}}"

    def __add__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise TypeError(f"It is allowed to add only vectors!")

        max_size = max(self.__size, other.__size)
        result = Vector(max_size)

        for i in range(self.__size):
            result.__items[i] += self.__items[i]

        for i in range(other.__size):
            result.__items[i] += other.__items[i]

        return result

    def __iadd__(self, other: "Vector") -> "Vector":

        if not isinstance(other, Vector):
            raise TypeError(f"It is allowed to add only vectors!")

        if self.__size < other.__size:
            self.__items.extend([0] * (other.__size - self.__size))

        for item in range(other.__size):
            self.__items[item] += other.__items[item]

        return self

    def __sub__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise TypeError(f"It is allowed to add only vectors!")

        max_size = max(self.__size, other.__size)
        result = Vector(max_size)

        for i in range(self.__size):
            result.__items[i] += self.__items[i]

        for i in range(other.__size):
            result.__items[i] -= other.__items[i]

        return result

    def __isub__(self, other: "Vector") -> "Vector":

        if not isinstance(other, Vector):
            raise TypeError(f"It is allowed to add only vectors!")

        if self.__size < other.__size:
            self.__items.extend([0] * (other.__size - self.__size))

        for item in range(other.__size):
            self.__items[item] -= other.__items[item]

        return self

    def __mul__(self, scalar: int) -> "Vector":
        if not isinstance(scalar, int):
            raise TypeError(f"Element must be integer, not {type(scalar)}")

        result = Vector(self.__size)

        for i in range(self.__size):
            result.__items[i] = scalar * self.__items[i]

        return Vector(result)

    def __imul__(self, scalar: int) -> "Vector":
        if not isinstance(scalar, int):
            raise TypeError(f"Element must be ingere, not {type(scalar)}")

        for item in range(self.__size):
            self.__items[item] *= scalar

        return self

    def __eq__(self, other: "Vector") -> bool:

        if not isinstance(other, Vector):
            raise TypeError(f"It is allowed to compare only vectors!")

        if self.__items == other.__items and self.__size == other.__size:
            return True

        return False

    def __getitem__(self, index: int) -> int:

        if index < 0 or index >= self.__size:
            raise IndexError(f"Index {index} out of size {self.__size}")
        return self.__items[index]

    def __setitem__(self, index: int, value: int) -> None:

        if index < 0 or index >= self.__size:
            raise IndexError(f"Index {index} out of size {self.__size}")
        self.__items[index] = value

    def __hash__(self) -> int:
        return hash(tuple(self.__items))
